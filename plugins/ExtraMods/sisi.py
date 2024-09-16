import random
import time
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example list of credit card details
CC_DETAILS = [
    {"number": "4219 4000 0245 4560", "expiry": "09/26", "cvv": "173", "name": "", "address": "", "country": "ES"},
    {"number": "5374 1001 5289 0716", "expiry": "12/26", "cvv": "667", "name": "", "address": "", "country": " "},
    {"number": "5154 6200 2458 1306", "expiry": "09/2031", "cvv": "272", "name": "", "address": "", "country": "US"},
    {"number": "4482 3301 4809 8932", "expiry": "03/27", "cvv": "722", "name": "Berry Syerra", "address": "21022 Normandy Forest Dr, Spring, TX, 77388", "country": "US"},
    {"number": "5425 4301 2380 3160", "expiry": "07/29", "cvv": "779", "name": "", "address": "", "country": "ES"},
    {"number": "4301 5703 6900 9055", "expiry": "01/27", "cvv": "191", "name": "Debbie Bullington", "address": "PO Box 2725, Jackson, Wyoming, 83001", "country": "US"},
    {"number": "5110 4300 3912 0717", "expiry": "05/31", "cvv": "699", "name": "Numse Olsen", "address": "555 n rodeo dr, B", "country": "CN"},
    {"number": "4213 5237 5708 9137", "expiry": "11/25", "cvv": "185", "name": "", "address": "", "country": "PL"},
    {"number": "4436 2801 0927 6463", "expiry": "08/2026", "cvv": "955", "name": "", "address": "", "country": "US"},
    {"number": "4415 5544 4646 2514", "expiry": "10/25", "cvv": "233", "name": "", "address": "", "country": "BH"},
    {"number": "4258 3845 1582 9983", "expiry": "11/26", "cvv": "205", "name": "", "address": "", "country": "US"},
    {"number": "4516 0222 9559 2359", "expiry": "10/24", "cvv": "382", "name": "", "address": "", "country": "CA"},
    {"number": "4023 4705 2291 1460", "expiry": "09/26", "cvv": "528", "name": "", "address": "", "country": "US"},
    {"number": "4436 2801 0921 1684", "expiry": "08/2026", "cvv": "100", "name": "", "address": "", "country": "US"},
    {"number": "5344 1324 5469 3115", "expiry": "07/25", "cvv": "773", "name": "", "address": "", "country": "IT"},
    {"number": "4023 4705 2291 1460", "expiry": "09/26", "cvv": "528", "name": "", "address": "", "country": "US"},
    {"number": "4023 4705 2940 1853", "expiry": "11/25", "cvv": "794", "name": "Weston Ainge", "address": "303 N 900 E, Spanish Fork, UT, 84660", "country": "US"},
    {"number": "5527 3601 2327 6462", "expiry": "05/28", "cvv": "802", "name": "", "address": "", "country": "US"},
    {"number": "5144 0316 8894 3282", "expiry": "08/28", "cvv": "240", "name": "", "address": "", "country": "US"},
    {"number": "5144 0318 8894 3282", "expiry": "08/28", "cvv": "240", "name": "", "address": "", "country": "US"},
    {"number": "4270 8250 3292 7456", "expiry": "12/25", "cvv": "947", "name": "Cory Rossnagel", "address": "2645 N Halleck St, Portland, OR, 97217", "country": "US"},
    {"number": "5573 8300 2882 6648", "expiry": "01/28", "cvv": "315", "name": "Dylan Harrison", "address": "6 David St, South Glamorgan, Cardiff, CF10 2EH, United Kingdom", "country": "GB"},
    {"number": "4078 4300 0840 9573", "expiry": "08/27", "cvv": "077", "name": "SEAN D GUTIERREZ", "address": "", "country": "FR"},
    {"number": "4430 4500 9636 8286", "expiry": "10/26", "cvv": "298", "name": "Gregg A. Schultz", "address": "451 West Macon Street, Decatur, IL, 62522", "country": "US"},
    {"number": "4078 4300 0840 9573", "expiry": "08/27", "cvv": "890", "name": "RYZEN iOS", "address": "", "country": "FR"},
    {"number": "4935 1201 4396 3773", "expiry": "09/26", "cvv": "576", "name": "", "address": "", "country": "IT"},
    {"number": "5373 1703 1953 7279", "expiry": "11/26", "cvv": "829", "name": "", "address": "", "country": " "},
    {"number": "4100 4000 2520 3467", "expiry": "05/26", "cvv": "848", "name": "Gary Gallerstein", "address": "3014 Evergreen St., San Diego, CA, 92110", "country": "US"},
    {"number": "4130 4002 0006 8663", "expiry": "10/27", "cvv": "775", "name": "Ingrid Forster", "address": "4013173469, 3804 east fairfield road, Mount Vernon, IL, 62864", "country": "US"},
    {"number": "4430 4500 4749 1872", "expiry": "04/25", "cvv": "435", "name": "Staci Roy", "address": "6010 N Frostwood Pkwy, Peoria, IL, 61615", "country": "US"},
    {"number": "5373 1703 1953 7279", "expiry": "11/26", "cvv": "829", "name": "", "address": "", "country": " "},
    {"number": "4100 4000 2520 3467", "expiry": "05/26", "cvv": "848", "name": "Gary Gallerstein", "address": "3014 Evergreen St., San Diego, CA, 92110", "country": "US"},
    {"number": "4254 1809 5705 8535", "expiry": "04/28", "cvv": "998", "name": "", "address": "", "country": "US"},
    {"number": "4258 3645 0393 9242", "expiry": "03/27", "cvv": "671", "name": "Zuha Bajwa", "address": "29 Water St Apt 217, Claremont, NH, 03743", "country": "US"},
    {"number": "4935 1201 9936 7465", "expiry": "06/27", "cvv": "009", "name": "", "address": "", "country": "IT"},
    {"number": "4100 4000 2520 3467", "expiry": "05/26", "cvv": "848", "name": "", "address": "", "country": "US"},
    {"number": "5397 6800 1871 2512", "expiry": "03/28", "cvv": "438", "name": "Clemens Lockman", "address": "22871 21 Mile Rd, Michigan, Macomb, 48044", "country": "US"},
    {"number": "4366 1832 6888 4084", "expiry": "03/26", "cvv": "269", "name": "Aaron Palomino", "address": "1713 Marlowe Drive, Austin, TX, 78727", "country": "US"},
    {"number": "5247 3772 1168 8502", "expiry": "01/26", "cvv": "117", "name": "", "address": "", "country": "ES"},
    {"number": "4241 0396 7604 3403", "expiry": "05/25", "cvv": "580", "name": "", "address": "", "country": "ES"},
    {"number": "4187 8820 0194 4903", "expiry": "06/28", "cvv": "441", "name": "", "address": "", "country": "ES"},
    {"number": "4214 1714 3944 8982", "expiry": "09/24", "cvv": "851", "name": "", "address": "", "country": "US"},
    {"number": "4233 3395 1050 8682", "expiry": "07/26", "cvv": "145", "name": "", "address": "", "country": "US"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "4539 4233 2425 7280", "expiry": "05/27", "cvv": "477", "name": "", "address": "", "country": "ES"},
    {"number": "4921 9000 9901 2357", "expiry": "11/25", "cvv": "485", "name": "", "address": "", "country": "ES"},
    {"number": "5166 2910 8581 6658", "expiry": "03/28", "cvv": "131", "name": "", "address": "", "country": "US"},
    {"number": "4903 9270 0018 1304", "expiry": "09/26", "cvv": "382", "name": "", "address": "", "country": "ES"},
    {"number": "4716 6580 3101 4433", "expiry": "11/25", "cvv": "871", "name": "", "address": "", "country": "ES"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "4539 4233 2425 7280", "expiry": "05/27", "cvv": "477", "name": "", "address": "", "country": "ES"},
    {"number": "4214 1714 3944 8982", "expiry": "09/24", "cvv": "851", "name": "", "address": "", "country": "US"},
    {"number": "4521 2078 6692 1860", "expiry": "06/28", "cvv": "311", "name": "", "address": "", "country": "ES"},
    {"number": "4782 5455 4256 9932", "expiry": "10/27", "cvv": "526", "name": "", "address": "", "country": "ES"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "4233 3395 1050 8682", "expiry": "07/26", "cvv": "145", "name": "", "address": "", "country": "US"},
    {"number": "4437 0402 1988 6016", "expiry": "12/25", "cvv": "181", "name": "Randy Akers", "address": "1066 Carman Lane, Eugene, OR, 97405", "country": "US"},
    {"number": "4233 3395 1050 8682", "expiry": "07/26", "cvv": "145", "name": "", "address": "", "country": "US"},
    {"number": "4921 9000 9901 2357", "expiry": "11/25", "cvv": "485", "name": "", "address": "", "country": "ES"},
    {"number": "4747 1686 8777 1846", "expiry": "08/26", "cvv": "631", "name": "", "address": "", "country": "US"},
    {"number": "4335 6767 9990 5300", "expiry": "10/25", "cvv": "368", "name": "Michael Phipps", "address": "2312 Tanglewood Dr, Glenwood Springs, CO, 81601", "country": "US"},
    {"number": "5333 9010 5713 9423", "expiry": "11/26", "cvv": "919", "name": "", "address": "", "country": "IT"},
    {"number": "5312 3450 0988 7654", "expiry": "05/26", "cvv": "290", "name": "", "address": "", "country": "IT"},
    {"number": "5210 4567 8765 4321", "expiry": "07/27", "cvv": "789", "name": "", "address": "", "country": "IT"},
    {"number": "4234 5689 1234 5678", "expiry": "09/28", "cvv": "456", "name": "", "address": "", "country": "IT"},
    {"number": "4241 0396 7604 3403", "expiry": "05/25", "cvv": "580", "name": "", "address": "", "country": "ES"},
    {"number": "4187 8820 0194 4903", "expiry": "06/28", "cvv": "441", "name": "", "address": "", "country": "ES"},
    {"number": "4147 0013 3000 0000", "expiry": "11/24", "cvv": "667", "name": "", "address": "", "country": "ES"},
    {"number": "4219 4000 0245 4560", "expiry": "09/26", "cvv": "173", "name": "", "address": "", "country": "ES"},
    {"number": "4539 4233 2425 7280", "expiry": "05/27", "cvv": "477", "name": "", "address": "", "country": "ES"},
    {"number": "4451 8023 3456 7890", "expiry": "03/26", "cvv": "732", "name": "", "address": "", "country": "US"},
    {"number": "4187 8820 0194 4903", "expiry": "06/28", "cvv": "441", "name": "", "address": "", "country": "ES"},
    {"number": "5144 0316 8894 3282", "expiry": "08/28", "cvv": "240", "name": "", "address": "", "country": "US"},
    {"number": "5397 6800 1871 2512", "expiry": "03/28", "cvv": "438", "name": "Clemens Lockman", "address": "22871 21 Mile Rd, Michigan, Macomb, 48044", "country": "US"},
    {"number": "4199 5478 7456 8921", "expiry": "06/27", "cvv": "995", "name": "", "address": "", "country": "ES"},
    {"number": "5333 9010 5713 9423", "expiry": "11/26", "cvv": "919", "name": "", "address": "", "country": "IT"},
    {"number": "4895 3282 9422 7685", "expiry": "07/27", "cvv": "142", "name": "", "address": "", "country": "IT"},
    {"number": "4484 3465 2356 8745", "expiry": "11/25", "cvv": "111", "name": "", "address": "", "country": "IT"},
    {"number": "5164 1791 2330 7985", "expiry": "05/27", "cvv": "099", "name": "", "address": "", "country": "IT"},
    {"number": "4562 7773 6123 4557", "expiry": "09/27", "cvv": "900", "name": "", "address": "", "country": "IT"},
    {"number": "4093 3370 6221 0976", "expiry": "12/26", "cvv": "624", "name": "", "address": "", "country": "IT"},
    {"number": "4241 0396 7604 3403", "expiry": "05/25", "cvv": "580", "name": "", "address": "", "country": "ES"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "4234 5689 1234 5678", "expiry": "09/28", "cvv": "456", "name": "", "address": "", "country": "IT"},
    {"number": "4716 6580 3101 4433", "expiry": "11/25", "cvv": "871", "name": "", "address": "", "country": "ES"},
    {"number": "4782 5455 4256 9932", "expiry": "10/27", "cvv": "526", "name": "", "address": "", "country": "ES"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "5196 2384 7587 6431", "expiry": "04/28", "cvv": "586", "name": "Sarah Miller", "address": "1234 Elm St, New York, NY, 10001", "country": "US"},
    {"number": "4233 3395 1050 8682", "expiry": "07/26", "cvv": "145", "name": "", "address": "", "country": "US"},
    {"number": "5333 9010 5713 9423", "expiry": "11/26", "cvv": "919", "name": "", "address": "", "country": "IT"},
    {"number": "5196 2384 7587 6431", "expiry": "04/28", "cvv": "586", "name": "Sarah Miller", "address": "1234 Elm St, New York, NY, 10001", "country": "US"},
    {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"},
    {"number": "5238 4934 3845 1871", "expiry": "02/26", "cvv": "207", "name": "", "address": "", "country": "US"},
    {"number": "4725 9382 7406 2083", "expiry": "11/25", "cvv": "957", "name": "", "address": "", "country": "US"},
    {"number": "5144 0316 8894 3282", "expiry": "08/28", "cvv": "240", "name": "", "address": "", "country": "US"},
    {"number": "5210 4567 8765 4321", "expiry": "07/27", "cvv": "789", "name": "", "address": "", "country": "IT"},
    {"number": "4233 3395 1050 8682", "expiry": "07/26", "cvv": "145", "name": "", "address": "", "country": "US"},
    {"number": "5411 6666 6666 6666", "expiry": "10/26", "cvv": "888", "name": "Roger Smith", "address": "7890 5th Ave, New York, NY, 10003", "country": "US"},
    {"number": "4562 7773 6123 4557", "expiry": "09/27", "cvv": "900", "name": "", "address": "", "country": "IT"},
    {"number": "5210 4567 8765 4321", "expiry": "07/27", "cvv": "789", "name": "", "address": "", "country": "IT"},
    {"number": "4147 0013 3000 0000", "expiry": "11/24", "cvv": "667", "name": "", "address": "", "country": "ES"},
    {"number": "4921 9000 9901 2357", "expiry": "11/25", "cvv": "485", "name": "", "address": "", "country": "ES"},
    {"number": "5312 3450 0988 7654", "expiry": "05/26", "cvv": "290", "name": "", "address": "", "country": "IT"},
    {"number": "5164 1791 2330 7985", "expiry": "05/27", "cvv": "099", "name": "", "address": "", "country": "IT"},
    {"number": "4539 4233 2425 7280", "expiry": "05/27", "cvv": "477", "name": "", "address": "", "country": "ES"},
    {"number": "5247 3772 1168 8502", "expiry": "01/26", "cvv": "117", "name": "", "address": "", "country": "ES"},
    {"number": "4716 6580 3101 4433", "expiry": "11/25", "cvv": "871", "name": "", "address": "", "country": "ES"},
   {"number": "4532 4122 1678 5204", "expiry": "01/27", "cvv": "690", "name": "", "address": "", "country": "ES"}
]

# Cooldown tracking dictionary
USER_REFRESH_TIMES = {}
COOLDOWN_PERIOD = 24 * 60 * 60  # 24 hours in seconds

# Function to get random CC
def get_random_cc():
    return random.choice(CC_DETAILS)

# Function to check cooldown
def is_cooldown_expired(user_id):
    last_refresh = USER_REFRESH_TIMES.get(user_id, 0)
    return (time.time() - last_refresh) > COOLDOWN_PERIOD

# Function to set the user's refresh time
def set_refresh_time(user_id):
    USER_REFRESH_TIMES[user_id] = time.time()

# Command handler for /cc
@Client.on_message(filters.command("cc") & filters.private)
async def handle_cc(client, message):
    user_id = message.from_user.id
    logger.info(f"User {user_id} requested a CC")

    # Generate random CC
    cc = get_random_cc()
    cc_text = (f"**Card Number**: {cc['number']}\n"
               f"**Expiry**: {cc['expiry']}\n"
               f"**CVV**: {cc['cvv']}\n"
               f"**Country**: {cc['country']}")
    
    # Create inline keyboard for refresh
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Refresh", callback_data="refresh_cc")],
        [InlineKeyboardButton("💳 Get Unlimited CCs (Crypto)", callback_data="get_subscription")]
    ])
    
    await message.reply_text(cc_text, reply_markup=keyboard)

# Callback query handler for refresh button
@Client.on_callback_query(filters.regex("refresh_cc"))
async def refresh_cc(client, callback_query):
    user_id = callback_query.from_user.id

    if not is_cooldown_expired(user_id):
        # Alert user if refresh is on cooldown
        await callback_query.answer("Next refresh available in 24 hours.", show_alert=True)
        return

    # Reset the refresh cooldown
    set_refresh_time(user_id)

    # Send new random CC
    cc = get_random_cc()
    cc_text = (f"**Card Number**: {cc['number']}\n"
               f"**Expiry**: {cc['expiry']}\n"
               f"**CVV**: {cc['cvv']}\n"
               f"**Country**: {cc['country']}")

    # Edit the message with the new CC
    await callback_query.message.edit_text(cc_text, reply_markup=callback_query.message.reply_markup)

# Callback query handler for subscription button
@Client.on_callback_query(filters.regex("get_subscription"))
async def get_subscription(client, callback_query):
    subscription_text = (
        "**Subscription Plans:**\n"
        "1. Basic: 1 week unlimited CC refresh - $5 (crypto)\n"
        "2. Standard: 1 month unlimited CC refresh - $15 (crypto)\n"
        "3. Premium: 3 months unlimited CC refresh - $40 (crypto)\n"
        "Contact support to pay in Bitcoin, Ethereum, or USDT."
    )
    
    await callback_query.message.edit_text(subscription_text)
    await callback_query.answer("Contact support for more info!", show_alert=True)
