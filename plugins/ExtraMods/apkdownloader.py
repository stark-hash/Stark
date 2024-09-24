import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import LOG_CHANNEL  # Import LOG_CHANNEL from your info module

# API keys and host details
API_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
API_HOST = "apkpure-malavida-app-downloader.p.rapidapi.com"
APK_URL = "https://apkpure-malavida-app-downloader.p.rapidapi.com/aptoide"

# Fetch APK data from API
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

# Pyrogram command to search for APKs
@Client.on_message(filters.command("apk"))
async def apk_downloader(bot, message):
    try:
        # Get the APK name or query from the message
        query = message.text.split(None, 1)[1].lower()

        # Fetch APK data based on the query
        response_text, apk_list = fetch_apk_response(query)

        # Log the search query to LOG_CHANNEL
        await bot.send_message(
            chat_id=LOG_CHANNEL, 
            text=f"User {message.from_user.mention} searched for '{query}'"
        )

        if apk_list:
            for apk in apk_list:
                # Prepare app details message
                app_name = apk["name"]
                developer = apk["developer"]["name"]
                icon_url = apk["icon"]
                graphic_url = apk.get("graphic", "")
                version = apk["file"]["vername"]
                size = apk["file"]["filesize"] / (1024 * 1024)  # Convert to MB
                download_link = apk["file"]["path"]

                # Create message text with APK details
                text = (
                    f"**App Name:** {app_name}\n"
                    f"**Developer:** {developer}\n"
                    f"**Version:** {version}\n"
                    f"**Size:** {size:.2f} MB\n"
                    f"![Icon]({icon_url})"
                )

                # Create an inline button for downloading the APK
                buttons = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Download APK", url=download_link)]]
                )

                # Send message with APK details and download button
                await message.reply_photo(
                    photo=graphic_url or icon_url,  # Use graphic if available, else icon
                    caption=text,
                    reply_markup=buttons
                )
        else:
            await message.reply_text(text="❌ <b>No results found.</b>")

    except IndexError:
        await message.reply_text(text="❌ <b>Please provide an APK name or query. Usage:</b> /apk [query]", quote=True)
    except Exception as e:
        await message.reply_text(text=f"❌ <b>Error fetching APK data:</b> {str(e)}", quote=True)

# Helper function to format APK search response
def fetch_apk_response(query):
    data = fetch_apk_data(query)

    if not data or data["info"]["status"] != "OK" or not data["datalist"]["list"]:
        return f"❌ <b>No data found for the query:</b> {query}", None

    apk_list = data["datalist"]["list"]
    return None, apk_list
