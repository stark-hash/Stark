from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

API = "https://aiimage.hellonepdevs.workers.dev/?prompt={}&state=url"
vulgar_words = [
    "nudegirl", "nude", "sex", "porn", "vulgarwords", "ass", "bitch", "boobs", "breast", "cock", 
    "cunt", "dick", "fuck", "motherfucker", "pussy", "slut", "whore", "damn", "bastard", 
    "shit", "bollocks", "bugger", "bloody", "blowjob", "dildo", "fag", "faggot", "handjob", 
    "jizz", "knob", "muff", "nigger", "penis", "prick", "snatch", "tit", "twat", "vagina", 
    "wank", "wanker", "cum", "jugs", "spunk", "skank", "slutty", "tits", "milf", "hentai",
    "gangbang", "hardcore", "incest", "lesbian", "masturbate", "orgasm", "rape", "screw", 
    "stripper", "suck", "threesome", "xxx", "anus", "arse", "arsehole", "bollock", "boner",
    "clit", "clitoris", "douche", "dyke", "fellatio", "felch", "gonads", "horny", "jizzum", 
    "knobend", "knobhead", "minge", "nutsack", "pecker", "piss", "scrote", "scrotum", "semen",
    "shag", "shite", "shitface", "shithead", "shlong", "spunk", "titty", "turd", "willy",
    "chode", "rimjob", "foreskin", "herpes", "titfuck", "tranny", "shemale"
]

@Client.on_message(filters.command("aiimage"))
async def aiimage_sendu(bot, message):
    query = message.text.split(None, 1)[1]

    # Check for vulgar words
    if any(word in query.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>You cannot generate images with vulgar prompts.</b>",
            quote=True
        )
        return

    try:
        response_text, reply_markup, image_url = aiimage_info(query)
        
        # Send the AI-generated image with a caption
        await message.reply_photo(
            photo=image_url,
            caption=response_text,
            quote=True,
            reply_markup=reply_markup
        )

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching AI image</b>", quote=True)

def aiimage_info(promptquery):
    response = requests.get(API.format(promptquery))
    info = response.json()

    # Extract data from the JSON response
    image_url = info['image_url']

    response_text = "Your AI-generated image has been successfully created."

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("FDBotz", url='t.me/FDBotz')]
    ])

    return response_text, reply_markup, image_url
