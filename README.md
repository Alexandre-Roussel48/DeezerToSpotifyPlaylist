# DeezerToSpotifyPlaylist

DeezerToSpotifyPlaylist is a handy tool that allows users to seamlessly migrate Deezer playlists to Spotify. The project is written in a combination of Bash, Python, and a touch of HTML to provide a smooth and efficient playlist migration process.

## Prerequisites

Before getting started with the migration process, ensure you have the following prerequisites installed:

1. **jq:** The migration script relies on jq, a lightweight and flexible command-line JSON processor. Install it by running ```sudo apt install jq``` in your bash terminal.

2. **Spotify Developer App:** To make API calls to Spotify, you need to create a Spotify Developer App and obtain client tokens. Follow the steps below to create your app:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Log in or create a Spotify account.
   - Click on "Create an App" and fill in the required information (in Redirect URIs be sure to put : ```http://localhost:8000``` or the app will not work).
   - Once your app is created, note down the client ID and client secret in the ```secret.json.sample``` and rename it to ```secret.json```.

## Installation

1. Clone the DeezerToSpotifyPlaylist repository to your local machine:

   ```bash
   git clone https://github.com/Alexandre-Roussel48/DeezerToSpotifyPlaylist.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DeezerToSpotifyPlaylist
   ```

3. Make the migration script executable:

   ```bash
   chmod +x migrate
   ```

## Usage

To migrate a Deezer playlist to Spotify, follow these steps:

1. Launch the migration script in your terminal:

   ```bash
   ./migrate <url_for_deezer_playlist>
   ```

2. The script will prompt you to authenticate with your Spotify account. Follow the on-screen instructions.

3. Once authenticated, the script will create a new playlist on your Spotify profile and add songs from the Deezer playlist to it.

## Important Note

Please make sure to keep your Spotify client ID and client secret confidential. Do not share them or embed them directly in your code.

## Contributors

- [Alexandre Roussel](https://github.com/Alexandre-Roussel48)

## License

This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/Alexandre-Roussel48/DeezerToSpotifyPlaylist/main/LICENSE) file for details.

---

Feel free to contribute to the project and make it even better! If you encounter any issues, please report them in the [Issues](https://github.com/Alexandre-Roussel48/DeezerToSpotifyPlaylist/issues) section.
