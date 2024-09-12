import requests
from pyrogram import Client, filters
import os

# API details
API_URL = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/server"
HEADERS = {
    "x-rapidapi-key": "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d",  # Replace with your own API key
    "x-rapidapi-host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com",
    "Content-Type": "application/json"
}

def fetch_pinterest_content(pinterest_url):
    """Fetch Pinterest content using the API."""
    payload = {"id": pinterest_url}
    response = requests.post(API_URL, json=payload, headers=HEADERS)
    return response.json()

def download_video(video_url, video_path):
    """Download video from the given URL."""
    response = requests.get(video_url, stream=True)
    with open(video_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

@Client.on_message(filters.command("pinterest") & filters.private)
async def handle_pinterest(client, message):
    if len(message.command) != 2:
        await message.reply_text("Usage: /pinterest <Pinterest URL>")
        return

    pinterest_url = message.command[1]
    pinterest_data = fetch_pinterest_content(pinterest_url)

    if not pinterest_data or not pinterest_data.get("data"):
        await message.reply_text("Unable to fetch details from Pinterest.")
        return

    # Extract data from the response
    data = pinterest_data["data"]
    title = data.get("title", "No Title Available")
    videos = data.get("stories")[0]["video"]["video_list"] if data.get("stories") else None
    image_url = data.get("image_medium_url")
    
    if videos:  # If there is a video, download and send it
        video_url = videos["V_EXP3"]["url"]  # Picking the mp4 version (you can change it based on preference)
        video_path = f"{message.chat.id}_pinterest_video.mp4"
        download_video(video_url, video_path)

        await client.send_video(
            chat_id=message.chat.id,
            video=video_path,
            caption=f"{title}\n[Download Video]({video_url})",
            parse_mode="markdown"
        )
        
        os.remove(video_path)  # Remove the video file after sending
    else:  # If there is no video, send the image
        await client.send_photo(
            chat_id=message.chat.id,
            photo=image_url,
            caption=f"{title}\n[View Image]({image_url})",
            parse_mode="markdown"
        )


