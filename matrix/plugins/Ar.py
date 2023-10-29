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
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP
from ..core.managers import edit_or_reply
from matrix import StartTime
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

random_media = ["https://telegra.ph/file/74066cb3ddb0bdba1c4b7.mp4","https://telegra.ph/file/20cc5275397d21790162b.mp4"]

matrix_uptime, start_time = None, None

@matrix.ma_cmd(pattern="فحص(?:\s|$)([\s\S]*)")
async def matrixar(event):
    reply_to_id = await reply_id(event)
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
    me = await event.client.get_me()
    my_last = me.last_name
    my_mention = f"[{me.last_name}](tg://user?id={me.id})"
    start = datetime.now()
    end = datetime.now()
    MATRIXTM = time.strftime("%I:%M")
    file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    my_mention=my_mention,
    MATRIXTM=MATRIXTM
    MATRIXDATE=installation_time
    ping=ms
        
    final_message = f"""
‌‎⿻┊NamE : {user.first_name}
‌‎⿻┊TimE : {MATRIXTM}
‌‎⿻┊DaTE : {tg_bot}
‌‎⿻┊UpTimE : {uptime}
‌‎⿻┊BoT : {tg_bot}
‌‎⿻┊PyThon : 3.8
‌‎⿻┊‌‎PinG : {ping}
⿻┊‌‎VarSioN : (1.2)
‌‎⿻┊‌[MaTrix AraBic](https://t.me/matrixthon)"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))
