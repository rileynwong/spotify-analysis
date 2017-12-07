from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# IDs of monthly playlists from November 2016 to November 2017
playlist_ids = [
    "07zqCIPCroFMKSajvERGvE",
    "30PgYnoeT2PAgFNuYLR5qd",
    "1vS1nakUrLYkTd3W0yRMYe",
    "3scPGVlAn7d74uXRtFnmUC",
    "5LzBRPVAPYUssZ4ZESnRmH",
    "6hDHXewz8qBTezvONSqzyl",
    "00riJCYiVJ1yptAXtv2h6k",
    "0HxFI5dOlKztf38T9sa0cF",
    "7EFWm7Mjy6GLJHOEgKEblM",
    "6YAG0Li1BoUkmhc8iycY6l",
    "7Iw0yI71QX59zyFq0kAZTS",
    "69XTCqVzbSWPMLucSvzlLl",
    "7pRnKuQMkmntEj7Nnj94r0"
]


username = '1240951381'
playlist_id = playlist_ids[0]

results = sp.user_playlist(username, playlist_id)
print(json.dumps(results, indent=4))
