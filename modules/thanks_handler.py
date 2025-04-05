from pyrogram.types import User, Message
from pyrogram.client import Client
from pyrogram import filters
from config import querty_id, me_id
from globals import app
from typing import Optional

def does_text_contains_thanks(mess: str) -> Optional[str]: 
    """
    Returns a string with language that "thanks" was written or None if "thanks" wasn't written at all
    """
    thanks = {
            "ua": ["дякую", "спасибі"],
            "ru": [ "спасибо", "благодарю", "спс", "sps", "spasibo" ],
            "en": [ "thank you", "thank", "thanks" ],
            "fr": [ "merci", "remercie" ]
    }
    for (lang, words) in thanks.items():
        for word in words:
            if word in mess:
                return lang
    return None

async def thanks_filter_func(fliter, user: User, message: Message):
    return does_text_contains_thanks(message.text.lower()) is not None

thanks_filter: filters.Filter = filters.create(thanks_filter_func)

async def thanks_handler(client: Client, message: Message):
    lang = does_text_contains_thanks(message.text.lower())
    if lang is None:
        return print("No language found")
    
    if message.chat.id != message.from_user.id:
        return
    await message.react("❤️")
