import base64, logging
from pyrogram import filters, Client, enums
from info import ADMINS, LOGS_CHANNEL, PUBLIC_FILE_STORE
from database.ia_filterdb import unpack_new_file_id
from utils import temp
from info import CLONE_DB_URI as MONGO_URL
from pymongo import MongoClient

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["cloned_fdbotz"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False

@Client.on_message(filters.command(['link', 'plink']) & filters.create(allowed))
async def gen_link_s(bot, message):
    id = bot.me.id
    owner = mongo_db.bots.find_one({'bot_id': id})
    ownerid = int(owner['user_id'])
    if ownerid != message.from_user.id:
        await message.reply_text("ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅ❗")
        return
    replied = message.reply_to_message
    if not replied:
        return await message.reply('Reply to a message to get a shareable link.')
    file_type = replied.media
    if file_type not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
        return await message.reply("Reply to a supported media")
    if message.has_protected_content and message.chat.id not in ADMINS:
        return await message.reply("​🇺​​🇳​​🇵​​🇷​​🇴​​🇹​​🇪​​🇨​​🇹​ ​🇮​​🇹​ !")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type.value)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    bot_username = (await bot.get_me()).username
    temp.CU_NAME = bot_username
    link = f"https://t.me/{temp.CU_NAME}?start={outstr}"
    
    # Reply to the user with the generated link
    await message.reply(f"Here is your Link:\n{link}")
    
    # Send the generated link to the log channel
    await bot.send_message(
        chat_id=LOGS_CHANNEL,
        text=f"Generated Link: {link}\n\nBy: @{message.from_user.username} (ID: {message.from_user.id})"
    )
