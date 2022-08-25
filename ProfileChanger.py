import os
import random

from time import sleep
from typing import List, Sequence, Union

import log21
import requests

from pyrogram import Client
from bs4 import BeautifulSoup
from dotenv import load_dotenv

RED = log21.get_color('Red')
BLUE = log21.get_color('Blue')
GREEN = log21.get_color('Green')
CYAN = log21.get_color('Cyan')
LRED = log21.get_color('Light Red')
LBLUE = log21.get_color('Light Blue')
LGREEN = log21.get_color('Light Green')
LCYAN = log21.get_color('Light Cyan')
RESET = log21.get_color('RESET')


class ProfileChanger:
    time_to_sleep = 60 * 30  # in seconds

    def __init__(self, api_id: int, api_hash: str, categories: List[str], time_to_sleep: int = 1800,
                 clean: bool = False, level: Union[int, str] = 'INFO'):
        self.app = Client("session", api_id, api_hash)
        self.logger = log21.get_logger('ProfileChanger', level=level)
        if not categories:
            raise ValueError('You must specify categories.')
        if not isinstance(categories, Sequence):
            raise TypeError('categories must be sequence of strings.')
        if not isinstance(time_to_sleep, int):
            raise TypeError('time_to_sleep must be an integer.')
        if time_to_sleep < 1:
            raise ValueError('time_to_sleep can\'t be less than 1.')
        self.categories = list(set(categories))
        self.time_to_sleep = time_to_sleep
        self.clean = clean
        self.app.start()
        self.app.stop()

    def get_new_profile(self):
        # Find images with a random category
        category = random.choice(self.categories)
        self.logger.info(f'Searching for images related to {LCYAN}{category}{RESET}...')
        url = f"https://www.peakpx.com/en/search?q={category}&device=2"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        figures = soup.find_all("figure")
        urls = list(map(lambda i: i.a["href"], figures))

        # Checks if the script was able to find any images
        if not urls:
            return None

        self.logger.info(f'Found {LBLUE}{len(urls)}{RESET} images!')

        # Get the download url of a random image
        self.logger.debug('Choosing an image and finding the download URL...')
        response = requests.get(random.choice(urls))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_url = soup.find("figure").img["src"]
        self.logger.debug(f'Download URL: {BLUE}{image_url}{RESET}')

        # Download the image
        self.logger.debug('Downloading image...')
        content = requests.get(image_url).content
        name = image_url.split("/")[-1]
        if name in os.listdir():
            return name
        with open(name, "wb") as file:
            file.write(content)
        self.logger.debug('Downloaded the image!')
        self.logger.debug(f'Image Size: {LRED}{(os.stat(name).st_size / 1024):.2f}{RESET} KiBs')

        return name

    def change_profile(self, path: Union[str, os.PathLike]):
        self.logger.info('Setting the profile picture...')
        with self.app:
            # photos = list(app.get_chat_photos("me"))
            # app.delete_profile_photos([p.file_id for p in photos[1:]]) # Delete Profile Photos
            self.app.set_profile_photo(photo=path)
            if self.clean:
                os.remove(path)  # Delete Downloaded Photo
                self.logger.info('Removed downloaded image!')
        self.logger.info('Done!')

    def run(self):
        while True:
            try:
                profile_path = self.get_new_profile()
            except Exception as e:
                self.logger.error(f'Failed to get new profile: {RED}{e.__class__.__name__}: {e}{RESET}')
                continue

            # Checks if the script was able to find any images
            if not profile_path:
                self.logger.warning('No images found! Retrying...')
                continue

            try:
                # Set the Profile
                self.change_profile(profile_path)
            except Exception as e:
                self.logger.error(f'Failed to set the profile: {RED}{e.__class__.__name__}: {e}{RESET}')
                continue

            # Wait for some seconds
            self.logger.info(f'Waiting for {LGREEN}{self.time_to_sleep}{RESET} seconds...')
            sleep(self.time_to_sleep)


log21.console_reporter.ignore(KeyboardInterrupt)
log21.console_reporter.ignore(SystemExit)


@log21.console_reporter.reporter
def main():
    parser = log21.ColorizingArgumentParser()
    parser.add_argument('categories', action='store', nargs='+', help='Categories for profile photos.')
    parser.add_argument('-id', '--api-id', action='store', type=int, help='Your telegram API-ID')
    parser.add_argument('-hash', '--api-hash', action='store', help='Your telegram API-HASH')
    parser.add_argument('-t', '--time-to-sleep', action='store', type=int,
                        help='Change the profile every X seconds(Default: 1800)', default=1800)
    parser.add_argument('-c', '--clean', action='store_true',
                        help='Remove images from the storage after setting the profile.')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    load_dotenv()
    api_id = args.api_id
    api_hash = args.api_hash
    if not api_id:
        api_id = int(os.getenv('APIID'))
    if not api_hash:
        api_hash = os.getenv('APIHASH')

    if args.verbose and args.quiet:
        parser.error('You can not use --verbose and --quiet arguments together!')
    if args.verbose:
        level = 'DEBUG'
    elif args.quiet:
        level = 'ERROR'
    else:
        level = 'INFO'

    if not api_id:
        log21.error('API-ID is not specified! Please use `-id` argument or put your API-ID in `.env` file.')
    if not api_hash:
        log21.error('API-HASH is not specified! Please use `-hash` argument or put your API-HASH in `.env` file.')

    bot = ProfileChanger(api_id, api_hash, args.categories, args.time_to_sleep, args.clean, level)
    bot.run()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log21.error(f'KeyboardInterrupt{LRED}:{RESET} Exiting...')
