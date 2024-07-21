from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

from image.edit_1 import bright, mix, black_white, g_blur, normal_blur, box_blur
from image.edit_2 import circle_with_bg, circle_without_bg, sticker, edge_curved, contrast, sepia_mode, pencil, cartoon                             
from image.edit_3 import green_border, blue_border, black_border, red_border
from image.edit_4 import rotate_90, rotate_180, rotate_270, inverted, round_sticker, removebg_white, removebg_plain, removebg_sticker
from image.edit_5 import normalglitch_1, normalglitch_2, normalglitch_3, normalglitch_4, normalglitch_5, scanlineglitch_1, scanlineglitch_2, scanlineglitch_3, scanlineglitch_4, scanlineglitch_5



@Client.on_message(filters.photo & filters.private)
async def photo_handler(client, message):
    buttons = [[
        InlineKeyboardButton(text="𝖡𝗋𝗂𝗀𝗍𝗁", callback_data="bright"),
        InlineKeyboardButton(text="𝖬𝗂𝗑𝖾𝖽", callback_data="mix"),
        InlineKeyboardButton(text="𝖡 & 𝖶", callback_data="b|w"),
        ],[
        InlineKeyboardButton(text="𝖢𝗂𝗋𝖼𝗅𝖾", callback_data="circle"),
        InlineKeyboardButton(text="𝖡𝗅𝗎𝗋", callback_data="blur"),
        InlineKeyboardButton(text="𝖡𝗈𝗋𝖽𝖾𝗋", callback_data="border"),
        ],[
        InlineKeyboardButton(text="𝖲𝗍𝗂𝖼𝗄𝖾𝗋", callback_data="stick"),
        InlineKeyboardButton(text="𝖱𝗈𝗍𝖺𝗍𝖾", callback_data="rotate"),
        InlineKeyboardButton(text="𝖢𝗈𝗇𝗍𝗋𝖺𝗌𝗍", callback_data="contrast"),
        ],[
        InlineKeyboardButton(text="𝖲𝖾𝗉𝗂𝖺", callback_data="sepia"),
        InlineKeyboardButton(text="𝖯𝖾𝗇𝖼𝗂𝗅", callback_data="pencil"),
        InlineKeyboardButton(text="𝖢𝖺𝗋𝗍𝗈𝗈𝗇", callback_data="cartoon"),
        ],[
        InlineKeyboardButton(text="𝖨𝗇𝗏𝖾𝗋𝗍", callback_data="inverted"),
        InlineKeyboardButton(text="𝖦𝗅𝗂𝗍𝖼𝗁", callback_data="glitch"),
        InlineKeyboardButton(text="𝖱𝖾𝗆𝗈𝗏𝖾 𝖡𝖦", callback_data="removebg"),
        ],[
        InlineKeyboardButton(text="𝖢𝗅𝗈𝗌𝖾", callback_data="close_data"),
    ]]
    try:
        await message.reply(text="Select Your Required Mode From Below", quote=True, reply_markup=InlineKeyboardMarkup(buttons))            
    except Exception as e:
        print(e)
        if "USER_IS_BLOCKED" in str(e): return           
        try: await message.reply_text(f"{e} \nSomething Went Wrong!", quote=True)
        except Exception: return

@Client.on_callback_query(filters.regex("^(bright|mix|b|w|circle|blur|border|stick|rotate|contrast|sepia|pencil|cartoon|inverted|glitch|removebg|close_data|rmbgwhite|rmbgplain|rmbgsticker|stkr|cur_ved|circle_sticker|180|90|270|normalglitch|scanlineglitch|box|normal|gas|circlewithbg|circlewithoutbg|red|green|blue|black)$"))
async def callback_query_handler(client, query):
    data = query.data

    if data == "removebg":
        buttons = [
            [
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁 𝖶𝗁𝗂𝗍𝖾 𝖡𝖦", callback_data="rmbgwhite"),
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁𝗈𝗎𝗍 𝖡𝖦", callback_data="rmbgplain"),
            ],
            [
                InlineKeyboardButton(text="𝖲𝗍𝗂𝖼𝗄𝖾𝗋", callback_data="rmbgsticker"),
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "stick":
        buttons = [
            [
                InlineKeyboardButton(text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="stkr"),
                InlineKeyboardButton(text="𝖤𝖽𝗀𝖾 𝖢𝗎𝗋𝗏𝖾𝖽", callback_data="cur_ved"),
            ],
            [
                InlineKeyboardButton(text="𝖢𝗂𝗋𝖼𝗅𝖾", callback_data="circle_sticker")
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select A Type**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "rotate":
        buttons = [
            [
                InlineKeyboardButton(text="180", callback_data="180"),
                InlineKeyboardButton(text="90", callback_data="90")
            ],
            [
                InlineKeyboardButton(text="270", callback_data="270")
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select The Degree**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "glitch":
        buttons = [
            [
                InlineKeyboardButton(text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="normalglitch"),
                InlineKeyboardButton(text="𝖲𝖼𝖺𝗇 𝖫𝖺𝗂𝗇𝗌", callback_data="scanlineglitch")
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "normalglitch":
        buttons = [
            [
                InlineKeyboardButton(text="1", callback_data="normalglitch1"),
                InlineKeyboardButton(text="2", callback_data="normalglitch2"),
                InlineKeyboardButton(text="3", callback_data="normalglitch3"),
            ],
            [
                InlineKeyboardButton(text="4", callback_data="normalglitch4"),
                InlineKeyboardButton(text="5", callback_data="normalglitch5"),
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="glitch")
            ]
        ]
        await query.message.edit_text(text="**Select Glitch Power Level**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "scanlineglitch":
        buttons = [
            [
                InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
                InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
                InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
            ],
            [
                InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
                InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="glitch")
            ]
        ]
        await query.message.edit_text("**Select Glitch Power Level**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "blur":
        buttons = [
            [
                InlineKeyboardButton(text="𝖡𝗈𝗑", callback_data="box"),
                InlineKeyboardButton(text="𝖭𝗈𝗋𝗆𝖺𝗅", callback_data="normal"),
            ],
            [
                InlineKeyboardButton(text="𝖦𝖺𝗎𝗌𝗌𝗂𝖺𝗇", callback_data="gas")
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select A Type**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "circle":
        buttons = [
            [
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁 𝖡𝖦", callback_data="circlewithbg"),
                InlineKeyboardButton(text="𝖶𝗂𝗍𝗁𝗈𝗎𝗍 𝖡𝖦", callback_data="circlewithoutbg"),
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "border":
        buttons = [
            [
                InlineKeyboardButton(text="𝖱𝖾𝖽", callback_data="red"),
                InlineKeyboardButton(text="𝖦𝗋𝖾𝖾𝗇", callback_data="green"),
            ],
            [
                InlineKeyboardButton(text="𝖡𝗅𝖺𝖼𝗄", callback_data="black"),
                InlineKeyboardButton(text="𝖡𝗅𝗎𝖾", callback_data="blue"),
            ],
            [
                InlineKeyboardButton(text="𝙱𝙰𝙲𝙺", callback_data="photo")
            ]
        ]
        await query.message.edit_text("**Select Required Color**", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()

    elif query.data == "bright":
        await bright(client, query.message)
    elif query.data == "mix":
        await mix(client, query.message)
    elif query.data == "b|w":
        await black_white(client, query.message)
    elif query.data == "circlewithbg":
        await circle_with_bg(client, query.message)
    elif query.data == "circlewithoutbg":
        await circle_without_bg(client, query.message)
    elif query.data == "green":
        await green_border(client, query.message)
    elif query.data == "blue":
        await blue_border(client, query.message)
    elif query.data == "red":
        await red_border(client, query.message)
    elif query.data == "black":
        await black_border(client, query.message)
    elif query.data == "circle_sticker":
        await round_sticker(client, query.message)
    elif query.data == "inverted":
        await inverted(client, query.message)
    elif query.data == "stkr":
        await sticker(client, query.message)
    elif query.data == "cur_ved":
        await edge_curved(client, query.message)
    elif query.data == "90":
        await rotate_90(client, query.message)
    elif query.data == "180":
        await rotate_180(client, query.message)
    elif query.data == "270":
        await rotate_270(client, query.message)
    elif query.data == "contrast":
        await contrast(client, query.message)
    elif query.data == "box":
        await box_blur(client, query.message)
    elif query.data == "gas":
        await g_blur(client, query.message)
    elif query.data == "normal":
        await normal_blur(client, query.message)
    elif query.data == "sepia":
        await sepia_mode(client, query.message)
    elif query.data == "pencil":
        await pencil(client, query.message)
    elif query.data == "cartoon":
        await cartoon(client, query.message)
    elif query.data == "normalglitch1":
        await normalglitch_1(client, query.message)
    elif query.data == "normalglitch2":
        await normalglitch_2(client, query.message)
    elif query.data == "normalglitch3":
        await normalglitch_3(client, query.message)
    elif query.data == "normalglitch4":
        await normalglitch_4(client, query.message)
    elif query.data == "normalglitch5":
        await normalglitch_5(client, query.message)
    elif query.data == "scanlineglitch1":
        await scanlineglitch_1(client, query.message)
    elif query.data == "scanlineglitch2":
        await scanlineglitch_2(client, query.message)
    elif query.data == "scanlineglitch3":
        await scanlineglitch_3(client, query.message)
    elif query.data == "scanlineglitch4":
        await scanlineglitch_4(client, query.message)
    elif query.data == "scanlineglitch5":
        await scanlineglitch_5(client, query.message)
    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)
    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)
    elif query.data == "rmbgsticker":
        await removebg_sticker(client, query.message)
    elif query.data == "pages":
        await query.answer("🤨 Cᴜʀɪᴏsɪᴛʏ Is A Lɪᴛᴛʟᴇ Mᴏʀᴇ, Isɴ'ᴛ Iᴛ? 😁", show_alert=True)


