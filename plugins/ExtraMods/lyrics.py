from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

API = "https://lyrist.vercel.app/api/{}"

@Client.on_message(filters.command("lyrics"))
async def lyrics_sendu(bot, message):
    query = message.text.split(None, 1)[1]
    try:
        response_text, reply_markup, image_url, lyrics_text = lyrics_info(query)
        
        # Send the image with the song title and artist as the caption
        await message.reply_photo(
            photo=image_url,
            caption=response_text,
            quote=True,
            reply_markup=reply_markup
        )

        # Send the lyrics in a separate message
        await message.reply_text(text=lyrics_text, quote=True)

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching Lyrics</b>", quote=True)

def lyrics_info(lyricsquery):
    r = requests.get(API.format(lyricsquery))
    info = r.json()

    # Extract data from the JSON response
    image_url = info['image']
    lyrics_text = info['lyrics']
    title = info['title']
    artist = info['artist']

    response_text = f"🎶 Successfully Extracted Lyrics Of {title} by {artist} 🎶"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("​🇸​​🇹​​🇦​​🇷​​🇰​ ​🇧​​🇴​​🇹​ ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​​🇸​", url='t.me/StarkBotUpdates')]
    ])

    return response_text, reply_markup, image_url, lyrics_text
