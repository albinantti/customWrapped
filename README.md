# Custom Wrapped

This code is taken from @monetenmangel's [Spotify Rewind](https://github.com/monetenmangel/Spotify-Rewind) and adapted to suit my preferences. It can currently parse the Spotify json exports and output them in a csv format, which is more than half of the functionality I want.

To try it out for yourself, request your full streaming history from [Spotify](https://www.spotify.com/se/account/privacy/).

1. Download the export zip and place the streaming history json files in the `input` folder.
2. Navigate to the repository directory and (optionally using a python virtual environment) install the required packages with `pip install -r requirements.txt`
3. Run the `merge_and_filter_raw_data.py` script using Python.
4. A parsed CSV will be created and placed in the `output` folder.

### Roadmap
I am in the progress of adding functionality to request song information from Spotify's API in order to get artists and subsequently requesting Artist information from Spotify's api in order to add genres to songs. Will be stored in an sqlite file to reduce amount of API requests needed.
