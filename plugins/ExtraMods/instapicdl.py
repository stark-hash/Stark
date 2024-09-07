from pyrogram import Client, filters
import requests

INSTAGRAM_API_URL = "https://instagram-video-downloader-api.p.rapidapi.com/api/instagram/links"
RAPIDAPI_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
RAPIDAPI_HOST = "instagram-video-downloader-api.p.rapidapi.com"

# Handler for Instagram picture download
@Client.on_message(filters.command("instadl"))
async def instagram_picture_download(bot, message):
    try:
        # Extract the Instagram URL from the user's message
        query = message.text.split(None, 1)[1]

        # Call the function to get the picture download link
        response_text, picture_url = download_instagram_picture(query)

        # Send the picture back to the user
        await message.reply_photo(
            photo=picture_url,
            caption=response_text,
            quote=True
        )

    except IndexError:
        # Handle case where the user does not provide a URL
        await message.reply_text("❌ <b>Please provide an Instagram post URL.</b>", quote=True)
    except Exception as e:
        # Handle any other errors
        await message.reply_text(f"❌ <b>Error fetching Instagram picture:</b> {str(e)}", quote=True)

# Function to fetch Instagram picture download link
def download_instagram_picture(insta_url):
    # Payload and headers for the API request, using the user-provided Instagram URL
    payload = {
        "url": insta_url  # The Instagram URL provided by the user
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }

    # Send POST request to the Instagram downloader API
    response = requests.post(INSTAGRAM_API_URL, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the 'pictureUrl' from the response
        picture_url = data[0].get('pictureUrl')

        if picture_url:
            # Create a response text for the user
            response_text = "Here is the Instagram picture you requested."
            return response_text, picture_url
        else:
            # Handle case where the picture URL is not available
            raise Exception("Picture URL not found in the response.")
    else:
        # Handle unsuccessful responses
        raise Exception(f"Failed to fetch Instagram picture: {response.status_code}")
