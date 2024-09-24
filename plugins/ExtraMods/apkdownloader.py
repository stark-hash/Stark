import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import LOG_CHANNEL  # Import LOG_CHANNEL from your info module

# API keys and host details (replace the x-rapidapi-key if needed)
API_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
API_HOST = "apkpure-malavida-app-downloader.p.rapidapi.com"
APK_URL = "https://apkpure-malavida-app-downloader.p.rapidapi.com/aptoide"


# Define the APK fetcher function
def fetch_apk_data(query):
    payload = (
        "-----011000010111000001101001\r\n"
        "Content-Disposition: form-data; name=\"query\"\r\n\r\n"
        f"{query}\r\n"
        "-----011000010111000001101001\r\n"
        "Content-Disposition: form-data; name=\"limit\"\r\n\r\n5\r\n"
        "-----011000010111000001101001\r\n"
        "Content-Disposition: form-data; name=\"language\"\r\n\r\nen\r\n"
        "-----011000010111000001101001--\r\n"
    )
    
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST,
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }
    
    response = requests.post(APK_URL, data=payload, headers=headers)
    return response.json()

# Bot command to search for APKs
@Client.on_message(filters.command("apk") & filters.text)
async def apk_downloader(client, message):
    query = " ".join(message.command[1:])
    
    if not query:
        await message.reply_text("Please provide an APK name or query to search.")
        return
    
    # Fetch APK data
    data = fetch_apk_data(query)
    
    # Log the search query to the LOG_CHANNEL
    await client.send_message(
        chat_id=LOG_CHANNEL, 
        text=f"User {message.from_user.mention} searched for '{query}'"
    )
    
    if data["info"]["status"] != "OK" or not data["datalist"]["list"]:
        await message.reply_text("No results found.")
        return
    
    apk_list = data["datalist"]["list"]
    
    # Prepare the message text and buttons
    for apk in apk_list:
        app_name = apk["name"]
        developer = apk["developer"]["name"]
        icon_url = apk["icon"]
        graphic_url = apk.get("graphic", "")
        version = apk["file"]["vername"]
        size = apk["file"]["filesize"] / (1024 * 1024)  # Convert to MB
        download_link = apk["file"]["path"]

        # Message text with app details
        text = (
            f"**App Name:** {app_name}\n"
            f"**Developer:** {developer}\n"
            f"**Version:** {version}\n"
            f"**Size:** {size:.2f} MB\n"
            f"![Icon]({icon_url})"
        )
        
        # Inline button with the download link
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Download APK", url=download_link)]]
        )
        
        # Send message with the APK details and download button
        await message.reply_photo(
            photo=graphic_url or icon_url,  # Use graphic image if available, else icon
            caption=text,
            reply_markup=buttons
        )


