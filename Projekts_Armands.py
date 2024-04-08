import json
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sqlite3
connection = sqlite3.connect("main.db")

dziesmas = []

klienta_id= "5a14efe06cbb48038f89eabf30a4a60a"
klienta_secret = "426791bc88854b2e8a83fc6efbbcdc4e"

klienta2_id = "EIpcEal2Kdlck9COc_CzfCzalsdu_xzwxqmSTvKQy6AuJTVdyXwB5zBBKxPo3pBH"
klienta2_secret = "B2AkQktsf5qq0rP4WMwLX7xcN8kbMql4pq35i9se7zGDPG-zU_AEpfM1tBwq9rNsQ3v4xHIPgeuCV2XskeA-sQ"
klienta_access_token = "BIH3Ig-66qBCiX8qFFIrm81B7A1p5aKOPydarK_0YNRZO25kauVOZAWpTYRhKCop"

# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(klienta_id, klienta_secret))

a= input("Ieraksti izpildītāju: ")

# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()



# spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = a

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])


# rezultats = spotify.artist_top_tracks(results)

# for track in resultats['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()












