from pyrogram import Client, filters
import requests, asyncio

API = "https://chatgpt.apinepdev.workers.dev/?question={}"
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

@Client.on_message(filters.command("ai"))
async def ask_chatgpt(bot, message):
    query = message.text.split(None, 1)[1]

    # Check for vulgar words
    if any(word in query.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>Please refrain from asking questions with inappropriate content.</b>",
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
        answer = chatgpt_info(query)
        
        await message.reply_text(
            text=answer,
            quote=True
        )

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching response from ChatGPT</b>", quote=True)

def chatgpt_info(question):
    response = requests.get(API.format(question))
    info = response.json()

    # Extract the answer part from the JSON response
    answer = info['answer']

    return answer
