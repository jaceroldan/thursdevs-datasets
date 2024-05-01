import pandas as pd
import json

json_files = ['BINI.json', 'eddy_kenzo.json', 'noah_kahan.json', 'olivia_rodrigo.json', 'sabrina_carpenter.json', 'taylor_swift.json']
track_master_list = {}

for file_name in json_files:
    with open(file_name, 'r') as file:
        artist_name = file_name.replace('.json', '').replace('_', ' ').title()
        artist = json.load(file)
        tracks = artist['tracks']['items']
        track_ids = {track['name']: track['id'] for track in tracks}
        track_master_list[artist_name] = track_ids


for artist, list_of_tracks in track_master_list.items():
    print(f'Artist: {artist}')
    tracks = list(list_of_tracks.values())
    print(len(tracks))

    # Process the list in batches of 50
    for i in range(0, len(tracks), 50):
        batch = tracks[i:i + 50]
        print('[', ','.join(batch), ']')
