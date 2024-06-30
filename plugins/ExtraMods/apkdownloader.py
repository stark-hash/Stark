from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

API = "https://apkdownloader.hellonepdevs.workers.dev/?query={}"

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

@Client.on_message(filters.command("apk"))
async def apk_download(bot, message):
    query = message.text.split(None, 1)[1]

    # Check for vulgar words
    if any(word in query.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>You cannot search for APKs with vulgar content.</b>",
            quote=True
        )
        return

    try:
        # Fetch APK details from the API
        results = apk_info(query)
        
        # Send each result as a separate message
        for result in results:
            response_text, reply_markup, image_url = result
            await message.reply_photo(
                photo=image_url,
                caption=response_text,
                quote=True,
                reply_markup=reply_markup
            )
        
    except Exception as e:
        await message.reply_text(text=str(e), quote=True)

def apk_info(apkquery):
    r = requests.get(API.format(apkquery))
    infos = r.json()  # Get the list of results

    results = []
    for info in infos:
        # Extract data from the JSON response
        name = info["name"]
        package = info["package"]
        filesize = info["filesize"]
        rank = info["rank"]
        image_url = info["image"]
        developer = info["developer"]
        download_url = info["path"]

        response_text = f"""--APK Download--

📱 <b>Name:</b> {name}
👤 <b>Developer:</b> {developer}
📦 <b>Package:</b> {package}
💾 <b>File Size:</b> {filesize} bytes
⭐ <b>Rank:</b> {rank}

Made by @FDBotz ❤️"""

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 Download APK", url=download_url)],
            [InlineKeyboardButton("FDBotz", url='t.me/FDBotz')]
        ])

        results.append((response_text, reply_markup, image_url))

    return results
