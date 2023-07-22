from AloneXMusic import bot
from AloneXMusic.modules.main.database import is_on_off
from AloneXMusic.utilities.config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**{MUSIC_BOT_NAME} ᴩʟᴀʏ ʟᴏɢɢᴇʀ**

**ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**ᴜsᴇʀ:** {message.from_user.mention}
**ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**ɪᴅ:** `{message.from_user.id}`
**ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

**sᴇᴀʀᴄʜᴇᴅ ғᴏʀ:** {message.text}

**sᴛʀᴇᴀᴍ ᴛʏᴩᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await bot.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
