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

from matrix import StartTime, matrix
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..helpers.tools import media_type
from ..sql_helper.globals import gvarstatus
from . import mention

matrix_uptime, start_time = None, None

@matrix.ma_cmd(pattern="فحص(?:\s|$)([\s\S]*)")
async def matrixar(event):
    reply_to_id = await reply_id(event)
    await edit_or_reply(event, "** ᥀︙يتـم التـأكـد انتـظر قليلا رجاءا**")
    uptime = await get_readable_time((time.time() - StartTime))
    tg_bot = Config.TG_BOT_USERNAME
    me = await event.client.get_me()
    start = datetime.now()
    end = datetime.now()
    my_first_name = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    random_media = ["https://telegra.ph/file/74066cb3ddb0bdba1c4b7.mp4"]
    MATRIXTM = time.strftime("%I:%M")
    MATRIXDATE = time.strftime("%Y/%m/%d")
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    MATRIXTM=MATRIXTM
    MATRIXDATE=MATRIXDATE
    my_mention=my_mention
    pyver=python_version()
    ping=ms
        
    final_message = f"""
‌‎᥀┊‌[MaTrix AraBic](https://t.me/matrixthon)
‌‎᥀┊NamE : {my_mention}
᥀‌‎┊DaTE : {MATRIXDATE}
‌‎᥀┊TimE : {MATRIXTM}
‌‎᥀┊UpTimE : {uptime}
‌‎᥀┊BoT : {tg_bot}
‌‎᥀┊PyThon : {pyver}
‌‎᥀┊‌‎PinG : {ping}
᥀┊‌‎VarSioN : (1.2)"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))
