import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ff21f86c4414494087581a5af4d7c4a6"
CLIENT_SECRET = "4016f0b4fd9d42db93bf392ba6905e83"

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
#scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))




year_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year_to_travel}/"
ALL_TITLES = []

response = requests.get(URL).text
soup = BeautifulSoup(response, 'html.parser')

all_blocks = soup.findAll(name='div', class_='o-chart-results-list-row-container')
for block in all_blocks:
    title = block.find('h3', id="title-of-a-story").getText().strip("\t\n")
    ALL_TITLES.append(title)

print(ALL_TITLES)