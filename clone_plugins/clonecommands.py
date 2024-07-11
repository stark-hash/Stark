import base64, logging, random, asyncio

from Script import script
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from database.ia_filterdb import get_file_details
from info import CPICS, AUTO_DELETE_TIME, AUTO_DELETE, CUSTOM_FILE_CAPTION, CLONE_START_MESSAGE, CDB_NAME 
from utils import get_size

from info import CLONE_DB_URI as MONGO_URL
from pymongo import MongoClient

logger = logging.getLogger(__name__)
BATCH_FILES = {}

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["cloned_fdbotz"]
mongo_collection = mongo_db[CDB_NAME]


@Client.on_message(filters.command("start") & filters.incoming & filters.text)
async def start(client, message):
    # Define inline buttons
    buttons = [[ 
        InlineKeyboardButton("ᴍʏ ᴘᴀʀᴇɴᴛ 🔈", url="https://t.me/AnAutoFilterBot")
    ],[
        InlineKeyboardButton("Hᴇʟᴩ 🕸", callback_data="help"),
        InlineKeyboardButton("Aʙᴏᴜᴛ ✨", callback_data="about")
    ]]

    # Reply with a photo, caption, and buttons
    owner = mongo_db.bots.find_one({'bot_id': id})
    ownerid = int(owner['user_id'])
    await message.reply_photo(
        photo=random.choice(CPICS),
        caption=CLONE_START_MESSAGE.format(ownerid),
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.HTML
    )

    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""   

    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                protect_content=True if pre == 'filep' else False,
                )
            filetype = msg.media
            file = getattr(msg, filetype.value)
            title = '@StarkBotUpdates  ' + ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), file.file_name.split()))
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            await msg.edit_caption(f_caption)
            k = await msg.reply(f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nThis Movie File/Video will be deleted in <b><u>{AUTO_DELETE} mins</u> 🫥 <i></b>(Due to Copyright Issues)</i>.\n\n<b><i>Please forward this File/Video to your Saved Messages and Start Download there</i></b>",quote=True)
            await asyncio.sleep(AUTO_DELETE_TIME)
            await msg.delete()
            await k.edit_text("<b>Your File/Video is successfully deleted!!!</b>")
            return
        except:
            pass
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=True if pre == 'filep' else False,
        )

@Client.on_callback_query(filters.regex("^(help|about|start|extmod|aifoto|apkdownloader|terabox|carbon|chatgpt|crypto|font|handwrite|lyrics|password|paste|photo|pinterest|qr|share_text|telegraph)$"))
async def handle_callback_query(client, query: CallbackQuery):
    if query.data == "help":
        buttons = [
            [
                InlineKeyboardButton('🎀 ᴅɪꜱᴄʟᴀɪᴍᴇʀ 🎀', 'trailers'),
                InlineKeyboardButton('ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ❄️', 'about')
            ],
            [
                InlineKeyboardButton('ᴀʟɪᴠᴇ', 'alive'),
                InlineKeyboardButton('ᴊꜱᴏɴ', 'json'),
                InlineKeyboardButton('ᴇxᴛʀᴀ ᴍᴏᴅᴇ', 'extmod')
            ],
            [
                InlineKeyboardButton('Sʜᴀʀᴇ Tᴇxᴛ', 'sharetext'),
                InlineKeyboardButton('Wᴀʟʟᴘᴀᴘᴇʀs', 'wallpapers')
            ],
            [
                InlineKeyboardButton(text="ᴀɪꜰᴏᴛᴏ", callback_data="aifoto"),
                InlineKeyboardButton(text="ᴀᴘᴋᴅᴏᴡɴʟᴏᴀᴅᴇʀ", callback_data="apkdownloader"),
                InlineKeyboardButton(text="ᴛᴇʀᴀʙᴏx", callback_data="terabox")
            ],
            [
                InlineKeyboardButton(text="ᴄᴀʀʙᴏɴ", callback_data="carbon"),
                InlineKeyboardButton(text="ᴄʜᴀᴛɢᴘᴛ", callback_data="chatgpt")
            ],
            [
                InlineKeyboardButton(text="ᴄʀʏᴘᴛᴏ", callback_data="crypto"),
                InlineKeyboardButton(text="ꜰᴏɴᴛ", callback_data="font"),
                InlineKeyboardButton(text="ʜᴀɴᴅᴡʀɪᴛᴇ", callback_data="handwrite")
            ],
            [
                InlineKeyboardButton(text="ʟʏʀɪᴄꜱ", callback_data="lyrics"),
                InlineKeyboardButton(text="ᴘᴀꜱꜱᴡᴏʀᴅ", callback_data="password")
            ],
            [
                InlineKeyboardButton(text="ᴘᴀꜱᴛᴇ", callback_data="paste"),
                InlineKeyboardButton(text="ᴘʜᴏᴛᴏ", callback_data="photo"),
                InlineKeyboardButton(text="ᴘɪɴᴛᴇʀᴇꜱᴛ", callback_data="pinterest")
            ],
            [
                InlineKeyboardButton(text="ǫʀ", callback_data="qr"),
                InlineKeyboardButton(text="ᴛᴇʟᴇɢʀᴀᴘʜ", callback_data="telegraph")
            ],
            [
                InlineKeyboardButton(text="ᴛᴛꜱ", callback_data="tts"),
                InlineKeyboardButton(text="ᴡᴇʙꜱꜱ", callback_data="webss"),
                InlineKeyboardButton(text="ᴡɪᴋɪ", callback_data="wiki")
            ],
            [
                InlineKeyboardButton('✘ ᴄʟᴏꜱᴇ', 'close_data'),
                InlineKeyboardButton(text="« ʙᴀᴄᴋ", callback_data="start")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [
            [
                InlineKeyboardButton('ꜰᴅʙᴏᴛᴢ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('ʙᴀᴄᴋ', 'help'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        
        me2 = (await client.get_me()).mention
        id = client.me.id
        owner = mongo_db.bots.find_one({'bot_id': id})
        ownerid = int(owner['user_id'])
        await query.message.edit_text(
        text=script.CABOUT_TXT.format(me2, ownerid),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    elif query.data == "start":
        me3 = (await client.get_me()).username
        buttons = [
            [
                InlineKeyboardButton("➕️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕️", url=f"http://t.me/{me3}?startgroup=true")
            ],
            [
                InlineKeyboardButton('Hᴇʟᴩ 🕸', callback_data="help"),
                InlineKeyboardButton('Aʙᴏᴜᴛ ✨', callback_data="about")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.CLONE_START_MESSAGE,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "extmod":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.AIIMAGE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "sharetext":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.SHARETXT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "wallpapers":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.WALLPAPER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "aifoto":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.AIIMAGE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "alive":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.ALIVE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "json":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.JSON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "carbon":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.CARBON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "apkdownloader":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.APKDL_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "terabox":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.TERABOX_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "carbon":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        text = script.CARBON_TXT

    elif query.data == "chatgpt":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.CHATGPT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "crypto":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.CRYPTO_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "font":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.FONT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "handwrite":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.HANDWRITE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "lyrics":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.LYRICS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "password":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.PWGEN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "paste":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.PASTE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "photo":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.PICEDIT_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "pinterest":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.PINTEREST_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "qr":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.QR_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
      
    elif query.data == "telegraph":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.TELEGRAPH_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "tts":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.TTS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "webss":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.WEBSS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "wiki":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.WIKI_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    
    elif query.data == "webss":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.WEBSS_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "trailers":
        buttons = [
            [
                InlineKeyboardButton('ＦＤ  ＢＯＴＺ ', url='https://t.me/FDBotz')
            ],
            [
                InlineKeyboardButton('‹ Bᴀᴄᴋ', callback_data='help')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            chat_id=query.message.chat.id, 
            message_id=query.message.id, 
            media=InputMediaPhoto(random.choice(CPICS))
        )
        await query.message.edit_text(
            text=script.TRAILER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )





        
