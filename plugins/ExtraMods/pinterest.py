import requests
import logging
from pyrogram import Client, filters, enums
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# API details
API_URL = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/server"
HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",  # Replace with your own API key
    "x-rapidapi-host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com",
    "Content-Type": "application/json"
}

def fetch_pinterest_content(pinterest_url):
    """Fetch Pinterest content using the API."""
    logger.info(f"Fetching Pinterest content for URL: {pinterest_url}")
    
    payload = {"id": pinterest_url}
    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for bad HTTP responses
        logger.info(f"Received response: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching Pinterest content: {e}")
        return None

def download_video(video_url, video_path):
    """Download video from the given URL."""
    logger.info(f"Downloading video from URL: {video_url}")
    
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad HTTP responses
        
        with open(video_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        logger.info(f"Downloaded video to: {video_path}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading video: {e}")

@Client.on_message(filters.command("pinterest") & filters.private)
async def handle_pinterest(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /pinterest <Pinterest URL>")
        return

    pinterest_url = message.command[1]
    logger.info(f"Processing Pinterest URL: {pinterest_url}")
    
    pinterest_data = fetch_pinterest_content(pinterest_url)

    if not pinterest_data or not pinterest_data.get("data"):
        logger.error(f"Invalid Pinterest data received: {pinterest_data}")
        await message.reply_text("Unable to fetch details from Pinterest.")
        return

    # Extract data from the response
    data = pinterest_data["data"]
    title = data.get("title", "No Title Available")
    videos = data.get("stories")[0]["video"]["video_list"] if data.get("stories") else None
    image_url = data.get("image_medium_url")
    
    if videos:
        logger.info("Video found in Pinterest data.")
        
        video_url = videos["V_EXP3"]["url"]  # Picking the mp4 version (you can change it based on preference)
        video_path = f"{message.chat.id}_pinterest_video.mp4"
        download_video(video_url, video_path)

        # Send the video
        try:
            await client.send_video(
                chat_id=message.chat.id,
                video=video_path,
                caption=f"{title}\n[Download Video]({video_url})",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            logger.info(f"Video sent to chat: {message.chat.id}")
        except Exception as e:
            logger.error(f"Error sending video: {e}")
        finally:
            # Clean up: Remove the video file after sending
            if os.path.exists(video_path):
                os.remove(video_path)
                logger.info(f"Deleted video file: {video_path}")
    else:
        logger.info("No video found. Sending image.")
        
        # Send the image
        try:
            await client.send_photo(
                chat_id=message.chat.id,
                photo=image_url,
                caption=f"{title}\n[View Image]({image_url})",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            logger.info(f"Image sent to chat: {message.chat.id}")
        except Exception as e:
            logger.error(f"Error sending image: {e}")
