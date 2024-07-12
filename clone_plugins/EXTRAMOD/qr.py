from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

API = "https://dynamicqrcode.nepcoderdevs.workers.dev/?message={}"

@Client.on_message(filters.command("qr"))
async def qr_sendu(bot, message):
    query = message.text.split(None, 1)[1]
    try:
        response_text, reply_markup, image_url = qr_info(query)
        
        # Send the QR code image with a caption
        await message.reply_photo(
            photo=image_url,
            caption=response_text,
            quote=True,
            reply_markup=reply_markup
        )

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching QR</b>", quote=True)

def qr_info(qrcodequery):
    r = requests.get(API.format(qrcodequery))
    info = r.json()

    # Extract data from the JSON response
    image_url = info['qrImageUrl']

    response_text = "Your QR code has been successfully generated. | By @FDBotz"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("​🇸​​🇹​​🇦​​🇷​​🇰​ ​🇧​​🇴​​🇹​ ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​​🇸​", url='t.me/StarkBotUpdates')]
    ])

    return response_text, reply_markup, image_url
