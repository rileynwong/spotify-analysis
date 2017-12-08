from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import csv


def get_features(track_id):
    features_results = sp.audio_features([track_id])
    json_features = json.dumps(features_results)
    features_data = json.loads(json_features)

    # Convert features dictionary to a list
    features_list = list(features_data[0].values())

    return features_list


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

# Audio features
feature_names = [
  "danceability",
  "energy",
  "key",
  "loudness",
  "mode",
  "speechiness",
  "acousticness",
  "instrumentalness",
  "liveness",
  "valence",
  "tempo",
  "type",
  "id",
  "uri",
  "track_href",
  "analysis_url",
  "duration_ms",
  "time_signature"
]

username = '1240951381'

### Write data to CSV file
data_file = open('data.csv','w')
writer = csv.writer(data_file)

# Write header
writer.writerow(['track_id', 'date_added'] + feature_names)

for playlist_id in playlist_ids:

    # Query Spotify API
    results = sp.user_playlist(username, playlist_id)
    json_results = json.dumps(results, indent=4)
    data = json.loads(json_results)

    # Write rows
    for track in data['tracks']['items']:
        track_id = track['track']['id']
        date_added = track['added_at']

        # Track features
        features = get_features(track_id)

        writer.writerow([track_id, date_added] + features)

data_file.close()

