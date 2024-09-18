from pyrogram import Client, filters
import requests
from io import BytesIO
from PIL import Image

API = "https://apis.xditya.me/write?text="
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

@Client.on_message(filters.command("write"))
async def write_text(bot, message):
    query = message.text.split(None, 1)[1]

    # Check for vulgar words
    if any(word in query.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>You cannot generate handwriting with vulgar content.</b>",
            quote=True
        )
        return

    try:
        # Get the handwriting image from the API
        response = requests.get(API + query)
        
        # Check if the response is successful
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            
            # Send the image
            with BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)
                await bot.send_photo(
                    chat_id=message.chat.id,
                    photo=image_binary,
                    caption="🖋️ Here is your handwritten text",
                    reply_to_message_id=message.id
                )
        else:
            await message.reply_text(text="❌ <b>Error generating handwriting. Please try again later.</b>", quote=True)
        
    except Exception as e:
        await message.reply_text(text=str(e), quote=True)
