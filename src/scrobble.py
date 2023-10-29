import pylast
import json
import os
import sys
import time
from dotenv import load_dotenv
from colorama import init, Fore
init(autoreset = True)  

# Load
load_dotenv()
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'config.json')
with open(file_path, 'r') as json_file:
    config = json.load(json_file)  

# Global 
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
username = os.getenv('LASTFM_USERNAME')
password = os.getenv('LASTFM_PASSWORD')
artist = config['ARTIST']
track = config['TRACK']
album = config['ALBUM']
limit = config['LIMIT']
interval = config['INTERVAL']

# Login
try:
    network = pylast.LastFMNetwork(
    api_key=api_key,
    api_secret=api_secret,
    username=username,
    password_hash=pylast.md5(password)
    )
except pylast.NetworkError as e:
    print(Fore.RED + f'Please check your internet connection\n{e}')
    sys.exit()
except pylast.WSError as e:
    print(Fore.RED + f'Please check your creditentials at .env file\n{e}')
    sys.exit()

# Scrobble
def scrobble():
    try:
        scrobbles = 0
        while scrobbles < limit:
            network.scrobble(artist=artist, title=track, timestamp=int(time.time()), album=album)
            print(Fore.BLUE +  f'\rScrobbling {track} by {artist} {scrobbles+1}/{limit}', end='', flush=True)
            scrobbles+=1
            time.sleep(interval)
            
        print(Fore.GREEN + f"\nSuccessfully scrobbled {scrobbles} tracks.")
    except pylast.NetworkError as e:
        print(Fore.RED + f'Please check your internet connection\n{e}')