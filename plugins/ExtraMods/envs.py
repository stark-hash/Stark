import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import requests


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Define envs.sh interaction functions
def upload_file(file_path, secret=None, expires=None):
    url = 'https://envs.sh'
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = {}
            if secret:
                data['secret'] = secret
            if expires:
                data['expires'] = expires
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.text.strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error uploading file: {e}")
        return None
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None

def upload_remote_url(remote_url, secret=None, expires=None):
    url = 'https://envs.sh'
    data = {'url': remote_url}
    if secret:
        data['secret'] = secret
    if expires:
        data['expires'] = expires
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error uploading URL: {e}")
        return None

def shorten_url(long_url):
    url = 'https://envs.sh'
    data = {'shorten': long_url}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error shortening URL: {e}")
        return None

def delete_file(token):
    url = 'https://envs.sh'
    data = {'token': token, 'delete': ''}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error deleting file: {e}")
        return None

def change_expiration(token, expires):
    url = 'https://envs.sh'
    data = {'token': token, 'expires': expires}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error changing expiration: {e}")
        return None

# Command Handlers

@Client.on_message(filters.command("start") & filters.private)
def start_command(client: Client, message: Message):
    message.reply_text(
        "Hello! I'm your EnvS.sh Bot.\n\n"
        "You can use the following commands:\n"
        "/upload - Upload a photo.\n"
        "/uploadurl <URL> - Upload a file from a URL.\n"
        "/shorten <URL> - Shorten a URL.\n"
        "/delete <token> - Delete an uploaded file.\n"
        "/expire <token> <hours> - Change expiration time."
    )

@Client.on_message(filters.command("upload") & filters.private)
def handle_upload(client: Client, message: Message):
    if message.reply_to_message and (message.reply_to_message.photo or message.reply_to_message.document):
        # Determine the type of media and download accordingly
        media = message.reply_to_message.photo or message.reply_to_message.document
        file_path = media.download()
        if not file_path:
            message.reply_text("Failed to download the file.")
            return

        uploaded_url = upload_file(file_path)
        if uploaded_url:
            message.reply_text(f"📤 *File uploaded successfully:*\n{uploaded_url}")
        else:
            message.reply_text("❌ Failed to upload the file.")
    else:
        message.reply_text("❗ Please reply to a photo or document with the /upload command.")

@Client.on_message(filters.command("shorten") & filters.private)
def handle_shorten(client: Client, message: Message):
    try:
        _, long_url = message.text.split(None, 1)
        if not long_url.startswith(("http://", "https://")):
            message.reply_text("❌ Please provide a valid URL starting with http:// or https://")
            return
        short_url = shorten_url(long_url)
        if short_url:
            message.reply_text(f"🔗 *Shortened URL:*\n{short_url}")
        else:
            message.reply_text("❌ Failed to shorten the URL.")
    except ValueError:
        message.reply_text("ℹ️ Usage: /shorten <URL>")

@Client.on_message(filters.command("uploadurl") & filters.private)
def handle_upload_url(client: Client, message: Message):
    try:
        _, remote_url = message.text.split(None, 1)
        if not remote_url.startswith(("http://", "https://")):
            message.reply_text("❌ Please provide a valid URL starting with http:// or https://")
            return
        uploaded_url = upload_remote_url(remote_url)
        if uploaded_url:
            message.reply_text(f"📤 *URL uploaded successfully:*\n{uploaded_url}")
        else:
            message.reply_text("❌ Failed to upload the URL.")
    except ValueError:
        message.reply_text("ℹ️ Usage: /uploadurl <URL>")

@Client.on_message(filters.command("delete") & filters.private)
def handle_delete(client: Client, message: Message):
    try:
        _, token = message.text.split(None, 1)
        confirmation = delete_file(token)
        if confirmation:
            message.reply_text(f"✅ *File deleted successfully:*\n{confirmation}")
        else:
            message.reply_text("❌ Failed to delete the file. Please check the token.")
    except ValueError:
        message.reply_text("ℹ️ Usage: /delete <token>")

@Client.on_message(filters.command("expire") & filters.private)
def handle_expire(client: Client, message: Message):
    try:
        _, token, expires = message.text.split(None, 2)
        if not expires.isdigit():
            message.reply_text("❌ The expiration time must be a number representing hours.")
            return
        confirmation = change_expiration(token, expires)
        if confirmation:
            message.reply_text(f"⏳ *Expiration updated successfully:*\n{confirmation}")
        else:
            message.reply_text("❌ Failed to update expiration. Please check the token.")
    except ValueError:
        message.reply_text("ℹ️ Usage: /expire <token> <hours>")


