# This simple Python Script is a demo for Web Scrapping 
# This script retrives the Profile Photo of GitHub users

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub Username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)