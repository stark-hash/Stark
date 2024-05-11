from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.cust_p_filters import f_onw_fliter

# LUCK------------ https://telegram.me/Josprojects ------------ #

# EMOJI CONSTANTS
PIN_BALL = "🎳"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["pinball", "tenpin"])
)
async def pinball_tenpin(client, message):
    """ /pinball an @animatedpinball """
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=PIN_BALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
