# Telegram UserBot

This repository provides a python script for telegram userbot that I personally
use for my account.

## Features
- Automatically forward all messages from chosen contacts
- Convert voice messages to text using just one command
- Get weather and clothes recommendation
- Scheduled weather and clothes recommendation
- Automatically put an emoji on the messages containing "thanks" on four different languages
- Qrcode generation for any text

## Installation
1. `git clone https://github.com/DobbiKov/userbot_2`
2. `cd userbot_2`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip3 install -r requirements.txt`
6. set up `config.ini`
    ```ini
    [pyrogram]
    api_id = <your-tg-api-id>
    api_hash = <your-tg-api-hash>
    gemini_api = <your-gemini-api>

    [user]
    location = <your location>
    ```
7. `python3 main.py`
