import requests
from bs4 import BeatifulSoup
import urllib

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeatifulSoup(response.content, 'html.parser')
        image_tacontainer = soup.find(id='comic')

if __name__ == '__main__':
    run()