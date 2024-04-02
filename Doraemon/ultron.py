

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from JarvisRobo import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, BOT_NAME

# <============================================== CONSTANTS =========================================================>
STATS_IMG = [
    "https://telegra.ph/file/61296490da95c55a1d5ee.jpg",
]
START_IMG = [
    "https://telegra.ph/file/cca68f5b49279dbee536b.jpg",
    "https://telegra.ph/file/7cf58d5a9fddd72a75867.jpg",
    "https://telegra.ph/file/61296490da95c55a1d5ee.jpg",
]

HEY_IMG = "https://telegra.ph/file/9458a724ae8ebe1de8565.png"

ALIVE_ANIMATION = [
     "https://graph.org/file/c3b6db252f9b089a7d14a.mp4",
     "https://graph.org/file/b28f15902589c079f5f79.mp4",
]

FIRST_PART_TEXT = "*ʜᴇʏ* `{}` , 🥀 . . ."

PM_START_TEXT = """
*๏ ᴛʜɪs ɪs* ˹ᴊᴀʀᴠɪs˼ !
➻ ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs ✨

──────────────────
*๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.*
"""

START_BTN = [
   [
        InlineKeyboardButton(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
   [
        InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="❄ ᴀʙᴏᴜᴛ ❄", callback_data="Jarvis_"),
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/JARVIS_X_SUPPORT"),
    ],
   [
        InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="☁️ sᴏᴜʀᴄᴇ ☁️", callback_data="git_source"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/JARVIS_X_SUPPORT"),
        InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/JARVIS_X_SUPPORT"),
        ib(text="sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/CHATTING_2024"),
    ],
    [
        ib(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = f"""
*» ᴊᴀʀᴠɪs ᴇxᴄʟᴜsɪᴠᴇ ꜰᴇᴀᴛᴜʀᴇs*

ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜱᴇᴄᴛɪᴏɴ.
 ‣ ɪɴ ᴘᴍ : ᴡɪʟʟ ꜱᴇɴᴅ ʏᴏᴜ ʜᴇʟᴘ​ ꜰᴏʀ ᴀʟʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇꜱ.
 ‣ ɪɴ ɢʀᴏᴜᴘ : ᴡɪʟʟ ʀᴇᴅɪʀᴇᴄᴛ ʏᴏᴜ ᴛᴏ ᴘᴍ, ᴡɪᴛʜ ᴀʟʟ ᴛʜᴀᴛ ʜᴇʟᴘ​ ᴍᴏᴅᴜʟᴇꜱ.
 """
