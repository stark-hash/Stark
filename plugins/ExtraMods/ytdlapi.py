from pyrogram import Client, filters
import requests
import re
import os

# Function to fetch video info from the RapidAPI service
def fetch_video_info(video_id):
    url = "https://yt-api.p.rapidapi.com/dl"
    querystring = {"id": video_id}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,  # Make sure to set your RAPIDAPI_KEY
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Function to extract the YouTube video ID from a URL
def extract_video_id(url):
    """Extracts video ID from a YouTube URL."""
    video_id = None
    patterns = [
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?v%3D|watch\?v=)([0-9A-Za-z_-]{11})",
        r"youtube\.com\/(?:shorts\/|channel\/|user\/)(?:[A-Za-z0-9-_]{1,100}\/)?([0-9A-Za-z_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            break
    return video_id

@Client.on_message(filters.command("video") & filters.private)
async def handle_video(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /video <YouTube URL>")
        return

    video_url = message.command[1]
    video_id = extract_video_id(video_url)

    if video_id:
        video_info = fetch_video_info(video_id)
        
        title = video_info.get("title", "No Title Available")
        description = video_info.get("description", "No Description Available")
        video_file_url = video_info.get("formats")[0].get("url") if video_info.get("formats") else None

        if video_file_url:
            # Download the video file locally
            video_response = requests.get(video_file_url)
            video_filename = f"{video_id}.mp4"

            with open(video_filename, "wb") as video_file:
                video_file.write(video_response.content)
            
            # Send the video file to the user
            await client.send_video(
                chat_id=message.chat.id,
                video=video_filename,
                caption=f"Title: {title}\nDescription: {description}"
            )

            # Clean up the downloaded video file
            os.remove(video_filename)
        else:
            await message.reply_text("No video URL found.")
    else:
        await message.reply_text("Invalid YouTube URL")
