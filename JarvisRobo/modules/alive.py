import random
import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver
from JarvisRobo import SUPPORT_CHAT, pbot, BOT_USERNAME, OWNER_ID, BOT_NAME, START_IMG

VID = [
    "https://graph.org/file/c3b6db252f9b089a7d14a.mp4",
    "https://graph.org/file/b28f15902589c079f5f79.mp4",
]

Jarvis_buttons = [
    [
        InlineKeyboardButton(text="ᴊᴀʀᴠɪs", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("📲")
    await asyncio.sleep(0.2)
    await accha.edit("Jᴀʀᴠɪs ᴄᴀᴄʜɪɴɢ ᴅᴀᴛᴀ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴄᴏʀᴇ ᴀɴᴀʟʏsᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...")
    await asyncio.sleep(0.1)
    await accha.edit("ᴊᴀʀᴠɪs 🔮 ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgEAAx0Cfbdm0QACATVmC-2FuLpqFS0KfIHldXuM8eTtjwACsQQAAsW0uURrdxdu_gmoNh4E"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_video(
        random.choice(VID),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
━━━━━━━━━━━━━━━━━━━
» **ᴍʏ ᴏᴡɴᴇʀ :** [ᴏᴡɴᴇʀ](tg://user?id={OWNER_ID})

» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`

» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`

» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`

» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(Jarvis_buttons),
    )
