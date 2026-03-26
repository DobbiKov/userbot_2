import os
from google import genai
from pyrogram.types import User, Message
from pyrogram.client import Client
from pyrogram import filters
from config import querty_id, me_id
from globals import app
from config import gemini_api, location

async def weather_command_filter_func(fliter, user: User, message: Message):
    return message.text.startswith("/weather")

weather_command_filter: filters.Filter = filters.create(weather_command_filter_func)

async def weather_command_handler(client: Client, message: Message):
    mess = await message.reply("Let's get the weather for today")
    weather = get_today_weather(location)
    await mess.edit_text(f"Got the weather, let's analyze it and decide what to wear\n\n {weather}")
    what_to_wear = get_what_to_wear_today(weather)
    await mess.edit_text(what_to_wear)

async def send_weather():
    mess = await app.send_message("me", "Let's get the weather for today!")
    weather = get_today_weather(location)
    await mess.edit_text(f"Got the weather, let's analyze it and decide what to wear\n\n {weather}")
    what_to_wear = get_what_to_wear_today(weather)
    await mess.edit_text(what_to_wear)

def get_what_to_wear_today(weather: str) -> str:
    client = genai.Client(api_key=gemini_api)

    response = client.models.generate_content(
      model='gemini-2.5-flash',
      contents=[f'You are a personal assistant that is very professional in \
                weather and clothes that needs to feel as comfortable as \
                possible during the day. You are given the weather for today, \
                your goal is to analyze the weather for the whole day and \
                answer to the user what it should wear today, prefer short answer, also provide a short one sentence summary of the weather for the day: \
                underwear if it is too cold, shorts vs pants, tshirt is sufficient/shirt/jacket if it is that cold: \n{weather}']
    )

    return response.text or "error"

def get_today_weather(location) -> str:
    client = genai.Client(api_key=gemini_api)
    response = client.models.generate_content(
      model='gemini-2.5-flash',
      contents=[f"Get the weather for today in {location}. Give the weather for the next hours: 7:00, 10:00, 12:00, 15:00, 18:00, 21:00. Provide the temperature in celsius but also if it will rain, how strong the wind is." ],
      config=genai.types.GenerateContentConfig(
        tools=[genai.types.Tool(google_search=genai.types.GoogleSearch())]
    )
    )
    return response.text or "error"
#
#
