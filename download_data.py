from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import csv
import pylyrics3
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


def get_features(track_id):
    features_results = sp.audio_features([track_id])
    json_features = json.dumps(features_results)
    features_data = json.loads(json_features)

    # Convert features dictionary to a list
    features_list = list(features_data[0].values())

    return features_list


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sentiment_analyzer = SIA()

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
writer.writerow(['track_id', 'playlist_id', 'date_added', 'track_name', 'first_artist'] + feature_names + ['lyrics', 'neg', 'neu', 'pos', 'compound'])

for playlist_id in playlist_ids:
    print('Querying playlist: ' + str(playlist_id))

    repeat_query = True
    offset_n = 0
    for i in range(2):
        # Query Spotify API
        if i > 0:
            print('Repeating query')
            offset_n += 100
        results = sp.user_playlist_tracks(username, playlist_id, offset=offset_n)
        json_results = json.dumps(results)
        data = json.loads(json_results)

        # Write rows
        for track in data['items']:
            track_id = track['track']['id']
            date_added = track['added_at']
            track_name = track['track']['name']
            first_artist = track['track']['artists'][0]['name']

            # Track features
            features = get_features(track_id)

            # Try to get lyrics, if available
            lyrics = ''
            try:
                lyrics = pylyrics3.get_song_lyrics(first_artist, track_name)
            except:
                pass

            # Sentiment Analysis
            neg = None
            neu = None
            pos = None
            compound = None
            if lyrics:
                snt = sentiment_analyzer.polarity_scores(lyrics)
                neg = snt['neg']
                neu = snt['neu']
                pos = snt['pos']
                compound = snt['compound']

            writer.writerow([track_id, playlist_id, date_added, track_name, first_artist] + features + [lyrics] + [neg, neu, pos, compound])

        # Special case: API limit is 100 tracks, so we need a second request
        # for playlists that have over 100 tracks
        if data['total'] < 100:
            break

    print('Done querying')

data_file.close()

