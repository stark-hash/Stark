import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import LOG_CHANNEL  # Import the LOG_CHANNEL from the info module

# API details for Facebook Downloader
FB_API_URL = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"
FB_HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",
    "x-rapidapi-host": "facebook-reel-and-video-downloader.p.rapidapi.com"
}

def fetch_facebook_video_data(url):
    """Fetch video data from Facebook using the downloader API."""
    querystring = {"url": url}
    response = requests.get(FB_API_URL, headers=FB_HEADERS, params=querystring)
    return response.json()

@Client.on_message(filters.command("fb") & filters.private)
async def handle_fb_download(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /fbdownload <Facebook Video URL>")
        return

    url = message.command[1]
    user = message.from_user

    # Log the request
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"New Facebook download request from [{user.first_name}](tg://user?id={user.id})\nURL: {url}"
    )

    # Fetch video data from the downloader API
    video_data = fetch_facebook_video_data(url)

    if not video_data or not video_data.get("success"):
        await message.reply_text("Unable to fetch video details from Facebook.")
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Error: Could not fetch Facebook video details for URL: {url} by [{user.first_name}](tg://user?id={user.id})"
        )
        return

    # Extract video details
    title = video_data.get("title", "Facebook Video")
    low_quality_url = video_data["links"].get("Download Low Quality")
    high_quality_url = video_data["links"].get("Download High Quality")

    if not low_quality_url:
        await message.reply_text("Low-quality video not found.")
        return

    # Download the low-quality video
    response = requests.get(low_quality_url)
    file_name = f"{title}.mp4"
    
    with open(file_name, "wb") as file:
        file.write(response.content)

    # Prepare inline keyboard button for high-quality download
    if high_quality_url:
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Download High Quality", url=high_quality_url)]]
        )
    else:
        keyboard = None

    # Send the low-quality video to the user with an inline button for high quality
    await client.send_video(
        chat_id=message.chat.id,
        video=file_name,
        caption=f"**{title}**\nHere is your downloaded Facebook video.",
        reply_markup=keyboard
    )

    # Delete the file after sending
    os.remove(file_name)

    # Log the successful download
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"Sent low-quality Facebook video to [{user.first_name}](tg://user?id={user.id})\nTitle: {title}"
    )
