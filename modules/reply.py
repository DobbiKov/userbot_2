from pyrogram.types import User, Message
from pyrogram.client import Client
from pyrogram import filters
from config import querty_id, me_id
from globals import app

async def reply_filter_func(fliter, user: User, message: Message):
    if message.from_user.id != querty_id:
        return False
    if not message.text.startswith("/send "):
        return False
    return True

reply_filter: filters.Filter = filters.create(reply_filter_func)

async def reply_handler(client: Client, message: Message):
    text = message.text
    splitted = text.split(" ")
    chat_id = 0
    try:
        chat_id = int(splitted[1])
    except:
        return await message.reply_text("You must enter chat_id")

    text_to_send = ""
    for s in splitted[2::]:
        text_to_send += s + " "
    await app.send_message(chat_id, text_to_send) 
