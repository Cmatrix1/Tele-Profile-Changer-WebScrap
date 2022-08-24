import os
import random

from time import sleep

import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pyrogram import Client


class ProfileChanger:
    categories = ["lancer", "benz", "bmw", "love", "peaky", "shellby", "ford", "programmer", "python", "jdm", "cat",
                  "dog", "iran", "car", "mazda"]
    space_time = 30  # To second

    def __init__(self, api_id: int, api_hash: str):
        self.app = Client("Cmatrix1", api_id, api_hash)

    def get_source(self, url):
        req = requests.get(url).content
        soup = BeautifulSoup(req, 'html.parser')
        return soup

    def extract_urls2(self, word):
        soup = self.get_source("https://www.peakpx.com/en/search?q=" + word)
        find = soup.find_all("figure")
        finds = list(map(lambda i: i.a["href"], find))
        return finds

    def get_image(self, url):
        soup = self.get_source(url)
        find = soup.find("figure").img["src"]
        return find

    def download_img(self, url):
        content = requests.get(url).content
        name = url.split("/")[-1]
        if name in os.listdir():
            return name
        file = open(name, "wb").write(content)
        return name

    def change_profile(self, name):
        with self.app:
            # photos = list(app.get_chat_photos("me")) 
            # app.delete_profile_photos([p.file_id for p in photos[1:]]) # Delete Profile Photos
            self.app.set_profile_photo(photo=name)
            # remove(name) # Delete Downloded Photo

    def main(self):
        while True:
            sleep(5)
            urls = self.extract_urls2(random.choice(self.categories))
            url = self.get_image(random.choice(urls))
            name = self.download_img(url)
            self.change_profile(name)


def main():
    load_dotenv()
    bot = ProfileChanger(int(os.getenv('APIID')), os.getenv('APIHASH'))
    bot.main()


if __name__ == '__main__':
    main()
