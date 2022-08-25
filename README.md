Telegram Profile Changer
========================

This script is for changing your Telegram profiles at a specific time. The script gets some profile photos based on the
words you provide.

![Untitled](https://user-images.githubusercontent.com/74909796/177029185-82163201-8ad8-4ec2-9f45-ec1dd5112427.png)

Installation
------------

Clone the repository:

```shell
git clone https://github.com/MPCodeWriter21/Telegram-Profile-Changer
```

Install the required libraries:

```shell
pip install -r requirements.txt
```

Add your api_hash and api_id into the `.env` file:

```dotenv
APIID=api-id
APIHASH=api-hash
```

Usage
-----

```
usage: ProfileChanger.py [-h] [-id API_ID] [-hash API_HASH] [-t TIME_TO_SLEEP] [-v] [-q]
                         categories [categories ...]

positional arguments:
  categories        Categories for profile photos.

options:
  -h, --help
                        show this help message and exit
  -id API_ID, --api-id API_ID
                        Your telegram API-ID
  -hash API_HASH, --api-hash API_HASH
                        Your telegram API-HASH
  -t TIME_TO_SLEEP, --time-to-sleep TIME_TO_SLEEP
                        Change the profile every X seconds(Default: 1800)
  -v, --verbose
  -q, --quiet

```

### Example

```shell
# Changes the profile every 30 seconds and searches for images about one of the words: 
#   Python, Programming, Code, Computers
python ProfileChanger.py -t 30 Python Programming Code Computers
```

Future
------

### We need your support to add these features. Please support us by giving stars and sharing this source with your friends.

- [ ] Advanced admin panel
- [ ] The ability to write time on the photo
- [ ] The ability to change the account name at the same time as the photo
- [ ] The ability to change the account bio at the same time as the photo
