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
from modules.reply import reply_filter, reply_handler
from modules.ids_command import ids_command_filter, ids_command_handler

from globals import app
from modules.voice_to_text import two_text_filter, two_text_handler
    
app.add_handler(MessageHandler(reply_handler, (reply_filter)))
app.add_handler(MessageHandler(ids_command_handler, (ids_command_filter)))
app.add_handler(MessageHandler(qrcode_handler, (filters.text & qrcode_command_filter)))
app.add_handler(MessageHandler(chosen_chats_handler, (chosen_chats_filter)))
app.add_handler(MessageHandler(two_text_handler, (two_text_filter)))

if __name__ == "__main__":
    app.run()
