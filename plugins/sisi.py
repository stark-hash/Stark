import random
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Sample list of credit card (CC) details with three fields each
CC_DETAILS = [
    {"number": "4111 1111 1111 1111", "expiry": "12/25", "cvv": "123"},
    {"number": "5555 5555 5555 4444", "expiry": "11/24", "cvv": "456"},
    {"number": "3782 822463 10005", "expiry": "10/23", "cvv": "789"},
    {"number": "6011 0009 9013 9424", "expiry": "01/26", "cvv": "321"},
    {"number": "3530 1113 3330 0000", "expiry": "08/27", "cvv": "654"}
]

# Store user refresh times (user_id -> last refresh timestamp)
USER_REFRESH_TIMES = {}

# Set the cooldown period (24 hours in seconds)
COOLDOWN_PERIOD = 24 * 60 * 60  # 24 hours

def get_random_cc():
    """Return a random CC from the list."""
    return random.choice(CC_DETAILS)

def is_cooldown_expired(user_id):
    """Check if the cooldown period has expired for the given user."""
    last_refresh = USER_REFRESH_TIMES.get(user_id, 0)
    current_time = time.time()
    return (current_time - last_refresh) > COOLDOWN_PERIOD

def set_refresh_time(user_id):
    """Set the current time as the last refresh time for the user."""
    USER_REFRESH_TIMES[user_id] = time.time()

@Client.on_message(filters.command("cc") & filters.private)
async def handle_cc(client, message):
    """Handle the /cc command and send a random CC with a refresh button."""
    user_id = message.from_user.id
    cc = get_random_cc()
    
    # Create the message text with the random CC details
    cc_text = f"**Card Number**: {cc['number']}\n**Expiry Date**: {cc['expiry']}\n**CVV**: {cc['cvv']}"
    
    # Create an inline keyboard with a "Refresh" button
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Refresh", callback_data="refresh_cc")],
        [InlineKeyboardButton("💳 Get Unlimited CCs (Crypto)", callback_data="get_subscription")]
    ])
    
    # Send the CC details with the refresh button
    await message.reply_text(cc_text, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("refresh_cc"))
async def refresh_cc(client, callback_query):
    """Handle the refresh button click to send a new random CC with cooldown and subscription option."""
    user_id = callback_query.from_user.id
    
    # Check if the user is in the cooldown period
    if not is_cooldown_expired(user_id):
        # Show alert if cooldown is not expired
        await callback_query.answer("Next refresh available in 24 hours. Get unlimited CCs with a subscription!", show_alert=True)
        return

    # Update the last refresh time for the user
    set_refresh_time(user_id)
    
    # Send a new random CC
    cc = get_random_cc()
    cc_text = f"**Card Number**: {cc['number']}\n**Expiry Date**: {cc['expiry']}\n**CVV**: {cc['cvv']}"
    
    # Create a new keyboard with the refresh button and subscription option
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Refresh", callback_data="refresh_cc")],
        [InlineKeyboardButton("💳 Get Unlimited CCs (Crypto)", callback_data="get_subscription")]
    ])
    
    # Edit the original message with the new random CC
    await callback_query.message.edit_text(cc_text, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("get_subscription"))
async def get_subscription(client, callback_query):
    """Handle the subscription button click to show subscription options."""
    # Show subscription plans with crypto payments
    subscription_text = """
**Subscription Plans:**
1. 🟢 Basic: 1 week unlimited CC refresh - $5 in crypto
2. 🟡 Standard: 1 month unlimited CC refresh - $15 in crypto
3. 🔵 Premium: 3 months unlimited CC refresh - $40 in crypto

💳 We accept payments via Bitcoin, Ethereum, and USDT.

Please contact our support to process the payment and unlock your subscription!
"""
    # Edit the message to show subscription plans
    await callback_query.message.edit_text(subscription_text)

    # Show an alert (optional)
    await callback_query.answer("Contact us for crypto payments to get unlimited CC refreshes!", show_alert=True)
