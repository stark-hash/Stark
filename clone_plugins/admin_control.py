from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty

from info import IMDB_CLONETEMPLATE
from utils import get_size, get_poster
from database.users_chats_db import db
from database.ia_filterdb import Media
from Script import script
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('<b>Pʟᴇᴀꜱᴇ Wᴀɪᴛ...</b>')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(script.STATUS_TXT.format(files, total_users, totl_chats, size, free))
    
  
@Client.on_message((filters.command(["imdb", "search"]) & filters.text & filters.incoming & filters.group) | (filters.text & filters.incoming & filters.group))
async def imdb_search(client, message):
    if message.text.startswith("/"): return  
    if ' ' in message.text and any(message.text.startswith(f"/{cmd}") for cmd in ["imdb", "search"]):
        k = await message.reply('ꜱᴇᴀʀᴄʜɪɴɢ ɪᴍᴅʙ...')
        _, title = message.text.split(None, 1)
    else:
        title = message.text

    if title:
        k = await message.reply('ꜱᴇᴀʀᴄʜɪɴɢ ɪᴍᴅʙ...')
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("ɴᴏ ʀᴇꜱᴜʟᴛ ꜰᴏᴜɴᴅ")
        btn = [[InlineKeyboardButton(f"{movie.get('title')} - {movie.get('year')}", callback_data=f"imdb#{movie.movieID}")] for movie in movies]
        await k.edit('Hᴇʀᴇ Iꜱ Wʜᴀᴛ I Fᴏᴜɴᴅ Oɴ Iᴍᴅʙ', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Gɪᴠᴇ Mᴇ A Mᴏᴠɪᴇ / Sᴇʀɪᴇs Nᴀᴍᴇ')


@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, quer_y: CallbackQuery):
    i, movie = quer_y.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [[InlineKeyboardButton(f"{imdb.get('title')}", url=imdb['url'])]]
    message = quer_y.message.reply_to_message or quer_y.message
    if imdb:
        caption = IMDB_CLONETEMPLATE.format(
            query = imdb['title'],
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url'],
            **locals()
        )
    else:
        caption = "ɴᴏ ʀᴇꜱᴜʟᴛꜱ"
    if imdb.get('poster'):
        try:
            await quer_y.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await quer_y.message.reply_photo(photo=poster, caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        except Exception as e:
            logger.exception(e)
            await quer_y.message.reply(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
        await quer_y.message.delete()
    else:
        await quer_y.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
   
   



        



