import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import LOG_CHANNEL  # Import the LOG_CHANNEL from the info module

# API details
RAPIDAPI_URL = "https://full-downloader-social-media.p.rapidapi.com/"
HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",
    "x-rapidapi-host": "full-downloader-social-media.p.rapidapi.com"
}

MAX_FILE_SIZE = 200 * 1024 * 1024  # 200 MB limit

def fetch_video_data(url):
    """Fetch video data using the downloader API."""
    querystring = {"url": url}
    response = requests.get(RAPIDAPI_URL, headers=HEADERS, params=querystring)
    return response.json()

@Client.on_message(filters.command("download") & filters.private)
async def handle_download(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /download <URL>")
        return

    url = message.command[1]
    user = message.from_user

    # Log the request
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"New download request from [{user.first_name}](tg://user?id={user.id})\nURL: {url}"
    )

    # Blacklist for Pinterest and Pin URLs
    if "pinterest" in url.lower() or "pin" in url.lower():
        await message.reply_text("For Pinterest downloads, use the /pinterest command.")
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Pinterest/Pin URL detected. Redirected user [{user.first_name}](tg://user?id={user.id}) to /pinterest."
        )
        return

    # Fetch data from the downloader API
    video_data = fetch_video_data(url)

    if not video_data or video_data.get("error"):
        await message.reply_text("Unable to fetch video details.")
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Error: Could not fetch details for URL: {url} by [{user.first_name}](tg://user?id={user.id})"
        )
        return

    hosting = video_data.get("hosting")
    if hosting == "youtube":
        await handle_youtube(client, message, video_data)
    elif hosting == "instagram":
        await handle_instagram(client, message, video_data)
    else:
        await handle_other_platform(client, message, video_data)

async def handle_youtube(client, message, video_data):
    """Handle YouTube video download, download 360p if under 200 MB, show buttons for other qualities."""
    title = video_data.get("title", "YouTube Video")
    videos = video_data.get("videos", [])
    user = message.from_user
    download_url_360p = None
    video_size_360p = None

    # Prepare the buttons for other resolutions
    buttons = []

    # Search for the 360p version and also create buttons for other qualities
    for video in videos:
        quality = video.get("quality")
        dlink = video.get("dlink")
        size = video.get("size", "Unknown size")

        # Check if this is the 360p version and get the download link
        if quality == "360p":
            download_url_360p = dlink
            video_size_360p = size
        else:
            # Add buttons for other qualities
            buttons.append([InlineKeyboardButton(f"{quality} ({size})", url=dlink)])

    # Check if the 360p version is found
    if not download_url_360p:
        await message.reply_text("360p version not available for this video.")
        return

    # Check if the 360p video is under 200 MB
    if video_size_360p and video_size_360p.endswith("MB"):
        size_in_mb = float(video_size_360p.replace("MB", "").strip())
        if size_in_mb > 200:
            await message.reply_text("The 360p video is larger than 200 MB and cannot be downloaded.")
            return

    # If 360p is found and within size limit, download the video
    response = requests.get(download_url_360p)
    file_name = f"{title}.mp4"
    with open(file_name, "wb") as file:
        file.write(response.content)

    # Send the video and show buttons for other resolutions
    keyboard = InlineKeyboardMarkup(buttons) if buttons else None
    await client.send_video(
        chat_id=message.chat.id,
        video=file_name,
        caption=f"**{title}**\n\nDownloaded in 360p.",
        reply_markup=keyboard
    )

    # Delete the file after sending
    os.remove(file_name)

    # Log the YouTube video details
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"Sent YouTube video to [{user.first_name}](tg://user?id={user.id})\nTitle: {title}\nURL: {video_data['id']}"
    )

async def handle_instagram(client, message, video_data):
    """Handle Instagram video download."""
    caption = video_data.get("caption", "Instagram Reel")
    video_url = video_data.get("download_url")
    user = message.from_user

    await client.send_video(
        chat_id=message.chat.id,
        video=video_url,
        caption=caption
    )

    # Log the Instagram video details
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"Sent Instagram video to [{user.first_name}](tg://user?id={user.id})\nCaption: {caption}"
    )

async def handle_other_platform(client, message, video_data):
    """Handle videos from TikTok or other platforms."""
    video_url = video_data.get("download_url")
    caption = video_data.get("title", "Video")
    user = message.from_user

    await client.send_video(
        chat_id=message.chat.id,
        video=video_url,
        caption=caption
    )

    # Log the other platform video details
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"Sent video from {video_data['hosting']} to [{user.first_name}](tg://user?id={user.id})\nTitle: {caption}"
    )
