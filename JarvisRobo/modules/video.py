from __future__ import unicode_literals

import asyncio
import os
import time
from urllib.parse import urlparse

import wget
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
import requests
from JarvisRobo import pbot




async def download_instagram_reels(url: str) -> str:
    try:
        response = requests.post(f"https://api.qewertyy.dev/download/instagram?url={url}")
        
        if response.status_code == 200:
            data = response.json()
            if "content" in data and len(data["content"]) > 0:
                video_url = data["content"][0]["url"]
                return video_url
            else:
                return "No content found in the response."
        else:
            return f"Request failed with status code: {response.status_code}"
    except Exception as e:
        return f"Something went wrong: {e}"


# Command to download an Instagram Reels video
@pbot.on_message(filters.command("insta"))
async def download_instagram_reels_command(client, message):
    try:
        if len(message.text.split(" ")) == 1:
            await message.reply_text("Please provide an Instagram Reels link after the command.")
            return
        
        url = message.text.split(" ", 1)[1]
        video_url = await download_instagram_reels(url)
        
        if video_url.startswith("http"):
            await message.reply_video(video_url)
        else:
            await message.reply_text(video_url)
    except Exception as e:
        await message.reply_text(f"Something went wrong: {e}")


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@pbot.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, f"sᴇᴀʀᴄʜɪɴɢ, ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    if not urlissed:
        await pablo.edit(
            "😴 sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ᴏɴ ʏᴏᴜᴛᴜʙᴇ.\n\n» ᴍᴀʏʙᴇ ᴛᴜɴᴇ ɢᴀʟᴛɪ ʟɪᴋʜᴀ ʜᴏ, ᴩᴀᴅʜᴀɪ - ʟɪᴋʜᴀɪ ᴛᴏʜ ᴋᴀʀᴛᴀ ɴᴀʜɪ ᴛᴜ !"
        )
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            round(infoo["duration"] / 60)
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.** \n**ᴇʀʀᴏʀ :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"❄ **ᴛɪᴛʟᴇ :** [{thum}]({mo})\n💫 **ᴄʜᴀɴɴᴇʟ :** {thums}\n✨ **sᴇᴀʀᴄʜᴇᴅ :** {urlissed}\n🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {chutiya}"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress_args=(
            pablo,
            c_time,
            f"» ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\nᴜᴩʟᴏᴀᴅɪɴɢ `{urlissed}` ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ sᴇʀᴠᴇʀs...💫",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

# __mod_name__ = "Vɪᴅᴇᴏ"
# __help__ = """ 
# /video to download video
#  """


