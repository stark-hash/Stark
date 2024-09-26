import requests
import os
from pyrogram import Client, filters

# Replace these with your actual API keys and RapidAPI host details
RAPIDAPI_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
RAPIDAPI_HOST = "spotify-downloader9.p.rapidapi.com"

# Function to download song metadata and get the download link and cover image
def get_song_metadata(song_url):
    api_url = "https://spotify-downloader9.p.rapidapi.com/downloadSong"
    querystring = {"songId": song_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    response = requests.get(api_url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            song_data = data["data"]
            download_link = song_data.get("downloadLink")
            cover_link = song_data.get("cover")
            title = song_data["title"]
            return download_link, cover_link, title, response.status_code
        else:
            return None, None, None, response.status_code
    else:
        return None, None, None, response.status_code

# Function to download the song from the download link
def download_song(download_link, song_title):
    response = requests.get(download_link)
    if response.status_code == 200:
        file_name = f"{song_title}.mp3"
        with open(file_name, "wb") as f:
            f.write(response.content)
        return file_name
    return None

# Function to download the cover image
def download_cover(cover_link, song_title):
    response = requests.get(cover_link)
    if response.status_code == 200:
        file_name = f"{song_title}_cover.jpg"
        with open(file_name, "wb") as f:
            f.write(response.content)
        return file_name
    return None

# Create the Pyrogram handler for song download and sending
@Client.on_message(filters.command("downloadsong") & filters.private)
async def download_song_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a Spotify track URL.")
        return

    song_url = message.command[1]
    await message.reply_text(f"Fetching download link for: {song_url}")

    download_link, cover_link, song_title, status_code = get_song_metadata(song_url)

    if download_link and cover_link:
        await message.reply_text(f"Downloading song: {song_title}")
        
        # Download the song file
        song_file_name = download_song(download_link, song_title)
        cover_file_name = download_cover(cover_link, song_title)

        if song_file_name and cover_file_name:
            # Send the cover photo
            await client.send_photo(message.chat.id, cover_file_name, caption=f"Cover of '{song_title}'")
            
            # Send the song file to the user
            await client.send_audio(message.chat.id, song_file_name)
            
            # Clean up by deleting the files after sending
            os.remove(song_file_name)
            os.remove(cover_file_name)
        else:
            await message.reply_text("Failed to download the song or cover file.")
    else:
        await message.reply_text(f"Failed to fetch download link or cover. Response Code: {status_code}")


