from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from pymongo import MongoClient


SPOTIFY_API_URL = "https://spotify-downloader9.p.rapidapi.com/downloadPlaylist"
SPOTIFY_HEADERS = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
    "x-rapidapi-host": "spotify-downloader9.p.rapidapi.com"
}

# MongoDB connection setup
client = MongoClient("mongodb+srv://fdtekkz7:UIkt5bnklfYmXphA@cluster0.au15t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Change to your MongoDB connection string if needed
db = client["spotify_bot"]
collection = db["playlists"]  # Collection for storing playlist data

# Function to fetch playlist details and songs from Spotify API
def get_playlist_songs(playlist_url):
    querystring = {"playlistId": playlist_url}
    response = requests.get(SPOTIFY_API_URL, headers=SPOTIFY_HEADERS, params=querystring)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return data.get("data", {}).get("songs", []), data.get("data", {}).get("playlistDetails", {})
    return [], {}

# Helper function to create the song buttons and navigation
def create_song_buttons(songs, offset, limit=10):
    buttons = []
    for song in songs[offset:offset + limit]:
        song_title = song.get("title")
        download_link = song.get("downloadLink")
        buttons.append([InlineKeyboardButton(f"{song_title}", url=download_link)])
    
    # Add navigation buttons
    navigation_buttons = []
    if offset + limit < len(songs):
        navigation_buttons.append(InlineKeyboardButton("Next", callback_data=f"next_{offset + limit}"))
    if offset > 0:
        navigation_buttons.append(InlineKeyboardButton("Previous", callback_data=f"prev_{offset - limit}"))

    if navigation_buttons:
        buttons.append(navigation_buttons)
    
    return InlineKeyboardMarkup(buttons)

# Function to store playlist data in MongoDB
def store_playlist(chat_id, playlist_url, songs, details):
    collection.update_one(
        {"chat_id": chat_id, "playlist_url": playlist_url},
        {"$set": {"songs": songs, "details": details}},
        upsert=True
    )

# Function to retrieve playlist data from MongoDB
def get_stored_playlist(chat_id, playlist_url):
    playlist_data = collection.find_one({"chat_id": chat_id, "playlist_url": playlist_url})
    if playlist_data:
        return playlist_data.get("songs", []), playlist_data.get("details", {})
    return [], {}

@app.on_message(filters.command("playlist"))
def send_playlist(client, message):
    # Get playlist URL from user message
    try:
        playlist_url = message.text.split(" ")[1]
    except IndexError:
        message.reply_text("Please provide a Spotify playlist URL after the command.")
        return

    # Fetch playlist data from Spotify API
    songs, playlist_details = get_playlist_songs(playlist_url)
    if not songs:
        message.reply_text("Could not retrieve the playlist. Please make sure the URL is correct.")
        return

    # Store the playlist data in MongoDB
    chat_id = message.chat.id
    store_playlist(chat_id, playlist_url, songs, playlist_details)

    # Send playlist cover and first 10 songs
    playlist_title = playlist_details.get("title", "Unknown Playlist")
    playlist_cover = playlist_details.get("cover", "")
    playlist_artist = playlist_details.get("artist", "Unknown Artist")

    message.reply_photo(
        playlist_cover,
        caption=f"**Playlist:** {playlist_title}\n**Artist:** {playlist_artist}",
        reply_markup=create_song_buttons(songs, 0)
    )

# Callback handler for pagination (next/prev)
@app.on_callback_query(filters.regex(r"next_\d+|prev_\d+"))
def paginate_songs(client, callback_query):
    # Extract the offset from the callback data
    offset = int(callback_query.data.split("_")[1])

    # Retrieve the stored playlist data from MongoDB
    chat_id = callback_query.message.chat.id
    # We can get the playlist URL by checking the stored playlist data for this chat
    playlist_url = collection.find_one({"chat_id": chat_id}).get("playlist_url")
    
    songs, _ = get_stored_playlist(chat_id, playlist_url)

    # Edit message with updated list of songs
    callback_query.message.edit_reply_markup(reply_markup=create_song_buttons(songs, offset))


