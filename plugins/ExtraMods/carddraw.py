import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from info import LOG_CHANNEL  # Assumes LOG_CHANNEL is configured in info.py

API_URL = "https://www.deckofcardsapi.com/api/deck/"

# A dictionary to store each user's current deck ID
user_decks = {}

# Shuffle the deck command
@Client.on_message(filters.command("shuffle"))
async def shuffle_deck(client, message):
    # Call the API to shuffle a new deck
    response = requests.get(f"{API_URL}new/shuffle/?deck_count=1")
    data = response.json()

    if data['success']:
        deck_id = data['deck_id']
        user_decks[message.from_user.id] = deck_id  # Store the deck ID for the user

        # Send message that the deck is shuffled and provide the deck ID
        await message.reply(
            f"🃏 Deck shuffled successfully!\n"
            f"Deck ID: `{deck_id}`\n\n"
            "You can now draw cards using `/draw {number}` (Max 5)."
        )
        
        # Log the shuffle event
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"User {message.from_user.username} ({message.from_user.id}) shuffled a new deck with Deck ID: {deck_id}."
        )
    else:
        await message.reply("❌ Failed to shuffle the deck. Please try again.")

# Draw cards command
@Client.on_message(filters.command("draw"))
async def draw_cards(client, message):
    try:
        # Get the number of cards to draw from the command
        num_cards = int(message.command[1])

        if num_cards < 1 or num_cards > 5:
            await message.reply("Please specify a number between 1 and 5.")
            return

        # Get the user's deck ID
        user_id = message.from_user.id
        if user_id not in user_decks:
            await message.reply("You need to shuffle the deck first using /shuffle.")
            return
        
        deck_id = user_decks[user_id]

        # Call the API to draw cards
        draw_response = requests.get(f"{API_URL}{deck_id}/draw/?count={num_cards}")
        draw_data = draw_response.json()

        if draw_data['success']:
            # Prepare the card images and response text
            cards = draw_data['cards']
            card_images = [card['image'] for card in cards]
            remaining_cards = draw_data['remaining']

            # Send the caption as a message
            await message.reply(
                text=f"Here are your {num_cards} cards:\n" +
                     "\n".join([f"Value: {card['value']} of {card['suit']}" for card in cards]) +
                     f"\n\nRemaining cards in the deck: {remaining_cards}"
            )

            # Send each card image individually
            for card_image in card_images:
                await message.reply_photo(photo=card_image)

            # Log the draw event
            await client.send_message(
                chat_id=LOG_CHANNEL,
                text=f"User {message.from_user.username} ({message.from_user.id}) drew {num_cards} cards from Deck ID: {deck_id}. Remaining cards: {remaining_cards}."
            )
        else:
            await message.reply("Failed to draw cards. Please shuffle the deck again using /shuffle.")
    except (IndexError, ValueError):
        await message.reply("Please provide a valid number of cards to draw, e.g. `/draw 3`.")

