import pymongo
from info import DATABASE_URL, DATABASE_NAME
from pyrogram import enums
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture detailed logs

myclient = pymongo.MongoClient(DATABASE_URL)
mydb = myclient["GlobalFilters"]

async def add_gfilter(gfilters, text, reply_text, btn, file, alert):
    logger.debug(f"Attempting to add/update filter: {text} in collection: {gfilters}")
    mycol = mydb[str(gfilters)]
    data = {
        'text': str(text),
        'reply': str(reply_text),
        'btn': str(btn),
        'file': str(file),
        'alert': str(alert)
    }
    try:
        mycol.update_one({'text': str(text)}, {"$set": data}, upsert=True)
        logger.info(f"Filter '{text}' added/updated successfully in collection '{gfilters}'.")
    except Exception as e:
        logger.exception("Error occurred while adding filter.", exc_info=True)

async def find_gfilter(gfilters, name):
    logger.debug(f"Searching for filter '{name}' in collection '{gfilters}'")
    mycol = mydb[str(gfilters)]
    
    query = mycol.find({"text": name})
    try:
        for file in query:
            reply_text = file['reply']
            btn = file['btn']
            fileid = file['file']
            alert = file.get('alert', None)
            logger.info(f"Filter '{name}' found with reply: {reply_text}")
            return reply_text, btn, alert, fileid
        logger.warning(f"Filter '{name}' not found in collection '{gfilters}'")
        return None, None, None, None
    except Exception as e:
        logger.exception("Error occurred while retrieving filter.", exc_info=True)
        return None, None, None, None

async def get_gfilters(gfilters):
    logger.debug(f"Retrieving all filters in collection '{gfilters}'")
    mycol = mydb[str(gfilters)]
    
    texts = []
    try:
        query = mycol.find()
        for file in query:
            text = file['text']
            texts.append(text)
        logger.info(f"Retrieved filters: {texts}")
    except Exception as e:
        logger.exception("Error occurred while retrieving all filters.", exc_info=True)
    return texts

async def delete_gfilter(message, text, gfilters):
    logger.debug(f"Attempting to delete filter '{text}' in collection '{gfilters}'")
    mycol = mydb[str(gfilters)]
    
    myquery = {'text': text}
    try:
        query = mycol.count_documents(myquery)
        if query == 1:
            mycol.delete_one(myquery)
            await message.reply_text(
                f"'`{text}`'  deleted. I'll not respond to that gfilter anymore.",
                quote=True,
                parse_mode=enums.ParseMode.MARKDOWN
            )
            logger.info(f"Filter '{text}' deleted successfully from collection '{gfilters}'.")
        else:
            await message.reply_text("Couldn't find that gfilter!", quote=True)
            logger.warning(f"Filter '{text}' not found in collection '{gfilters}' for deletion.")
    except Exception as e:
        logger.exception("Error occurred while deleting filter.", exc_info=True)

async def del_allg(message, gfilters):
    logger.debug(f"Attempting to delete all filters in collection '{gfilters}'")
    if str(gfilters) not in mydb.list_collection_names():
        await message.edit_text("Nothing to delete!")
        logger.info(f"No collection named '{gfilters}' found to delete.")
        return

    mycol = mydb[str(gfilters)]
    try:
        mycol.drop()
        await message.edit_text("All filters have been removed.")
        logger.info(f"All filters in collection '{gfilters}' deleted successfully.")
    except Exception as e:
        await message.edit_text("Couldn't remove all filters!")
        logger.exception("Error occurred while deleting all filters.", exc_info=True)

async def count_gfilters(gfilters):
    logger.debug(f"Counting filters in collection '{gfilters}'")
    mycol = mydb[str(gfilters)]

    try:
        count = mycol.count_documents({})
        logger.info(f"Collection '{gfilters}' has {count} filters.")
        return False if count == 0 else count
    except Exception as e:
        logger.exception("Error occurred while counting filters.", exc_info=True)
        return False

async def gfilter_stats():
    logger.debug("Calculating global filter statistics")
    collections = mydb.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    totalcount = 0
    for collection in collections:
        mycol = mydb[collection]
        try:
            count = mycol.count_documents({})
            totalcount += count
        except Exception as e:
            logger.exception(f"Error counting documents in collection '{collection}'", exc_info=True)

    totalcollections = len(collections)
    logger.info(f"Total collections: {totalcollections}, Total filters: {totalcount}")
    return totalcollections, totalcount
