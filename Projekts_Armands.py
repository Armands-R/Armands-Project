import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

dziesmas = []

klienta_id= "5a14efe06cbb48038f89eabf30a4a60a"
klienta_secret = "426791bc88854b2e8a83fc6efbbcdc4e"

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(klienta_id, klienta_secret))


results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()













