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
from modules.thanks_handler import thanks_filter, thanks_handler
from modules.voice_to_text import two_text_filter, two_text_handler
from modules.weather import weather_command_filter, weather_command_handler, send_weather
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.calendarinterval import CalendarIntervalTrigger
from datetime import datetime, timedelta
    
app.add_handler(MessageHandler(reply_handler, (reply_filter)))
app.add_handler(MessageHandler(ids_command_handler, (ids_command_filter)))
app.add_handler(MessageHandler(qrcode_handler, (filters.text & qrcode_command_filter)))
app.add_handler(MessageHandler(chosen_chats_handler, (chosen_chats_filter)))
app.add_handler(MessageHandler(two_text_handler, (two_text_filter)))
app.add_handler(MessageHandler(thanks_handler, (thanks_filter)))
app.add_handler(MessageHandler(weather_command_handler, (weather_command_filter)))

if __name__ == "__main__":
    scheduler = AsyncIOScheduler()
    today = datetime.today()
    today.replace(hour=8, minute=0)
    tomorrow = today + timedelta(days=1)

    scheduler.add_job(send_weather, CalendarIntervalTrigger(days=1, start_date=tomorrow))

    scheduler.start()
    app.run()
