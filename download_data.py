from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import csv

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

### Query Spotify API
results = sp.user_playlist(username, playlist_id)
json_results = json.dumps(results, indent=4)
# print(json_results)
data = json.loads(json_results)
print("hey")
print(data['tracks'])
print(type(data['tracks']))

### Download data as CSV file
# json_parsed = json.loads(results)

# Parse JSON
save_data = open('data.csv','w')
writer = csv.writer(save_data)

count = 0
for key, value in data.items():
    if count == 0:
        header = key
        writer.writerow(header)
        count += 1
    writer.writerow(str(value))

save_data.close()

