from pyrogram.types import User, Message
from pyrogram.client import Client
from pyrogram import filters
from config import querty_id, me_id
from globals import app

async def ids_command_filter_func(fliter, user: User, message: Message):
    if message.from_user.id != querty_id:
        return False
    if not message.text.startswith("/ids"):
        return False
    return True

ids_command_filter: filters.Filter = filters.create(ids_command_filter_func)

async def ids_command_handler(client: Client, message: Message):
    text = "1) 6063070403 Denys\n\
            2) 5869977774 Valerii"
    await message.reply_text(text)
