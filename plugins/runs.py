import random
from pyrogram import Client, filters

def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

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
    filters.command("runs")
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
