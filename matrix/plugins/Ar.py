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

from matrix import Start_Time, matrix
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"

matrix_uptime, start_time = None, None

@matrix.on(events.NewMessage(outgoing=True, pattern=f'.{ALIVE}'))
async def CheckUpTime(event):
    global start_time, matrix_uptime
    
    delete = await event.delete()
    user = await event.client.get_entity(event.chat_id)
    if start_time == None:
        start_time = time.time()
    
    elapsed_time = time.time() - start_time
    uptime = await get_readable_time((time.time() - StartTime))
    tg_bot = Config.TG_BOT_USERNAME
    elapsed_hours, elapsed_minutes, elapsed_seconds = int(elapsed_time // 3600), int((elapsed_time % 3600) // 60), int(elapsed_time % 60)
    matrix_uptime = '{}:{:02d}:{:02d}'.format(elapsed_hours, elapsed_minutes, elapsed_seconds)
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ping=ms
    MATRIX_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/b180dcd0020f55cb63f8a.mp4"
    if MATRIX_IMG:
        matrix = [x for x in MATRIX_IMG.split()]
        PIC = random.choice(matrix)
        try:
            await matrix.client.send_file(matrix.chat_id, PIC, caption=caption, reply_to=reply_to_id)
            await matrixevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(event)
    else:
        await edit_or_reply(event,caption)
        
        
    final_message = f"""
‌‎⿻┊NamE : {user.first_name}
‌‎⿻┊PyThon : 3.8
‌‎⿻┊UpTimE : {uptime}
‌‎⿻┊BoT : {tg_bot} ٫
‌‎⿻┊‌‎PinG : {ping}
⿻┊‌‎Varsion : (1.2) ,"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))
