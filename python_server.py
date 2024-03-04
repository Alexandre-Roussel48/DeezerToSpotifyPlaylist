from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except FileNotFoundError:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Print the received content and stop serving further requests
        file_path = "token.json"

        # Create the file and write JSON content
        with open(file_path, 'w') as file:
            json.dump(json.loads(post_data), file)
        self.server.server_close()

if __name__ == '__main__':
    port = 8000
    server_address = ('', port)

    try:
        httpd = HTTPServer(server_address, MyRequestHandler)
        print(f"Server started on port {port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
        httpd.server_close()

