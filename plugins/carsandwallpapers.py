from pyrogram import Client, filters
import random

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
    "https://telegra.ph/file/13086135c1b7d0f11098d.jpg",
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

SCENERY_LINKS = [
    "https://telegra.ph/file/4ae97c58fc102edff5091.jpg",
    "https://telegra.ph/file/f9e785a082e3039b6c7ad.jpg",
    "https://telegra.ph/file/c8c88d59e1b9388e44760.jpg",
    "https://telegra.ph/file/a3a39d341dea34bcf505c.jpg",
    "https://telegra.ph/file/0c9e1158394f0b98557f9.jpg",
    "https://telegra.ph/file/138ea7e1d060b7c33aa5b.jpg",
    "https://telegra.ph/file/3ba85e586fb7b90c7b11e.jpg",
    "https://telegra.ph/file/6d1923c88d42affbc2c13.jpg",
    "https://telegra.ph/file/2b4e43a012ccac8a104b5.jpg",
    "https://telegra.ph/file/4ed44b9749972e4830266.jpg",
    "https://telegra.ph/file/26160ef099242c543fb2c.jpg",
    "https://telegra.ph/file/20aef818e50ab9f82b5be.jpg",
    "https://telegra.ph/file/ce30904c4cc272581f165.jpg",
    "https://telegra.ph/file/f5b21529f10b3d2450151.jpg",
    "https://telegra.ph/file/097e622758eb180f1c65f.jpg",
    "https://telegra.ph/file/1c6290e86b4125cdf0b1a.jpg",
    "https://telegra.ph/file/88998555298509060db86.jpg",
    "https://telegra.ph/file/50638ff52c630153bf9d1.jpg",
    "https://telegra.ph/file/f56f9368811bf421139f0.jpg",
    "https://telegra.ph/file/16f02e8d4a30d9487017e.jpg",
    "https://telegra.ph/file/34b81e17572f084d19560.jpg",
    "https://telegra.ph/file/337b08fcee5c210a773ea.jpg",
    "https://telegra.ph/file/2ccd89df380b6053b99f9.jpg",
    "https://telegra.ph/file/bb2677c71cfdadbd74e6d.jpg",
    "https://telegra.ph/file/3cc7f101d8986dbbe759f.jpg",
    "https://telegra.ph/file/2f5a892080f487297e1f3.jpg",
    "https://telegra.ph/file/3c394c436fd696ec628ac.jpg",
    "https://telegra.ph/file/7bfa2921021e049d1a4c5.jpg",
    "https://telegra.ph/file/38c33d537c93c3be8743c.jpg",
    "https://telegra.ph/file/3007992430153dcaf719e.jpg",
    "https://telegra.ph/file/aec9a43a9ceeedd145215.jpg",
    "https://telegra.ph/file/3c8fae25170dd6a32ae8a.jpg",
    "https://telegra.ph/file/8e7c029b5420331f2b57c.jpg",
    "https://telegra.ph/file/cdcc84f799bce0123f222.jpg",
    "https://telegra.ph/file/530b6bfcf8f4995ed2c24.jpg",
    "https://telegra.ph/file/7388be69f176734ef7d3f.jpg",
    "https://telegra.ph/file/6028614478badaa3b046c.jpg",
    "https://telegra.ph/file/d1b7c1e8d7dfb485f37a9.jpg",
    "https://telegra.ph/file/040741f6bd923f3424490.jpg",
    "https://telegra.ph/file/8bdf2d2d55288c9eca02b.jpg",
    "https://telegra.ph/file/fe455728874ff3ea04e04.jpg",
    "https://telegra.ph/file/8cdeb231bcf3f0729dbc1.jpg",
    "https://telegra.ph/file/b3d82f0cfe8dfb7f15817.jpg",
    "https://telegra.ph/file/970669e9157fef6e9b0f3.jpg",
    "https://telegra.ph/file/149a05cbc3b143b1b77dc.jpg",
    "https://telegra.ph/file/43be3bbfce0ca6f3ad16d.jpg",
    "https://telegra.ph/file/a378167152e8e65d4c183.jpg",
    "https://telegra.ph/file/fef2d09b4aa62bd7e0546.jpg",
    "https://telegra.ph/file/623f799844bbd6c1fd75e.jpg",
    "https://telegra.ph/file/ba35ece6d50112e4459da.jpg",
    "https://telegra.ph/file/854c2e7635666c0e63ba9.jpg",
    "https://telegra.ph/file/23b343867b9522dbf683f.jpg",
    "https://telegra.ph/file/24e83ae529e90c78a753b.jpg",
    "https://telegra.ph/file/373404f66a809f4e4aec4.jpg",
    "https://telegra.ph/file/78d06752f70447f1a69d1.jpg",
    "https://telegra.ph/file/c2d63c10f18bb37aa4a59.jpg",
    "https://telegra.ph/file/7484f17065defdf9bde82.jpg",
    "https://telegra.ph/file/8271b02bf62c3f081c8f5.jpg",
    "https://telegra.ph/file/ea2244229134f628db438.jpg",
    "https://telegra.ph/file/631f124ffb2a9bf0fc628.jpg",
    "https://telegra.ph/file/cb59cbbf1ca1493aed572.jpg",
    "https://telegra.ph/file/d0749870216af96639a5c.jpg",
    "https://telegra.ph/file/bfb10c257bf8e048bcbe0.jpg",
    "https://telegra.ph/file/70d9bf1d317f77c7b25d7.jpg",
    "https://telegra.ph/file/b94226c7a8d7eab1ac661.jpg",
    "https://telegra.ph/file/b94226c7a8d7eab1ac661.jpg",
    "https://telegra.ph/file/536a8b06446c010d4f46e.jpg",
    "https://telegra.ph/file/1e95ab94873329464a1f9.jpg",
    "https://telegra.ph/file/90f16ee52e82cd46d0e4e.jpg",
    "https://telegra.ph/file/bb80a85619d2316236720.jpg",
    "https://telegra.ph/file/9daefa98026b22de90c61.jpg",
    "https://telegra.ph/file/6b98b5a1cd0ac87236974.jpg"
]

MEMES = [
    "https://telegra.ph/file/4662853e1637b976820c6.jpg",
    "https://telegra.ph/file/435ebda3f2e055ca108e6.jpg",
    "https://telegra.ph/file/714bf07fe84f267de2292.jpg",
    "https://telegra.ph/file/5674d238c01e9c8fc2133.jpg",
    "https://telegra.ph/file/71351a04078280ee03f63.jpg",
    "https://telegra.ph/file/12a24f7f713406ffb88c8.jpg",
    "https://telegra.ph/file/cc95b8850aa88914a67aa.jpg",
    "https://telegra.ph/file/62449fafa7c526ab8363e.jpg",
    "https://telegra.ph/file/303b3ca322b5c6ef5187e.jpg"
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
    
@Client.on_message(
    filters.command(["nice"])
)
async def send_nice_wallpaper(client, message):
    """ /nice to get a random nice wallpaper """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id

    # Select a random car wallpaper link
    nice_wallpaper = random.choice(SCENERY_LINKS)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=nice_wallpaper,
        caption="Hᴇʀᴇ 😊 !",
        reply_to_message_id=rep_mesg_id
    )
@Client.on_message(
    filters.command(["meme"])
)
async def send_meme(client, message):
    """ /meme to get a random meme """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id

    # Select a random car wallpaper link
    meme = random.choice(MEMES)

    await client.send_photo(
        chat_id=message.chat.id,
        photo=meme,
        caption="Hᴇʀᴇ 😊 !",
        reply_to_message_id=rep_mesg_id
    )
