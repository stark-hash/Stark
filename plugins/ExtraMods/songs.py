import os
import requests
from pyrogram import Client, filters
from info import LOG_CHANNEL  # Ensure this is correctly set up

# Your RapidAPI key and host
API_HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",
    "x-rapidapi-host": "spotify-downloader9.p.rapidapi.com"
}
MAX_SONGS_LIMIT = 20  # Maximum number of songs to download

# ASCII progress bar function
def show_loading_bar(percent_complete):
    progress_length = 30
    bar_length = int((percent_complete / 100) * progress_length)
    bar = '█' * bar_length + '-' * (progress_length - bar_length)
    print(f"[{bar}] {percent_complete:.2f}%", end='\r')

def download_file(url, file_name):
    """Download a file with an ASCII loading bar."""
    try:
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('content-length', 0))
        
        with open(file_name, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent_complete = (downloaded / total_length) * 100
                    show_loading_bar(percent_complete)
        print(f"\nDownload complete: {file_name}")
        return file_name
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None

def fetch_album_data(album_id):
    """Fetch album data from the Spotify downloader API."""
    url = "https://spotify-downloader9.p.rapidapi.com/downloadAlbum"
    querystring = {"albumId": album_id}
    response = requests.get(url, headers=API_HEADERS, params=querystring)
    return response.json()

def fetch_playlist_data(playlist_id):
    """Fetch playlist data from the Spotify downloader API."""
    url = "https://spotify-downloader9.p.rapidapi.com/downloadPlaylist"
    querystring = {"playlistId": playlist_id}
    response = requests.get(url, headers=API_HEADERS, params=querystring)
    return response.json()

def fetch_song_data(song_id):
    """Fetch song data from the Spotify downloader API."""
    url = "https://spotify-downloader9.p.rapidapi.com/downloadSong"
    querystring = {"songId": song_id}
    response = requests.get(url, headers=API_HEADERS, params=querystring)
    return response.json()

@Client.on_message(filters.command("downloadalbum") & filters.private)
async def handle_album_download(client, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Usage: /downloadalbum <ALBUM_URL>")
            return

        album_id = message.command[1]
        user = message.from_user

        # Log the request
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"New album download request from [{user.first_name}](tg://user?id={user.id})\nAlbum ID: {album_id}"
        )

        # Fetch album data
        album_data = fetch_album_data(album_id)
        
        if not album_data or album_data.get("error"):
            await message.reply_text("Unable to fetch album details.")
            await client.send_message(
                chat_id=LOG_CHANNEL,
                text=f"Error: Could not fetch album details for Album ID: {album_id} by [{user.first_name}](tg://user?id={user.id})"
            )
            return

        album_details = album_data.get("albumDetails", {})
        album_title = album_details.get("title", "Unknown Title")
        artist = album_details.get("artist", "Unknown Artist")
        cover_url = album_details.get("cover", "")
        release_date = album_details.get("releaseDate", "Unknown Date")
        songs = album_data.get("songs", [])

        # Check if the album exceeds the song limit
        if len(songs) > MAX_SONGS_LIMIT:
            await message.reply_text(
                f"The album contains more than {MAX_SONGS_LIMIT} songs. Please upgrade your account."
            )
            return

        # Send album basic details and cover image
        await client.send_photo(
            chat_id=message.chat.id,
            photo=cover_url,
            caption=f"**Album:** {album_title}\n**Artist:** {artist}\n**Release Date:** {release_date}\n\nStarting download of songs..."
        )

        # Download and send each song in the album
        for song in songs:
            song_title = song.get("title", "Unknown Song").replace(' ', '_') + ".mp3"
            download_url = song.get("downloadLink", "")

            # Download the song
            file_path = download_file(download_url, song_title)

            if file_path:
                # Send the song to the user
                await client.send_audio(
                    chat_id=message.chat.id,
                    audio=file_path,
                    caption=f"**{song.get('title')}** - {artist}"
                )

                # Remove the file after sending
                os.remove(file_path)

        # Log the album download completion
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Completed sending album [{album_title}] to [{user.first_name}](tg://user?id={user.id})"
        )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error in handle_album_download: {e}")

@Client.on_message(filters.command("downloadplaylist") & filters.private)
async def handle_playlist_download(client, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Usage: /downloadplaylist <PLAYLIST_URL>")
            return

        playlist_id = message.command[1]
        user = message.from_user

        # Log the request
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"New playlist download request from [{user.first_name}](tg://user?id={user.id})\nPlaylist ID: {playlist_id}"
        )

        # Fetch playlist data
        playlist_data = fetch_playlist_data(playlist_id)

        if not playlist_data or playlist_data.get("error"):
            await message.reply_text("Unable to fetch playlist details.")
            return

        playlist_title = playlist_data.get("playlistTitle", "Unknown Playlist")
        songs = playlist_data.get("songs", [])

        # Check if the playlist exceeds the song limit
        if len(songs) > MAX_SONGS_LIMIT:
            await message.reply_text(
                f"The playlist contains more than {MAX_SONGS_LIMIT} songs. Please upgrade your account."
            )
            return

        # Download and send each song in the playlist
        for song in songs:
            song_title = song.get("title", "Unknown Song").replace(' ', '_') + ".mp3"
            download_url = song.get("downloadLink", "")

            # Download the song
            file_path = download_file(download_url, song_title)

            if file_path:
                # Send the song to the user
                await client.send_audio(
                    chat_id=message.chat.id,
                    audio=file_path,
                    caption=f"**{song.get('title')}** - {song.get('artist', 'Unknown Artist')}"
                )

                # Remove the file after sending
                os.remove(file_path)

        # Log the playlist download completion
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Completed sending playlist [{playlist_title}] to [{user.first_name}](tg://user?id={user.id})"
        )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error in handle_playlist_download: {e}")

@Client.on_message(filters.command("downloadsong") & filters.private)
async def handle_song_download(client, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Usage: /downloadsong <SONG_URL>")
            return

        song_id = message.command[1]
        user = message.from_user

        # Log the request
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"New song download request from [{user.first_name}](tg://user?id={user.id})\nSong ID: {song_id}"
        )

        # Fetch song data
        song_data = fetch_song_data(song_id)

        if not song_data or song_data.get("error"):
            await message.reply_text("Unable to fetch song details.")
            return

        song_title = song_data.get("title", "Unknown Song").replace(' ', '_') + ".mp3"
        download_url = song_data.get("downloadLink", "")

        # Download the song
        file_path = download_file(download_url, song_title)

        if file_path:
            # Send the song to the user
            await client.send_audio(
                chat_id=message.chat.id,
                audio=file_path,
                caption=f"**{song_data.get('title')}** - {song_data.get('artist', 'Unknown Artist')}"
            )

            # Remove the file after sending
            os.remove(file_path)

            # Log the song download completion
            await client.send_message(
                chat_id=LOG_CHANNEL,
                text=f"Completed sending song [{song_data.get('title')}] to [{user.first_name}](tg://user?id={user.id})"
            )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error in handle_song_download: {e}")

