import random
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import Button, events, version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from matrix import StartTime, matrixversion, matrix

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@matrix.ar_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    ANIME = None
    matrix_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in matrix_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    matrixevent = await edit_or_reply(event, "**- جار التأكد انتظر قليلا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**سورس ماتركس يعمل بنجاح**"
    matrix_IMG = gvarstatus("ALIVE_PIC")
    caption = matrix_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        maver=matrixversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if matrix_IMG:
        matrix = list(matrix_IMG.split())
        PIC = random.choice(matrix)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await matrixevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                matrixevent,
                f"**رابط الصورة غير صحيح**\nعليك الرد على رابط الصورة ب .اضف صورة الفحص",
            )
    else:
        await edit_or_reply(
            matrixevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**⊱━━━━━⊰✾⊱━━━━━⊰**
**{EMOJI} قاعدة البيانات :** `{dbhealth}`
**{EMOJI} اصدار التيليثون:** `{telever}`
**{EMOJI} اصدار ماتركس :** `{maver}`
**{EMOJI} اصدار البايثون :** `{pyver}`
**{EMOJI} الوقت :** `{uptime}`
**{EMOJI} المالك:** {mention}
⊱━━━━━⊰✾⊱━━━━━⊰"""

def matrixalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    matrix_caption = "**سورس ماتركس يعمل بنجاح**\n"
    matrix_caption += f"**{EMOJI} اصدار التيليثون :** `{version.__version__}\n`"
    matrix_caption += f"**{EMOJI} اصدار ماتركس :** `{matrixversion}`\n"
    matrix_caption += f"**{EMOJI} اصدار البايثون :** `{python_version()}\n`"
    matrix_caption += f"**{EMOJI} المالك:** {mention}\n"
    return matrix_caption


@matrix.ar_cmd(pattern="السورس$")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await matrix.inline_query(RR7PP, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()


MATR_PIC = "https://telegra.ph/file/c1849e51f4b591f84d422.jpg"
RAZAN = Config.TG_BOT_USERNAME
MATR_T = (
    f"**⌯︙بوت ماتــركس يعمل بنجاح 🤍،**\n"
    f"**   - اصدار التليثون :** `1.23.0\n`"
    f"**   - اصدار ماتركس :** `4.0.0`\n"
    f"**   - البوت المستخدم :** `{RAZAN}`\n"
    f"**   - اصدار البايثون :** `3.9.6\n`"
    f"**   - المستخدم :** {mention}\n"
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

@tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await matrix.get_me()
        if query.startswith("السورس") and event.query.user_id == matrix.uid:
            buttons = [
                [
                    Button.url("قنـاة السـورس ⚙️", "https://t.me/Matrix_Thon"),
                    Button.url("المطـور 👨🏼‍💻", "https://t.me/FFlXlX"),
                    Button.url("الدعم 🔍", "https://t.me/MatrixzSupport"),
                ]
            ]
            if MATR_PIC and MATR_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    MATR_PIC, text=MATR_T, buttons=buttons, link_preview=False
                )
            elif MATR_PIC:
                result = builder.document(
                    MATR_PIC,
                    title="MATRIX - USERBOT",
                    text=MATR_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="MATRIX - USERBOT",
                    text=MATR_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


