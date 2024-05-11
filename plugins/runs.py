import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "In the middle of difficulty lies opportunity.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The way to get started is to quit talking and begin doing.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "Don't watch the clock; do what it does. Keep going.",
    "The only place where success comes before work is in the dictionary.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Opportunities don't happen, you create them.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "The best way to predict the future is to create it.",
    "Everything you can imagine is real.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The secret of getting ahead is getting started.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
