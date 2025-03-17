from pyrogram.client import Client
from pyrogram.types import User, Message 
from pyrogram import filters
import PIL
from modules.qrcode import image_to_binary, generate_qr_code

async def qrcode_filter_func(fliter, user: User, message: Message):
    return message.text.startswith("/qr ")
qrcode_command_filter: filters.Filter = filters.create(qrcode_filter_func)

async def qrcode_handler(client: Client, message: Message):
    if not message.text.strip():
        await message.reply_text("You must provide a text to encode.\nExample: /qr google.com")

    text_to_qr = message.text.removeprefix("/qr ")
    try:
        img: PIL.Image.Image = generate_qr_code(text_to_qr) 
        await client.send_photo(message.chat.id, image_to_binary(img))
    except:
        await message.reply_text("The error is occured!")
 
