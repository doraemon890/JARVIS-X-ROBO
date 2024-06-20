import os
import re
import glob
import uuid
import asyncio
import requests
import urllib.request
from bs4 import BeautifulSoup
from bing_image_downloader import downloader
from search_engine_parser import GoogleSearch
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import httpx
from PIL import Image
from JarvisRobo import telethn as tbot, pbot
from JarvisRobo.events import register

# Constants
USER_AGENT = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
ENDPOINT = "https://sasta-api.vercel.app/googleImageSearch"
httpx_client = httpx.AsyncClient(timeout=60)
COMMANDS = ["reverse", "grs", "gis", "pp"]
opener = urllib.request.build_opener()
opener.addheaders = [("User-agent", USER_AGENT)]

# Strings
class STRINGS:
    REPLY_TO_MEDIA = "`ℹ️ Please reply to a message that contains one of the supported media types, such as a photo, sticker, or image file.`"
    UNSUPPORTED_MEDIA_TYPE = "`⚠️ <b>Unsupported media type!</b>\nℹ️ Please reply with a supported media type: image, sticker, or image file.`"
    REQUESTING_API_SERVER = "` Requesting to <b>API Server</b>... 📶`"
    DOWNLOADING_MEDIA = "` Downloading media...`"
    UPLOADING_TO_API_SERVER = "`📡 Uploading media to <b>API Server</b>... 📶`"
    PARSING_RESULT = "`💻 Parsing result...`"
    EXCEPTION_OCCURRED = "❌ <b>Exception occurred!</b>\n\n<b>Exception:</b> {}"
    RESULT = """
🔤 <b>Query:</b> {query}
🔗 <b>Page Link:</b> <a href="{search_url}">Link</a>
⌛️ <b>Time Taken:</b> <code>{time_taken}</code> ms.
    """
    OPEN_SEARCH_PAGE = "↗️ Open Search Page"

# Google search
@register(pattern="^/google (.*)")
async def google_search(event):
    if event.fwd_from:
        return

    webevent = await event.reply("Searching...")
    match = event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0].replace("page=", "")
        match = match.replace(f"page={page}", "")
    except IndexError:
        page = 1
    
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"❍[{title}]({link})\n**{desc}**\n\n"
        except IndexError:
            break
    
    await webevent.edit(
        f"**Search Query:**\n`{match}`\n\n**Results:**\n{msg}",
        link_preview=False
    )

# Image search
@register(pattern="^/img (.*)")
async def img_search(event):
    if event.fwd_from:
        return

    query = event.pattern_match.group(1)
    downloader.download(
        query,
        limit=4,
        output_dir="store",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
    )
    os.chdir(f'./store/"{query}"')
    files_grabbed = []
    for files in ("*.png", "*.jpeg", "*.jpg"):
        files_grabbed.extend(glob.glob(files))
    
    await tbot.send_file(event.chat_id, files_grabbed, reply_to=event.id)
    os.chdir("/app")
    os.system("rm -rf store")

# Reverse image search
@pbot.on_message(filters.command(COMMANDS))
async def on_google_lens_search(client: Client, message: Message):
    if len(message.command) > 1:
        image_url = message.command[1]
        params = {"image_url": image_url}
        status_msg = await message.reply(STRINGS.REQUESTING_API_SERVER)
        start_time = asyncio.get_event_loop().time()
        response = await httpx_client.get(ENDPOINT, params=params)
    elif (reply := message.reply_to_message):
        if reply.media not in (MessageMediaType.PHOTO, MessageMediaType.STICKER, MessageMediaType.DOCUMENT):
            await message.reply(STRINGS.UNSUPPORTED_MEDIA_TYPE)
            return

        status_msg = await message.reply(STRINGS.DOWNLOADING_MEDIA)
        file_path = f"temp/{uuid.uuid4()}"
        try:
            await reply.download(file_path)
        except Exception as exc:
            await message.reply(STRINGS.EXCEPTION_OCCURRED.format(exc))
            os.remove(file_path)
            return
        
        with open(file_path, "rb") as image_file:
            start_time = asyncio.get_event_loop().time()
            files = {"file": image_file}
            await status_msg.edit(STRINGS.UPLOADING_TO_API_SERVER)
            response = await httpx_client.post(ENDPOINT, files=files)
        
        os.remove(file_path)
    
    if response.status_code == 404:
        await message.reply(STRINGS.EXCEPTION_OCCURRED.format(response.json()["error"]))
        await status_msg.delete()
        return
    elif response.status_code != 200:
        await message.reply(STRINGS.EXCEPTION_OCCURRED.format(response.text))
        await status_msg.delete()
        return
    
    await status_msg.edit(STRINGS.PARSING_RESULT)
    response_json = response.json()
    query = response_json["query"]
    search_url = response_json["search_url"]
    end_time = asyncio.get_event_loop().time() - start_time
    time_taken = "{:.2f}".format(end_time)
    
    text = STRINGS.RESULT.format(
        query=f"<code>{query}</code>" if query else "<i>Name not found</i>",
        search_url=search_url,
        time_taken=time_taken
    )
    buttons = [[InlineKeyboardButton(STRINGS.OPEN_SEARCH_PAGE, url=search_url)]]
    await message.reply(text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))
    await status_msg.delete()

# Play Store app search
@register(pattern="^/app (.*)")
async def app_search(event):
    try:
        app_name = event.pattern_match.group(1)
        final_name = "+".join(app_name.split(" "))
        page = requests.get(f"https://play.google.com/store/search?q={final_name}&c=apps")
        soup = BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        
        app_info = results[0].findNext("div", "Vpfmgd")
        app_name = app_info.findNext("div", "WsMG1c nnK0zc").text
        app_dev = app_info.findNext("div", "KoLSrc").text
        app_dev_link = f"https://play.google.com{app_info.findNext('a', 'mnKHRc')['href']}"
        app_rating = app_info.findNext("div", "pf5lIe").find("div")["aria-label"]
        app_link = f"https://play.google.com{app_info.findNext('div', 'vU6FJ p63iDd').a['href']}"
        app_icon = app_info.findNext("div", "uzcko").img["data-src"]
        
        app_details = (
            f"<a href='{app_icon}'>📲&#8203;</a> <b>{app_name}</b>"
            f"\n\n<code>Developer :</code> <a href='{app_dev_link}'>{app_dev}</a>"
            f"\n<code>Rating :</code> {app_rating.replace('Rated ', '⭐ ').replace(' out of ', '/').replace(' stars', '', 1).replace(' stars', '⭐ ').replace('five', '5')}"
            f"\n<code>Features :</code> <a href='{app_link}'>View in Play Store</a>"
            f"\n\n===> Group Controller<==="
        )
        await event.reply(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.reply(f"Exception Occured:- {str(err)}")

__mod_name__ = "Gᴏᴏɢʟᴇ"
__help__ = """
 ❍ /google <text>*:* Perform a google search
 ❍ /img <text>*:* Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 ❍ /app <appname>*:* Searches for an app in Play Store and returns its details.
 ❍ /reverse |pp |grs
"""
