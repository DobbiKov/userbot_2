from pyrogram.client import Client
from pyrogram.types import User, Message
from pyrogram import filters
from config import querty_id, me_id

chosen_chats = [
        5869977774,
        5042508480,
        6063070403
]

async def chosen_chats_func(fliter, user: User, message: Message):
    return message.chat.id in chosen_chats and message.from_user.id != me_id 
chosen_chats_filter: filters.Filter = filters.create(chosen_chats_func)

async def chosen_chats_handler(client: Client, message: Message):
    forwarded_message = await message.forward(querty_id)
    if type(forwarded_message) != Message:
        return
    await forwarded_message.reply_text(f"From Chat: {message.chat.first_name} {message.chat.last_name or '-'}")
    



