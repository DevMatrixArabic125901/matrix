import random
import re
import base64
import time
import asyncio
import os
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from matrix import StartTime, matrix, catversion
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

@matrix.ma_cmd(pattern="فحص(?:\s|$)([\s\S]*)")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "**᥀︙ جاري فحص السورس**")
    end = datetime.now()
    ping = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "᥀︙‎"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "𝖶𝖾𝗅𝖼𝗈𝗆 𝖬𝖺𝗍𝗋𝗂x 𝖠𝗋𝖺𝖻𝗂𝖼"
    MATRIX_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/b180dcd0020f55cb63f8a.mp4"
    MATRIXTM = time.strftime("%I:%M")
    matrixiq_caption = gvarstatus("ALIVE_MATRIXTMATRIXT") or matrix
    caption = matrixiq_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        my_mention=mention,
        uptime=uptime,
        mention=mention,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ping,
        MATRIXTM=MATRIXTM,
        tg_bot=tg_bot,    )
    if MATRIX_IMG:
        matrix = [x for x in MATRIX_IMG.split()]
        PIC = random.choice(matrix)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


matrix = """᥀┊𝖬𝗒 𖠄 {my_mention} ٫
‌‎᥀┊𝖳𝗂𝗆𝖾 𖠄 {MATRIXMATRIXTM} ٫
‌‎᥀┊𝗎𝗉 𝖳𝗂𝗆𝖾 𖠄 {uptime} ٫
‌‎᥀┊‌‎𝖯𝗂𝗇𝗀 𖠄 {ping} ٫
‌‎᥀┊𝖡𝗈𝖳 𖠄 {tg_bot} ٫
‌‎᥀┊‌‎𝖬𝖺𝖳𝗋𝗂x 𝖠𝗋𝖺𝖻𝗂𝖼 𖠄 @MaTrixThon"""
