Telegram Profile Changer
=============================

This script is for changing your Telegram profile at a specified time. The script gets some profile photos based on the
words you provide.

![Untitled](https://user-images.githubusercontent.com/74909796/177029185-82163201-8ad8-4ec2-9f45-ec1dd5112427.png)

Installation
------------

Clone the repository:
```
git clone https://github.com/MPCodeWriter21/Telegram-Profile-Changer
```

Install the required libraries:

```
pip install -r requirement.txt
```

Add your api_hash and api_id into the `.env` file:

```dotenv
APIID=api-id
APIHASH=api-hash
```

Usage
-----

```
python ProfileChanger.py
```

You can also choose the category of images and the time to change the profile picture

```python
class ProfChanger():
    categorys = ["lancer", "benz", "bmw", "programmer", "python", "cat", "dog", "iran"]
    space_time = 30  # To second
```

# Future

### I need your support to add these features. Please support me by giving stars and sharing this source with your friends.

- Advanced admin panel
- The ability to write time on the photo
- The ability to change the account name at the same time as the photo
- The ability to change the account bio at the same time as the photo
