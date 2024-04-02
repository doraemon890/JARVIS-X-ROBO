from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.enums import ChatAction

from .. import pbot as  Jarvis,BOT_USERNAME
import requests


@Jarvis.on_message(filters.command("qrcode"))
async def qrcode_(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "`Please wait...,\n\nCreating your Qrcode ...`")
    write = requests.get(f"https://mukesh-api.vercel.app/qrcode?query={text}").json()["results"]

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ Gᴇɴᴇʀᴀᴛᴇᴅ Qʀᴄᴏᴅᴇ 💘
✨ **Gᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** @{BOT_USERNAME}
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)
__mod_name__ = "Qʀᴄᴏᴅᴇ"
__help__ = """
 ➻ /qrcode : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ǫʀᴄᴏᴅᴇ
 """
