from pyrogram import Client, filters
import random

# Replace this with your command handler prefix if needed
COMMAND_HAND_LER = "/"

# List of Telegraph links for car wallpapers
CAR_WALLPAPERS = [
    "https://telegra.ph/file/0306dc72a735d1b4dac90.jpg",
    "https://telegra.ph/file/9cc3fda763a4f95d5b2d6.jpg",
    "https://telegra.ph/file/3cc4ec1ecbb6a4f0f7fd9.jpg",
    "https://telegra.ph/file/f92c48fc1385560e68d1e.jpg",
    "https://telegra.ph/file/854ac65fdddbe2c773164.jpg",
    "https://telegra.ph/file/f11193eaf690699fc44fd.jpg",
    "https://telegra.ph/file/2df143e5207d387600170.jpg",
    "https://telegra.ph/file/f63c7d6936ed14ce9bda3.jpg",
    "https://telegra.ph/file/fb22ddff47844bc269756.jpg",
    "https://telegra.ph/file/607d61319ed11355a1c87.jpg",
    "https://telegra.ph/file/db40881c8f24fae575647.jpg",
    "https://telegra.ph/file/e9e1a92d433f5d12d2f0e.jpg",
    "https://telegra.ph/file/09c383ce641ac4b1dc89a.jpg",
    "https://telegra.ph/file/cfcb69aeed5384ffd914d.jpg",
    "https://telegra.ph/file/21f349103cbd9c91dbfe8.jpg",
    "https://telegra.ph/file/98ed2d5b40c7a40cd7024.jpg",
    "https://telegra.ph/file/c12fe775d932ce01d974a.jpg",
    "https://telegra.ph/file/d8a098ca367a69d641c1c.jpg",
    "https://telegra.ph/file/c280f60d00368c0bdee51.jpg"
]


@Client.on_message(
    filters.command(["cars"])
)
async def send_car_wallpaper(client, message):
    """ /cars to get a random car wallpaper """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id

    # Select a random car wallpaper link
    car_wallpaper = random.choice(CAR_WALLPAPERS)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=car_wallpaper,
        caption="Here's a random car wallpaper for you!",
        reply_to_message_id=rep_mesg_id
    )
