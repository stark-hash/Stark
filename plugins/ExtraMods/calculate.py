from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Define calculator text and buttons
CALCULATE_TEXT = "Made by @StarkBotUpdates"
CALCULATE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DEL", callback_data="calc_DEL"),
            InlineKeyboardButton("AC", callback_data="calc_AC"),
            InlineKeyboardButton("(", callback_data="calc_("),
            InlineKeyboardButton(")", callback_data="calc_)")
        ],
        [
            InlineKeyboardButton("7", callback_data="calc_7"),
            InlineKeyboardButton("8", callback_data="calc_8"),
            InlineKeyboardButton("9", callback_data="calc_9"),
            InlineKeyboardButton("÷", callback_data="calc_/")
        ],
        [
            InlineKeyboardButton("4", callback_data="calc_4"),
            InlineKeyboardButton("5", callback_data="calc_5"),
            InlineKeyboardButton("6", callback_data="calc_6"),
            InlineKeyboardButton("×", callback_data="calc_*")
        ],
        [
            InlineKeyboardButton("1", callback_data="calc_1"),
            InlineKeyboardButton("2", callback_data="calc_2"),
            InlineKeyboardButton("3", callback_data="calc_3"),
            InlineKeyboardButton("-", callback_data="calc_-")
        ],
        [
            InlineKeyboardButton(".", callback_data="calc_."),
            InlineKeyboardButton("0", callback_data="calc_0"),
            InlineKeyboardButton("=", callback_data="calc_="),
            InlineKeyboardButton("+", callback_data="calc_+")
        ]
    ]
)

@Client.on_message(filters.private & filters.command(["calc", "calculate", "calculator"]))
async def calculate(bot, message):
    try:
        await message.reply_text(
            text=CALCULATE_TEXT,
            reply_markup=CALCULATE_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as e:
        print(e)
        if "USER_IS_BLOCKED" in str(e):
            return
        try:
            await message.reply_text(f"{e}\nSomething Went Wrong!", quote=True)
        except Exception:
            return

@Client.on_callback_query()
async def handle_callback_query(bot, update):
    data = update.data

    if data.startswith("calc_"):
        await handle_calculator_callback(bot, update)
    else:
        await handle_autofilter_callback(bot, update)

async def handle_calculator_callback(bot, update):
    data = update.data.replace("calc_", "")
    try:
        message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
        message_text = '' if CALCULATE_TEXT in message_text else message_text

        if data == "=":
            text = float(eval(message_text.replace("×", "*").replace("÷", "/")))
        elif data == "DEL":
            text = message_text[:-1]
        elif data == "AC":
            text = ""
        else:
            text = message_text + data

        await update.message.edit_text(
            text=f"{text}\n\n{CALCULATE_TEXT}",
            disable_web_page_preview=True,
            reply_markup=CALCULATE_BUTTONS
        )
    except Exception as e:
        print(e)
        if "USER_IS_BLOCKED" in str(e):
            return
        try:
            await update.message.reply_text(f"{e}\nSomething Went Wrong!", quote=True)
        except Exception:
            return

async def handle_autofilter_callback(bot, update):
    try:
        # Implement your autofilter callback logic here
        await update.message.reply_text("Autofilter callback received!", quote=True)
    except Exception as e:
        print(e)
        if "USER_IS_BLOCKED" in str(e):
            return
        try:
            await update.message.reply_text(f"{e}\nSomething Went Wrong!", quote=True)
        except Exception:
            return
