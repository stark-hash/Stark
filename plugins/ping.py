"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "​🇸​​🇹​​🇮​​🇱​​🇱​ ​🇭​​🇪​​🇷​​🇪​, ​🇺​​🇳​​🇱​​🇮​​🇰​​🇪​ ​🇾​​🇴​​🇺​​🇷​ ​🇪​​🇽​🥲\n\n ⍟𝐌𝐲 𝐜𝐫𝐞𝐚𝐭𝐨𝐫: @TGTesla\n\n⍟𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭: @StarkBotSupport\n\n⍟𝐌𝐲 𝐮𝐩𝐝𝐚𝐭𝐞𝐬: @StarkBotUpdates\n\n⍟𝐌𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐫: @TGTesla"
HELP = "ᴅᴇᴀʀ ɢᴏᴅ, ᴘʟᴇᴀꜱᴇ ʜᴇʟᴘ ᴀɴᴅ ʟɪʙᴇʀᴀᴛᴇ ᴛʜᴇ ꜱᴛᴀᴛᴇ ᴏꜰ ᴘᴀʟᴇꜱᴛɪɴᴇ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴀꜱᴘ ᴏꜰ ᴏᴘᴘʀᴇꜱꜱᴏʀꜱ..."
REPO = "ᴅᴏ ʏᴏᴜ ᴀʟꜱᴏ ᴀꜱᴋ ᴍᴀɢɪᴄɪᴀɴꜱ ᴛᴏ ʀᴇᴠᴇᴀʟ ᴛʜᴇɪʀ ᴛʀɪᴄᴋꜱ?"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("helpme", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
