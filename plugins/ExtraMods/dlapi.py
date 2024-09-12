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

    # Special case for Pinterest URLs
    if "pinterest" in url.lower():
        await message.reply_text("For Pinterest downloads, use the /pinterest command.")
        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"Pinterest URL detected. Redirected user [{user.first_name}](tg://user?id={user.id}) to /pinterest."
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
    """Handle YouTube video download with inline buttons."""
    title = video_data.get("title", "YouTube Video")
    videos = video_data.get("videos", [])
    thumb_url = video_data.get("thumb")
    user = message.from_user

    buttons = []
    for i, video in enumerate(videos[:7]):  # Limit to 0-6
        quality = video.get("quality")
        size = video.get("size")
        dlink = video.get("dlink")
        buttons.append([InlineKeyboardButton(f"{quality} ({size})", url=dlink)])

    keyboard = InlineKeyboardMarkup(buttons)
    await client.send_photo(
        chat_id=message.chat.id,
        photo=thumb_url,
        caption=f"**{title}**\n\nSelect your preferred video quality:",
        reply_markup=keyboard
    )

    # Log the YouTube video details
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"Sent YouTube video to [{user.first_name}](tg://user?id={user.id})\nTitle: {title}\nURL: {video_data['id']}"
    )

async def handle_instagram(client, message, video_data):
    """Handle Instagram video download."""
    caption = video_data.get("caption", "Instagram Reel")
    video_url = video_data.get("download_url")
    thumb_url = video_data.get("thumb")
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
    thumb_url = video_data.get("thumb")
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
