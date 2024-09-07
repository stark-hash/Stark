import logging
from pyrogram import Client, filters
import requests
import re
import os

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Function to fetch video info from the RapidAPI service
def fetch_video_info(video_id):
    url = "https://yt-api.p.rapidapi.com/dl"
    querystring = {"id": video_id}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,  # Make sure to set your RAPIDAPI_KEY
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        logger.info(f"Fetched video info for video ID: {video_id}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching video info for video ID: {video_id} - {e}")
        return None

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
            logger.info(f"Extracted video ID: {video_id} from URL: {url}")
            break
    if not video_id:
        logger.warning(f"Failed to extract video ID from URL: {url}")
    return video_id

@Client.on_message(filters.command("vvideo") & filters.private)
async def handle_video(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /video <YouTube URL>")
        logger.warning("Invalid command usage.")
        return

    video_url = message.command[1]
    video_id = extract_video_id(video_url)

    if video_id:
        video_info = fetch_video_info(video_id)

        if not video_info:
            await message.reply_text("Error fetching video info.")
            logger.error(f"Failed to retrieve video info for ID: {video_id}")
            return
        
        title = video_info.get("title", "No Title Available")
        description = video_info.get("description", "No Description Available")
        video_file_url = video_info.get("formats")[0].get("url") if video_info.get("formats") else None

        if video_file_url:
            logger.info(f"Starting download for video ID: {video_id}")
            try:
                # Download the video file locally
                video_response = requests.get(video_file_url)
                video_response.raise_for_status()

                video_filename = f"{video_id}.mp4"
                with open(video_filename, "wb") as video_file:
                    video_file.write(video_response.content)
                logger.info(f"Downloaded video ID: {video_id}")

                # Send the video file to the user
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_filename,
                    caption=f"Title: {title}\nDescription: {description}"
                )
                logger.info(f"Sent video: {video_filename} to user: {message.chat.id}")

                # Clean up the downloaded video file
                os.remove(video_filename)
                logger.info(f"Removed local file: {video_filename}")

            except requests.exceptions.RequestException as e:
                logger.error(f"Error downloading video file for video ID: {video_id} - {e}")
                await message.reply_text("Error downloading the video.")
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                await message.reply_text("An error occurred while processing the video.")
        else:
            await message.reply_text("No video URL found.")
            logger.warning(f"No video URL found for video ID: {video_id}")
    else:
        await message.reply_text("Invalid YouTube URL")
        logger.warning("User provided an invalid YouTube URL")

