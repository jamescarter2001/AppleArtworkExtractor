import requests
import json
import webbrowser
import pycountry

import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-u', '--url', nargs="?",
                    help="Apple Music URL", required=True)
parser.add_argument('-r', '--region', nargs="?",
                    help="Region Code (US, GB, JP etc)", default="JP")
args = parser.parse_args()

region = pycountry.countries.get(alpha_2=args.region)
language = "en_us"  # ja_jp

print(colored(f"Region: {region.name}", 'yellow'))

link = args.url.split('/')[-1].split('?')[0]

itunes_endpoint = f'https://itunes.apple.com/lookup?id={link}&country={region.alpha_2}&lang={language}'

response = requests.get(itunes_endpoint)
if response.status_code == 200:
    print(f'Name: {response.json()["results"][0]["collectionName"]}')
    print(f'Artist: {response.json()["results"][0]["artistName"]}')
    print(
        f'Copyright: {response.json()["results"][0]["copyright"]}')
    artwork_link = response.json()["results"][0]["artworkUrl100"]
    artwork_link = artwork_link.replace("100x100bb.jpg", "3000x3000bb.jpg")
    print(f'\nArtwork Link: {artwork_link}')
    webbrowser.open(artwork_link, new=2)
elif response.status_code == 404:
    print("Track not found.")
else:
    print(f"Error while connecting to iTunes. ({response.status_code})")
