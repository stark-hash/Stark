from pyrogram import Client, filters
import requests

# Vulgar words list (same as before)
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

# RapidAPI credentials
RAPIDAPI_URL = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
RAPIDAPI_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
RAPIDAPI_HOST = "chatgpt-42.p.rapidapi.com"

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
        answer = chatgpt_info(query)
        
        await message.reply_text(
            text=answer,
            quote=True
        )

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching response from ChatGPT</b>", quote=True)

def chatgpt_info(question):
    # Define the payload for the API request
    payload = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
    response_data = response.json()

    # Extract the answer from the JSON response
    answer = response_data.get('result', 'Sorry, no response was returned.')

    return answer
