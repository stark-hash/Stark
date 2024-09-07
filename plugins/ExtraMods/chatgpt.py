import requests
from pyrogram import Client, filters

# API details
AI_URL = "https://chatgpt-api8.p.rapidapi.com/"
AI_HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",
    "x-rapidapi-host": "chatgpt-api8.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Blacklisted words
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

# Function to check for blacklisted words
def contains_vulgar_words(text):
    for word in vulgar_words:
        if word in text.lower():
            return True
    return False

# New command for AI Assistant with blacklist filtering
@Client.on_message(filters.command("ai"))
async def chatgpt(bot, message):
    try:
        # Extract the query from the user's message
        if len(message.text.split()) > 1:
            query = message.text.split(None, 1)[1]
        else:
            await message.reply_text("❌ Please provide a message for the ChatGPT AI.")
            return

        # Check if the message contains any vulgar words
        if contains_vulgar_words(query):
            await message.reply_text("🚫 Your message contains inappropriate language. Please refrain from using vulgar words.")
            return

        # Payload structure to send to the API
        payload = [
            {
                "content": "You are an AI assistant based on ChatGPT 3.5.",
                "role": "system"
            },
            {
                "content": query,
                "role": "user"
            }
        ]

        # Sending request to the API
        response = requests.post(AI_URL, json=payload, headers=AI_HEADERS)
        data = response.json()

        # Extracting the AI-generated response
        ai_response = data.get("text", "Sorry, I couldn't process your request.")

        # Sending the AI response back to the user
        await message.reply_text(text=f"🤖 {ai_response}", quote=True)

    except Exception as e:
        await message.reply_text(text="❌ <b>Error processing your request</b>", quote=True)
