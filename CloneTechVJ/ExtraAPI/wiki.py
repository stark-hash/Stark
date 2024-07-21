from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles={}&rvprop=content&format=json"

@Client.on_message(filters.command("wiki"))
async def get_wiki_info(bot, message):
    try:
        query = message.text.split(None, 1)[1]

        wiki_info_parts, reply_markup = fetch_wiki_info(query)

        for part in wiki_info_parts:
            await message.reply_text(
                text=part,
                quote=True,
                reply_markup=reply_markup if part == wiki_info_parts[-1] else None
            )

    except IndexError:
        await message.reply_text(
            text="❌ <b>Please provide a topic after the /wiki command.</b>",
            quote=True
        )

    except Exception as e:
        await message.reply_text(text=str(e), quote=True)

def fetch_wiki_info(query):
    response = requests.get(WIKIPEDIA_API.format(query))
    data = response.json()

    page = next(iter(data['query']['pages'].values()))
    title = page['title']
    content = page['revisions'][0]['*']

    response_text = f"--Wikipedia Info--\n\n📄 <b>Title:</b> {title}\n📄 <b>Content:</b> {content}"

    # Split the response text into chunks
    max_length = 4096
    wiki_info_parts = [response_text[i:i+max_length] for i in range(0, len(response_text), max_length)]

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("​🇸​​🇹​​🇦​​🇷​​🇰​ ​🇧​​🇴​​🇹​ ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​​🇸​", url='t.me/StarkBotUpdates')]
    ])

    return wiki_info_parts, reply_markup
