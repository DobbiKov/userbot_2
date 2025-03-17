import os
from google import genai
from pyrogram.types import User, Message
from pyrogram.client import Client
from pyrogram import filters
from config import querty_id, me_id
from globals import app
from config import gemini_api

async def two_text_filter_func(fliter, user: User, message: Message):
    return message.text.startswith("/2txt")

two_text_filter: filters.Filter = filters.create(two_text_filter_func)

async def two_text_handler(client: Client, message: Message):
    replied_to = message.reply_to_message
    if replied_to == None:
        return await message.reply("You must to reply to a message with a voice")
    contents_voice = replied_to.voice
    contents_video = replied_to.video
    if contents_voice == None and contents_video == None:
        return await message.reply("The message you're replying to doesn't contain any voice or video content!")
    file_id = -1
    if contents_voice != None:
        file_id = contents_voice.file_id
    else:
        file_id = contents_video.file_id

    mess = await message.reply("I'm starting to transcribe your audio!")
    path = await client.download_media(file_id, "./audio/")
    path = str(path)
    gemini_reply = transcribe_from_file(path)
    os.remove(path)
    await mess.edit_text(gemini_reply)

def transcribe_from_file(path: str) -> str:
#
    client = genai.Client(api_key=gemini_api)

    myfile = client.files.upload(file=path)

    response = client.models.generate_content(
      model='gemini-2.0-flash',
      contents=['Give me the complete transcript of the audio message (in the case if you understand that there\'s only one speaker). If there\'s more than one speaker, write the transcript in the format:\
              Speaker 1: ...\
              Speaker 2: ...\
              etc...\
                ', myfile]
    )

    return response.text or "error"
#
