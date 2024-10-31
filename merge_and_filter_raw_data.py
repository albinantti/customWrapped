import os
import json
import pandas as pd

def union_json_files(directory):
    """
    Union multiple JSON files from a directory into a single dataframe.
    
    Parameters:
    - directory: Path to the directory containing the JSON files
    
    Returns:
    - DataFrame containing unioned data
    """
    # List files in the directory that start with "Streaming_" and end with ".json"
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) 
                  if file.startswith("Streaming_History_Audio") and file.endswith(".json")]
    
    # Initialize an empty list to store dataframes
    dfs = []
    
    # Read the structure of the first file to set as a reference
    with open(file_paths[0], "r") as file:
        sample_data = json.load(file)
    sample_df = pd.DataFrame(sample_data)
    
    # Iterate over each file path
    for path in file_paths:
        with open(path, "r") as file:
            data = json.load(file)
        
        # Convert the JSON data into a dataframe
        df = pd.DataFrame(data)
        
        # Check if the structure of this dataframe matches the sample dataframe
        if set(df.columns) != set(sample_df.columns):
            raise ValueError(f"The structure of file {path} is not the same as the sample.")
        
        # Remove rows with no episode_name or master_metadata_track_name
        df = df.dropna(subset=['episode_name', 'master_metadata_track_name'], how='all') 

        # Replace spotify_uri with only identifier part
        df['spotify_track_uri'] = df['spotify_track_uri'].str.split(':').str[-1]
        df['spotify_episode_uri'] = df['spotify_episode_uri'].str.split(':').str[-1]

        # Remove unwanted columns
        df = df.drop(columns=['username',
                'conn_country',
                'ip_addr_decrypted',
                'user_agent_decrypted',
                'reason_start',
                'reason_end',
                'skipped',
                'offline_timestamp',
                'incognito_mode'], axis=1)

        # Remove rows with less than 20 000 ms played
        df = df[df['ms_played'] >= 20000]

        # Rename columns
        df.rename(columns={
            'master_metadata_track_name' : 'track_name',
            'master_metadata_album_artist_name': 'artist',
            'master_metadata_album_album_name': 'album',
            'episode_show_name':'podcast'
        }, inplace=True)

        # Add flag if it is a podcast episode
        df['isPodcast'] = df['episode_name'].notna()

        # Append the dataframe to the list
        dfs.append(df)
    
    # Concatenate all the dataframes together
    result_df = pd.concat(dfs, ignore_index=True)
    result_df = result_df.sort_values(by='ts', inplace=False, ascending=True)
    result_df = result_df.reset_index(drop=True)

    return result_df

# Directory containing the JSON files
directory = r"input"

# Union the files
unioned_df = union_json_files(directory)
unioned_df.to_csv("output/full_streaming_history.csv")

print("Successfully merged streaming history and placed in output folder.")