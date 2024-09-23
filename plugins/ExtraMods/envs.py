import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import requests



# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load ImgBB API key from environment variables
IMGBB_API_KEY = "7c37fa1960dcf159f2714faaa75ef12d"

# Define ImgBB interaction functions
def upload_image(file_path, name=None, expiration=None):
    url = 'https://api.imgbb.com/1/upload'
    try:
        with open(file_path, 'rb') as f:
            files = {'image': f}
            data = {'key': IMGBB_API_KEY}
            if name:
                data['name'] = name
            if expiration:
                data['expiration'] = expiration  # in seconds (60-15552000)

            logger.debug(f"Uploading image to {url} with data: {data} and files: {files.keys()}")
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response body: {response.text}")

            json_response = response.json()
            if json_response.get('success'):
                return json_response['data']['url']
            else:
                logger.error(f"ImgBB upload failed: {json_response}")
                return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error uploading image: {e}")
        if e.response is not None:
            logger.error(f"Response status: {e.response.status_code}")
            logger.error(f"Response body: {e.response.text}")
        return None
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None

# Command Handlers

@Client.on_message(filters.command("upload") & filters.private)
def handle_upload(client: Client, message: Message):
    if message.reply_to_message and (message.reply_to_message.photo or message.reply_to_message.document):
        # Determine the type of media and download accordingly
        media = message.reply_to_message.photo or message.reply_to_message.document
        file_path = media.download()
        if not file_path:
            message.reply_text("❌ Failed to download the file.")
            return

        uploaded_url = upload_image(file_path)
        if uploaded_url:
            message.reply_text(f"📤 *Image uploaded successfully:*\n{uploaded_url}")
        else:
            message.reply_text("❌ Failed to upload the image. Please check the logs for more details.")
    else:
        message.reply_text("❗ Please reply to a photo or document with the /upload command.")


