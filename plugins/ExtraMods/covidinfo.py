from pyrogram import Client, filters
import requests

# Your COVID-19 API details
API_URL = "https://covid-19-data.p.rapidapi.com/country/code"
API_KEY = "645c5bb55emsh4a9339f4e45b563p183a3cjsneaef1f5eae8d"
API_HOST = "covid-19-data.p.rapidapi.com"

# Function to fetch COVID-19 data
def fetch_covid_data(country_code):
    querystring = {"format": "json", "code": country_code}
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    
    response = requests.get(API_URL, headers=headers, params=querystring)
    data = response.json()

    if data:
        country_data = data[0]
        return (
            f"**Country:** {country_data['country']}\n"
            f"**Confirmed cases:** {country_data['confirmed']}\n"
            f"**Recovered cases:** {country_data['recovered']}\n"
            f"**Critical cases:** {country_data['critical']}\n"
            f"**Deaths:** {country_data['deaths']}\n"
            f"**Last update:** {country_data['lastUpdate']}"
        )
    else:
        return "No data available for the given country code."

# Your bot configuration
@Client.on_message(filters.command("covid"))
async def get_covid_info(bot, message):
    # Extract the country code from the message
    if len(message.text.split()) < 2:
        await message.reply_text(
            text="❌ <b>Please provide a country code (e.g., 'IT' for Italy).</b>",
            quote=True
        )
        return

    country_code = message.text.split()[1].upper()

    # Check for vulgar words
    if any(word in country_code.lower() for word in vulgar_words):
        await message.reply_text(
            text="❌ <b>Please refrain from using inappropriate content.</b>",
            quote=True
        )
        return

    try:
        answer = fetch_covid_data(country_code)
        await message.reply_text(
            text=answer,
            quote=True
        )

    except Exception as e:
        await message.reply_text(text="❌ <b>Error fetching COVID-19 data</b>", quote=True)

