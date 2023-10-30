import random
import re
import base64
import time
import asyncio
import requests
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
from ..sql_helper.globals import gvarstatus
from . import mention

headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Content-Length': '25',
    'User-Agent': 'Nicegram/101 CFNetwork/1404.0.5 Darwin/22.3.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

    data_matrix = '{"telegramId":' + str(idd) + '}'
    matrix = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data_matrix)

    mat = json.loads(matrix.text)
    date = mat['data']['date']

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
    random_media = ["https://telegra.ph/file/74066cb3ddb0bdba1c4b7.mp4"]
    MATRIXTM = time.strftime("%I:%M")
    MATRIXDATE = time.strftime("%Y/%m/%d")
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    my_mention=my_mention,
    MATRIXTM=MATRIXTM
    MATRIXDATE=MATRIXDATE
    pyver=python_version()
    ping=ms
    data_matrix=date
        
    final_message = f"""
‌‎⿻┊‌[MaTrix AraBic](https://t.me/matrixthon)
‌‎⿻┊NamE : {user.first_name}
‌‎⿻┊DaTE : {MATRIXDATE}
‌‎⿻┊TimE : {MATRIXTM}
‌‎⿻┊UpTimE : {uptime}
‌‎⿻┊BoT : {tg_bot}
‌‎⿻┊PyThon : {pyver}
‌‎⿻┊‌‎CreaTe AccounT : {data_matrix}
‌‎⿻┊‌‎PinG : {ping}
⿻┊‌‎VarSioN : (1.2)"""
    send_new_message = await event.client.send_message(entity=event.chat_id, message=final_message, file=random.choice(random_media))
