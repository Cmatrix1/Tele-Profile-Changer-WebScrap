from bs4 import BeautifulSoup
from requests import get
from random import choice
from os import listdir, remove
from pyrogram import Client, filters
from time import sleep


class ProfChanger():
    categorys = ["lancer", "benz", "bmw", "love", "peaky", "shellby", "ford", "programmer","python", "jdm", "cat", "dog", "iran", "car", "mazda"]
    space_time = 30 # To second

    def __init__(self):
        self.app = Client("Cmatrix1", 1111111, "Your accont hash")

    def get_source(self, url):
        req = get(url).content
        soup = BeautifulSoup(req)
        return soup

    def extract_urls2(self, word):
        soup = self.get_source("https://www.peakpx.com/en/search?q="+word)
        find = soup.find_all("figure")
        finds = list(map(lambda i:i.a["href"], find))
        return finds

    def get_image(self, url):
        soup = get_source(url)
        find = soup.find("figure").img["src"]
        return find

    def download_img(url):
        content = get(url).content
        name = url.split("/")[-1]
        if name in listdir():
            return name
        file = open(name, "wb").write(content)
        return name

    def change_profile(self):
        with app:
            # photos = list(app.get_chat_photos("me")) 
            # app.delete_profile_photos([p.file_id for p in photos[1:]]) # Delete Profile Photos
            app.set_profile_photo(photo=name)
            # remove(name) # Delete Downloded Photo
    
    def main(self):
        while True:
            sleep(30)
            urls = self.extract_urls2(choice(words))
            url = self.get_image(choice(urls))
            name = self.download_img(url)
            self.change_profile(name)

bot = ProfChanger()
bot.main()