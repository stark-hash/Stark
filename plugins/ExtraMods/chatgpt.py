import requests
import logging
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

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# New command for AI Assistant with blacklist filtering
@Client.on_message(filters.command("ai"))
async def chatgpt(bot, message):
    try:
        # Extract the query from the user's message
        if len(message.text.split()) > 1:
            query = message.text.split(None, 1)[1]
            logging.debug(f"Received query: {query}")
            print(f"Received query: {query}")  # For testing
        else:
            logging.warning("No query provided by user.")
            await message.reply_text("❌ Please provide a message for the ChatGPT AI.")
            return

        # Check if the message contains any vulgar words
        if contains_vulgar_words(query):
            logging.warning(f"Vulgar words detected in query: {query}")
            print(f"Vulgar words detected: {query}")  # For testing
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
        
        logging.debug(f"Sending request to API: {payload}")
        print(f"Sending request: {payload}")  # For testing

        # Sending request to the API
        response = requests.post(AI_URL, json=payload, headers=AI_HEADERS)
        logging.debug(f"API response status code: {response.status_code}")
        print(f"API status code: {response.status_code}")  # For testing
        data = response.json()
        logging.debug(f"API response data: {data}")
        print(f"API response: {data}")  # For testing

        # Extracting the AI-generated response
        ai_response = data.get("text", "Sorry, I couldn't process your request.")
        logging.debug(f"AI response: {ai_response}")
        print(f"AI response: {ai_response}")  # For testing

        # Sending the AI response back to the user
        await message.reply_text(text=f"🤖 {ai_response}", quote=True)

    except Exception as e:
        logging.error(f"Error occurred: {e}", exc_info=True)
        print(f"Error occurred: {e}")  # For testing
        await message.reply_text(text="❌ <b>Error processing your request</b>", quote=True)
