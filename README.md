# DeezerToSpotifyPlaylist README :

## Setup
First you need to register for a client_id and client_secret via Spotify for developpers and file the tokens in ```secret.json.sample```, rename it ```secret.json``` and install ```jq``` command for bash.

Then the app will ask for authentification via spotify/authorize for creating playlist scope.

Finally the app will search for the deezer music on spotify and append it in the new created spotify playlist.

## How to run the app :
```bash
./migrate <url_for_deezer_playlist>
```

## Enjoy and feel free to improve or raise issues