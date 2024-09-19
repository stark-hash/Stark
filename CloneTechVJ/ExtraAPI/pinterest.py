from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests, asyncio

API = "https://pinteresimage.nepcoderdevs.workers.dev/?query={}&limit=12"
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

@Client.on_message(filters.command("pinterest"))
async def pinterest_sendu(bot, message):
    query = message.text.split(None, 1)[1]

    # Check for vulgar words
    if any(word in query.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>You cannot search for images with vulgar prompts.</b>",
            quote=True
        )
        return

    try:
                # Send a "Processing..." message
        processing_message = await message.reply_text(text="⏳ `Processing...`", quote=True)
        
        # Wait for 5 seconds
        await asyncio.sleep(10)
        
        # Delete the "Processing..." message
        await processing_message.delete()
        
        results = pinterest_info(query)
        
        if results:
            for result in results:
                image_url = result['imageUrl']
                title = result['title']
                
                await message.reply_photo(
                    photo=image_url,
                    caption=title,
                    quote=True
                )
        else:
            await message.reply_text(text="❌ <b>No images found for your query.</b>", quote=True)

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching Pinterest Images</b>", quote=True)

def pinterest_info(pinterestpromptquery):
    response = requests.get(API.format(pinterestpromptquery))
    info = response.json()

    return info.get('results', [])

