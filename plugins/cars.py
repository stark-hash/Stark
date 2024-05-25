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
    "https://telegra.ph/file/89529c8f0ea790e119d30.jpg",
    "https://telegra.ph/file/bda06f0b2a646240ffa94.jpg",
    "https://telegra.ph/file/c273d21c4a44f1d4555e2.jpg",
    "https://telegra.ph/file/81ccc91819c74c0afd59a.jpg",
    "https://telegra.ph/file/bf1199ecedff7e12eeb91.jpg",
    "https://telegra.ph/file/5824c5e679328ba92f76e.jpg",
    "https://telegra.ph/file/aa5a9578c6bf1397ddf9f.jpg",
    "https://telegra.ph/file/31ea4df56e9f505f2334d.jpg",
    "https://telegra.ph/file/ee739e60ba8f469243fb3.jpg",
    "https://telegra.ph/file/9b9013c7a38ca2e316120.jpg",
    "https://telegra.ph/file/47e1bac996ec048cc2c91.jpg",
    "https://telegra.ph/file/9636e9ad5c7fca03b88c8.jpg",
    "https://telegra.ph/file/b4754f61293b62e53c994.jpg",
    "https://telegra.ph/file/625df7388b3af29a5cfc3.jpg",
    "https://telegra.ph/file/31270801b4db94cdb21f8.jpg",
    "https://telegra.ph/file/c045971faaa8d81748501.jpg",
    "https://telegra.ph/file/186dd1c89e7051f2127bb.jpg",
    "https://telegra.ph/file/091e8d4a4d65ec60d8402.jpg",
    "https://telegra.ph/file/146b1e5da341abe0257c5.jpg",
    "https://telegra.ph/file/075d95a61c03a1516d7ef.jpg",
    "https://telegra.ph/file/b8f5223d6a2d524398715.jpg",
    "https://telegra.ph/file/59f11b56a41fb82f72b9f.jpg",
    "https://telegra.ph/file/a600f3ec62d053f6fe2f2.jpg",
    "https://telegra.ph/file/7812f585a45628d47f288.jpg",
    "https://telegra.ph/file/e95ef901fc1f9c89a1b9b.jpg",
    "https://telegra.ph/file/03ebf029f88de1232708d.jpg",
    "https://telegra.ph/file/dbbfdd9897aead16d0c93.jpg",
    "https://telegra.ph/file/c3886547a2dc23fd99f0f.jpg",
    "https://telegra.ph/file/4ed04eaceced2d51cf60b.jpg",
    "https://telegra.ph/file/bbd938156af969947a0f7.jpg",
    "https://telegra.ph/file/a6770f3c05abc68651259.jpg",
    "https://telegra.ph/file/9b29693f475b9efb4c589.jpg",
    "https://telegra.ph/file/61d796bdacbdb891cd126.jpg",
    "https://telegra.ph/file/43868e0b9fbfd53b3e722.jpg",
    "https://telegra.ph/file/a241a6da71738d6f9dc71.jpg",
    "https://telegra.ph/file/135152555f5f45042b3d0.jpg",
    "https://telegra.ph/file/2ff90d113ffe3547b29a6.jpg",
    "https://telegra.ph/file/812ce00f1b8b7b78f64c9.jpg",
    "https://telegra.ph/file/dca135a7511917485754d.jpg",
    "https://telegra.ph/file/c38c37187d0a72cbd23f7.jpg",
    "https://telegra.ph/file/b75fba8f1b7eea3aa1565.jpg",
    "https://telegra.ph/file/97c8e1d15cf8a1493dd34.jpg",
    "https://telegra.ph/file/45ac9f37fc37ac731e688.jpg",
    "https://telegra.ph/file/495164ac9794858d3821f.jpg",
    "https://telegra.ph/file/5dd080fe387cac3d29055.jpg",
    "https://telegra.ph/file/ef6408a9c6384e638e13c.jpg",
    "https://telegra.ph/file/8dab1ce7def7f300dd5bf.jpg",
    "https://telegra.ph/file/10f62da853019b30d67e4.jpg",
    "https://telegra.ph/file/9188c91b8aee1c889e499.jpg",
    "https://telegra.ph/file/030e7b99f9bdab6967e03.jpg",
    "https://telegra.ph/file/3fe95f124f18e2e08e394.jpg",
    "https://telegra.ph/file/7d307f939973ebeed4c9d.jpg",
    "https://telegra.ph/file/2055a6710a1375b411638.jpg",
    "https://telegra.ph/file/7d04d42c47596be2e73fb.jpg",
    "https://telegra.ph/file/bcd7d31c9996b9c827c16.jpg",
    "https://telegra.ph/file/07f69513a57c36b3b8fb4.jpg",
    "https://telegra.ph/file/a7f84e1c311c65fef032b.jpg",
    "https://telegra.ph/file/417b8b04bea78a748d14d.jpg",
    "https://telegra.ph/file/29f561ba6d0ad21f29a56.jpg",
    "https://telegra.ph/file/1183a196f462a54a9cd78.jpg",
    "https://telegra.ph/file/1962f2d778f98bd2985e7.jpg",
    "https://telegra.ph/file/fdd3735c10c29dacf9591.jpg",
    "https://telegra.ph/file/52044f59f349a5889849f.jpg",
    "https://telegra.ph/file/a44f5175af36ff8db57e8.jpg",
    "https://telegra.ph/file/f52ba37ba1f4c56ce4638.jpg",
    "https://telegra.ph/file/af90e3b1b30a257348625.jpg",
    "https://telegra.ph/file/abc154a7f5c0acb4b8871.jpg",
    "https://telegra.ph/file/22c8bc6e62792ed607f3d.jpg",
    "https://telegra.ph/file/68923e77945e3a3266063.jpg",
    "https://telegra.ph/file/368e512d98a89ebd819be.jpg",
    "https://telegra.ph/file/4d75972dd3a4b84a9cf6a.jpg",
    "https://telegra.ph/file/d94e271acec559d236010.jpg",
    "https://telegra.ph/file/4d81fbb5f2b490e430d8a.jpg",
    "https://telegra.ph/file/413ad5d0ad42f571f24dd.jpg"
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
        caption="Hᴇʀᴇ 😊 !",
        reply_to_message_id=rep_mesg_id
    )
