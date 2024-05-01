import json
import pandas as pd

json_files = ['BINI.json', 'eddy_kenzo.json', 'noah_kahan.json', 'olivia_rodrigo.json', 'sabrina_carpenter.json', 'taylor_swift.json']
track_master_list = []

for file_name in json_files:
    with open(file_name, 'r') as file:
        artist_name = file_name.replace('.json', '').replace('_', ' ').title()
        artist = json.load(file)
        tracks = artist['tracks']['items']
        for track in tracks:
            # Create a dictionary for each track and append it to the list
            track_master_list.append({
                'Artist': artist_name,
                'Song Title': track['name'],
                'Song ID': track['id']
            })

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(track_master_list)

import json
import pandas as pd

audio_feature_files = ['BINI_af.json', 'eddy_kenzo_af.json', 'olivia_rodrigo_af.json', 'sabrina_carpenter_af.json', 'taylor_swift_af.json']  # Example file names
audio_features_list = []

for file_name in audio_feature_files:
    with open(file_name, 'r') as file:
        data = json.load(file)
        for feature in data['audio_features']:
            audio_features_list.append(feature)

# Create a DataFrame from the list of audio features
audio_features_df = pd.DataFrame(audio_features_list)

df['Song ID'] = df['Song ID'].astype(str)
audio_features_df['id'] = audio_features_df['id'].astype(str)

# Merge the DataFrames on 'Song ID' from df and 'id' from audio_features_df
merged_df = pd.merge(df, audio_features_df, left_on='Song ID', right_on='id', how='left')


# Display the DataFrame
print(merged_df)

# Optional: Save DataFrame to a CSV file
merged_df.to_csv('artist_tracks.csv', index=False)
