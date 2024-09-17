import random
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from info import LOG_CHANNEL  # Assumes LOG_CHANNEL is configured in info.py

API_URL = "https://www.deckofcardsapi.com/api/deck/"
HIDDEN_CARD_IMAGE = "https://path-to-your-hidden-card-image.png"  # Provide your hidden card image

# A dictionary to store each user's current deck ID and card to guess
user_game_data = {}


# Start a guessing game
@Client.on_message(filters.command("guess"))
async def start_guessing_game(client, message):
    user_id = message.from_user.id

    # Shuffle a new deck
    response = requests.get(f"{API_URL}new/shuffle/?deck_count=1")
    data = response.json()

    if data['success']:
        deck_id = data['deck_id']

        # Draw one random card from the deck
        draw_response = requests.get(f"{API_URL}{deck_id}/draw/?count=1")
        draw_data = draw_response.json()

        if draw_data['success']:
            card = draw_data['cards'][0]
            card_value = card['value']
            card_image = card['image']

            # Store the card details for the user
            user_game_data[user_id] = {
                "deck_id": deck_id,
                "card_value": card_value,
                "card_image": card_image
            }

            # Generate random options including the correct card value
            all_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
            random_values = random.sample(all_values, 5)  # Pick 5 random card values
            if card_value not in random_values:
                random_values[random.randint(0, 4)] = card_value  # Ensure the correct card value is in the options

            # Create buttons with the card values
            buttons = [
                [InlineKeyboardButton(text=value, callback_data=f"guess:{value}") for value in random_values[:3]],
                [InlineKeyboardButton(text=value, callback_data=f"guess:{value}") for value in random_values[3:]]
            ]

            # Send the hidden card and options to guess
            await message.reply_photo(
                photo=HIDDEN_CARD_IMAGE,
                caption="Guess the card value!",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            await message.reply("Failed to draw a card. Please try again.")
    else:
        await message.reply("Failed to shuffle the deck. Please try again.")

# Handle button press for guessing
@Client.on_callback_query(filters.regex(r"^guess:"))
async def handle_guess(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id

    if user_id not in user_game_data:
        await callback_query.answer("No active game. Please start with /guess.", show_alert=True)
        return

    guessed_value = callback_query.data.split(":")[1]
    actual_card = user_game_data[user_id]

    # Check if the guessed value is correct
    if guessed_value == actual_card['card_value']:
        # Correct guess, reveal the card
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=actual_card['card_image'])
        )
        await callback_query.message.reply(f"🎉 Congratulations! You guessed it right. The card was {actual_card['card_value']}.")
    else:
        # Incorrect guess, reveal the card
        await callback_query.edit_message_media(
            media=InputMediaPhoto(media=actual_card['card_image'])
        )
        await callback_query.message.reply(f"❌ Oops! Incorrect guess. The card was {actual_card['card_value']}.")

    # Log the game event
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"User {callback_query.from_user.username} ({callback_query.from_user.id}) guessed {guessed_value}. The card was {actual_card['card_value']}."
    )

    # Remove the game data for the user
    del user_game_data[user_id]


