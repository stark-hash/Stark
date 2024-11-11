import os, math, logging, datetime, pytz
import logging.config

from pyrogram.errors import BadRequest, Unauthorized
from pyrogram import Client
from pyrogram import types

from database.ia_filterdb import Media, Media2, choose_mediaDB, db as clientDB
from database.users_chats_db import db
from info import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, UPTIME, WEBHOOK, LOG_MSG, SECONDDB_URI
from utils import temp, __repo__, __license__, __copyright__, __version__
from typing import Union, Optional, AsyncGenerator
from plugins import web_server 

from plugins.clone import restart_bots
from aiohttp import web

# Get logging configurations
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="Professor-Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats        
        await super().start()
        await Media.ensure_indexes()
        await Media2.ensure_indexes()
        #choose the right db by checking the free space
        stats = await clientDB.command('dbStats')
        #calculating the free db space from bytes to MB
        free_dbSize = round(512-((stats['dataSize']/(1024*1024))+(stats['indexSize']/(1024*1024))), 2)
        if SECONDDB_URI and free_dbSize<10: #if the primary db have less than 10MB left, use second DB.
            tempDict["indexDB"] = SECONDDB_URI
            logging.info(f"Since Primary DB have only {free_dbSize} MB left, Secondary DB will be used to store datas.")
        elif SECONDDB_URI is None:
            logging.error("Missing second DB URI !\n\nAdd SECONDDB_URI now !\n\nExiting...")
            exit()
        else:
            logging.info(f"Since primary DB have enough space ({free_dbSize}MB) left, It will be used for storing datas.")
        await choose_mediaDB()
        me = await self.get_me()
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.id = me.id
        self.name = me.first_name
        self.mention = me.mention
        self.username = me.username
        self.log_channel = LOG_CHANNEL
        self.uptime = UPTIME
        curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        tame = curr.strftime('%I:%M:%S %p')
        logger.info(LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__))
        try: await self.send_message(LOG_CHANNEL, text=LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__), disable_web_page_preview=True)   
        except Exception as e: logger.warning(f"Bot Isn't Able To Send Message To LOG_CHANNEL \n{e}")
        if WEBHOOK is True:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
            await restart_bots()
            print("Restarted All Clone Bots.")
            logger.info("Web Response Is Running......🕸️")
            
    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logger.info(f"{me.first_name} is_...  ♻️Restarting...")

    async def iter_messages(self, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:                       
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1


Bot().run()
