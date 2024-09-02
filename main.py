import PIL
from pyrogram import filters
from config import api_id, api_hash
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import User, Message, Update 
from modules.qrcode import generate_qr_code, image_to_binary
import asyncio
from modules.qrcode_handler import qrcode_handler, qrcode_command_filter
from modules.forward_chosen import chosen_chats_filter, chosen_chats_handler


app = Client("my_account", api_id, api_hash)

    
app.add_handler(MessageHandler(qrcode_handler, (filters.text & qrcode_command_filter)))
app.add_handler(MessageHandler(chosen_chats_handler, (chosen_chats_filter)))

if __name__ == "__main__":
    app.run()
