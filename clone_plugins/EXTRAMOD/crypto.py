from pyrogram import Client, filters
import requests

API_BASE = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols={}"

@Client.on_message(filters.command("crypto"))
async def get_crypto_info(bot, message):
    try:
        symbol = message.text.split(None, 1)[1].lower()
        response_text = fetch_crypto_info(symbol)
        await message.reply_text(text=response_text, quote=True)

    except IndexError:
        await message.reply_text(text="❌ <b>Please provide a cryptocurrency symbol. Usage:</b> /crypto [symbol]", quote=True)
    except Exception as e:
        await message.reply_text(text=f"❌ <b>Error fetching data from CoinGecko API:</b> {str(e)}", quote=True)

def fetch_crypto_info(symbol):
    response = requests.get(API_BASE.format(symbol))
    data = response.json()

    if not data:
        return f"❌ <b>No data found for the symbol:</b> {symbol}"

    # Find the correct crypto by symbol
    for crypto in data:
        if crypto['symbol'].lower() == symbol:
            response_text = f"""--Crypto Information--

🔹 <b>Name:</b> {crypto['name']}
🔹 <b>Symbol:</b> {crypto['symbol'].upper()}
🔹 <b>Current Price:</b> ${crypto['current_price']}
🔹 <b>Market Cap:</b> ${crypto['market_cap']}
🔹 <b>Market Cap Rank:</b> {crypto['market_cap_rank']}
🔹 <b>Total Volume:</b> ${crypto['total_volume']}
🔹 <b>24h High:</b> ${crypto['high_24h']}
🔹 <b>24h Low:</b> ${crypto['low_24h']}
🔹 <b>Price Change (24h):</b> ${crypto['price_change_24h']}
🔹 <b>Price Change % (24h):</b> {crypto['price_change_percentage_24h']}%
🔹 <b>All-Time High:</b> ${crypto['ath']}
🔹 <b>All-Time High Change %:</b> {crypto['ath_change_percentage']}%
🔹 <b>All-Time High Date:</b> {crypto['ath_date']}
🔹 <b>All-Time Low:</b> ${crypto['atl']}
🔹 <b>All-Time Low Change %:</b> {crypto['atl_change_percentage']}%
🔹 <b>All-Time Low Date:</b> {crypto['atl_date']}
🔹 <b>Last Updated:</b> {crypto['last_updated']}
"""
            return response_text

    return f"❌ <b>No data found for the symbol:</b> {symbol}"