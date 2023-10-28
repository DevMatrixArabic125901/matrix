import os

import aiohttp

import requests

import random

import re

import time

import sys

import asyncio

import math

import heroku3

import urllib3

import speedtest

import base64

import psutil

import platform

from telethon.errors.rpcerrorlist import BotInlineDisabledError

import json

from subprocess import PIPE

from subprocess import run as runapp

from asyncio.exceptions import CancelledError

from time import sleep

from platform import python_version

from github import Github

from pySmartDL import SmartDL

from pathlib import Path

from telethon.errors import QueryIdInvalidError

from telethon.errors import QueryIdInvalidError

from telethon.tl.types import InputMessagesFilterDocument

from ..core import check_owner, pool

from datetime import datetime

from telethon import Button, events ,types 

from telethon.events import CallbackQuery, InlineQuery

from telethon.tl.functions.messages import ImportChatInviteRequest

from telethon.tl.functions.messages import GetMessagesViewsRequest

from telethon.tl.functions.channels import JoinChannelRequest

from telethon.tl.functions.channels import LeaveChannelRequest

from telethon.utils import get_display_name

from urlextract import URLExtract

from validators.url import url

from matrix import StartTime

from matrix import matrix

from ..Config import Config

from ..core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time

from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

from ..helpers.tools import media_type

from . import media_type, progress

from ..utils import load_module, remove_plugin

from ..sql_helper.globals import addgvar, delgvar, gvarstatus

from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items

from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP

from SQL.extras import *

from matrix import StartTime, matrix

from telethon.tl.functions.channels import JoinChannelRequest

from telethon.tl.functions.messages import ImportChatInviteRequest

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.contacts import UnblockRequest

from telethon import client, events

ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"

UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"

ORDERS = gvarstatus("OR_ORDERS") or "(الاوامر|ألاوامر|أوامري|م)"

matrixPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/b180dcd0020f55cb63f8a.mp4"

LOGS = logging.getLogger(os.path.basename(__name__))

LOGS1 = logging.getLogger(__name__)

ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")

GIT_TEMP_DIR = "./temp/"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)

heroku_api = "https://api.heroku.com"

HEROKU_APP_NAME = Config.HEROKU_APP_NAME

HEROKU_API_KEY = Config.HEROKU_API_KEY

cmdhd = Config.COMMAND_HAND_LER

extractor = URLExtract()

vlist = [    "ALIVE_PIC", "TGMABOT","subgroup","subprivate", "pchan",  "ALIVE_EMOJI",    "ALIVE_TMATRIXT",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP","OR_UNMUQT"]

DELETE_TIMEOUT = 5

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}

matrixteamPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/b180dcd0020f55cb63f8a.mp4"

def convert_from_bytes(size):

    power = 2 ** 10

    n = 0

    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}

    while size > power:

        size /= power

        n += 1

    return f"{round(size, 2)} {units[n]}"






@matrix.on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
	
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
    matrixiq_caption = gvarstatus("ALIVE_MATRIXTMATRIXT") or temp
    caption = matrixiq_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        my_mention=my_mention,
        uptime=uptime,
        mention=mention,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ping,
        MATRIXTM=MATRIXTM,
        tg_bot=tg_bot,    )
    )
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


temp = """᥀┊𝖬𝗒 𖠄 {my_mention} ٫
‌‎᥀┊𝖳𝗂𝗆𝖾 𖠄 {MATRIXMATRIXTM} ٫
‌‎᥀┊𝗎𝗉 𝖳𝗂𝗆𝖾 𖠄 {uptime} ٫
‌‎᥀┊‌‎𝖯𝗂𝗇𝗀 𖠄 {ping} ٫
‌‎᥀┊𝖡𝗈𝖳 𖠄 {tg_bot} ٫
‌‎᥀┊‌‎𝖬𝖺𝖳𝗋𝗂x 𝖠𝗋𝖺𝖻𝗂𝖼 𖠄 @MaTrixThon"""

@matrix.on(admin_cmd(pattern="المده(?: |$)(.*)"))    

async def amireallyalive(event):

    reply_to_id = await reply_id(event)

    uptime = await get_readable_time((time.time() - StartTime))

    _, check_sgnirts = check_data_base_heal_th()

    EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " ٍَ 🖤"

    matrix_ALIVE_TEXT = "❬ ماتركس العربي - MaTriX Arabic ، 🕸  ❭ :"

    matrix_IMG = gvarstatus("ALIVE_PIC")

    if matrix_IMG:

        CAT = [x for x in matrix_IMG.split()]

        A_IMG = list(CAT)

        PIC = random.choice(A_IMG)

        cat_caption += f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**"

        try:

            await event.client.send_file(event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id)

            await event.delete()

        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):

            return await edit_or_reply(event, f"**مدة التشغيل")

    else:

        await edit_or_reply(event, f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**")

@matrix.on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    

async def _(event):

    cmd = "env"

    o = (await _catutils.runcmd(cmd))[0]

    OUTPUT = (f"᥀ ︙ وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب سورس ماتركس @matrix :**\n\n{o}")

    await edit_or_reply(event, OUTPUT)



if Config.PLUGIN_CHANNEL:



    async def install():

        documentss = await matrix.get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )

        total = int(documentss.total)

        for module in range(total):

            plugin_to_install = documentss[module].id

            plugin_name = documentss[module].file.name

            if os.path.exists(f"matrix/plugins/{plugin_name}"):

                return

            downloaded_file_name = await matrix.download_media(                await matrix.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "matrix/plugins/",            )

            path1 = Path(downloaded_file_name)

            shortname = path1.stem

            flag = True

            check = 0

            while flag:

                try:

                    load_module(shortname.replace(".py", ""))

                    break

                except ModuleNotFoundError as e:

                    install_pip(e.name)

                    check += 1

                    if check > 5:

                        break

            if BOTLOG:

                await matrix.send_message(                    BOTLOG_CHATID,                    f"**᥀ ︙  تحـميل المـلف 🗂️  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )



    matrix.loop.create_task(install())

@matrix.on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    

async def _(event):

    sandy = await edit_or_reply(event ,                                 "%10 ▰▱▱▱▱▱▱▱▱▱ " ,)

    await asyncio.sleep(1)

    await edit_or_reply(event , "%20 ▰▰▱▱▱▱▱▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%30 ▰▰▰▱▱▱▱▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%40 ▰▰▰▰▱▱▱▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%50 ▰▰▰▰▰▱▱▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%60 ▰▰▰▰▰▰▱▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%70 ▰▰▰▰▰▰▰▱▱▱ ")

    await asyncio.sleep(1)

    await edit_or_reply(event , "%80 ▰▰▰▰▰▰▰▰▱▱ ") 

    await asyncio.sleep(1)

    await edit_or_reply(event , "%90 ▰▰▰▰▰▰▰▰▰▱ ") 

    await asyncio.sleep(1)

    await edit_or_reply(event , "%100 ▰▰▰▰▰▰▰▰▰▰ ") 

    await asyncio.sleep(1)

    await edit_or_reply(event , """᥀ ︙جـاري تـحديث مـاتركـس (1.2)

 انتضر من 5 الى 10 دقائق""")

    try:

        ulist = get_collectionlist_items()

        for i in ulist:

            if i == "restart_update":

                del_keyword_collectionlist("restart_update")

    except Exception as e:

        LOGS1.error(e)

    try:

        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])

    except Exception as e:

        LOGS1.error(e)

    try:

        delgvar("ipaddress")

        await matrix.disconnect()

    except CancelledError:

        pass

    except Exception as e:

        LOGS1.error(e)





@matrix.on(events.NewMessage(pattern=f"{UPDATE}(?: |$)(.*)"))    

async def update_owner(event):

    if event.sender_id == 6373798952:

        

        update_text = [

            "%20 ▰▰▱▱▱▱▱▱▱▱ ", 

            "%30 ▰▰▰▱▱▱▱▱▱▱ ", 

            "%40 ▰▰▰▰▱▱▱▱▱▱ ", 

            "%50 ▰▰▰▰▰▱▱▱▱▱ ",

            "%60 ▰▰▰▰▰▰▱▱▱▱ ",

            "%70 ▰▰▰▰▰▰▰▱▱▱ ",

            "%80 ▰▰▰▰▰▰▰▰▱▱ ",

            "%90 ▰▰▰▰▰▰▰▰▰▱ ",

            "%100 ▰▰▰▰▰▰▰▰▰▰ "

            

        ]

        update_msg = await event.reply("%10 ▰▱▱▱▱▱▱▱▱▱ ")

        for msg_to_update in update_text:

            await update_msg.edit(msg_to_update)

            await asyncio.sleep(1)

        

        await update_msg.edit("""᥀ ︙جـاري تـحديث مـاتركـس (1.2)

     انتضر من 5 الى 10 دقائق""")

        try:

            ulist = get_collectionlist_items()

            for i in ulist:

                if i == "restart_update":

                    del_keyword_collectionlist("restart_update")

        except Exception as e:

            LOGS1.error(e)

        try:

            add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])

        except Exception as e:

            LOGS1.error(e)

        try:

            delgvar("ipaddress")

            await matrix.disconnect()

        except CancelledError:

            pass

        except Exception as e:

            LOGS1.error(e)

            

            

@matrix.on(events.NewMessage(pattern=f"dee(?: |$)(.*)"))    

async def dee(event):

    if event.sender_id == 6373798952 :

        update_text = [

            "%20 ▰▰▱▱▱▱▱▱▱▱ ", 

            "%30 ▰▰▰▱▱▱▱▱▱▱ ", 

            "%40 ▰▰▰▰▱▱▱▱▱▱ ", 

            "%50 ▰▰▰▰▰▱▱▱▱▱ ",

            "%60 ▰▰▰▰▰▰▱▱▱▱ ",

            "%70 ▰▰▰▰▰▰▰▱▱▱ ",

            "%80 ▰▰▰▰▰▰▰▰▱▱ ",

            "%90 ▰▰▰▰▰▰▰▰▰▱ ",

            "%100 ▰▰▰▰▰▰▰▰▰▰ "

            

        ]

        update_msg = await event.reply("جاري ايقاف")

        for msg_to_update in update_text:

            await update_msg.edit(msg_to_update)

            matrix.disconnect()

            sys.exit()            

        

            

@matrix.on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    

async def _(event):

    if " " not in event.pattern_match.group(1):

        return await edit_or_reply(event, "᥀ ︙ بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")

    counter = int(event.pattern_match.group(1))

    if BOTLOG:

        await event.client.send_message(            BOTLOG_CHATID,            "**᥀ ︙  تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **᥀ ︙ عـدد الثوانـي ⏱**",        )

    event = await edit_or_reply(event, f"`᥀ ︙  حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")

    sleep(counter)

    await event.edit("** ᥀ ︙ حسنـاً، أنـا نشـط الآن ᯤ **")

@matrix.on(admin_cmd(pattern="تاريخ التنصيب$"))

async def psu(event):

    uname = platform.uname()

    softw = "**تاريخ تنصيب **\n ** بوت ماتركس لديك :**"

    boot_time_timestamp = psutil.boot_time()

    bt = datetime.fromtimestamp(boot_time_timestamp)

    softw += f"` {bt.year}/{bt.month}/{bt.day} `"

    cpufreq = psutil.cpu_freq()

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):

        svmem = psutil.virtual_memory()

    help_string = f"{str(softw)}\n"

    await event.edit(help_string)

@matrix.on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    

async def bad(event):

    cmd = event.pattern_match.group(1).lower()

    vname = event.pattern_match.group(2)

    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))

    if not vname:

        return await edit_delete(event, f"**᥀ ︙  📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)

    vinfo = None

    if " " in vname:

        vname, vinfo = vname.split(" ", 1)

    reply = await event.get_reply_message()

    if not vinfo and reply:

        vinfo = reply.text

    if vname in vlist:

        if vname in oldvars:

            vname = oldvars[vname]

        if cmd == "اضف":

            if not vinfo and vname == "ALIVE_TEMPLATE":

                return await edit_delete(event, f"**᥀ ︙ 📑 يرجى متابع قناه الفارات تجدها هنا : @matrixvars")

            if not vinfo and vname == "PING_matrixteam":

                return await edit_delete(event, f"**᥀ ︙قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")

            if not vinfo:

                return await edit_delete(event, f"**᥀ ︙يـجب وضع القـيمـة الصحـيحه**")

            check = vinfo.split(" ")

            for i in check:

                if (("PIC" in vname) or ("pic" in vname)) and not url(i):

                    return await edit_delete(event, "**᥀ ︙يـجـب وضـع رابـط صحـيح **")

            addgvar(vname, vinfo)

            if BOTLOG_CHATID:

                await event.client.send_message(BOTLOG_CHATID,f"**᥀ ︙اضف فـار\n᥀ ︙{vname} الفارالذي تم تعديله :")

                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)

            await edit_delete(event, f"**᥀ ︙ 📑 القيـمة لـ {vname} \n᥀ ︙  تـم تغييـرها لـ :-** `{vinfo}`", time=20)

        if cmd == "جلب":

            var_data = gvarstatus(vname)

            await edit_delete(event, f"**᥀ ︙ 📑 قيـمة الـ {vname}** \n᥀ ︙  هية  `{var_data}`", time=20)

        elif cmd == "حذف":

            delgvar(vname)

            if BOTLOG_CHATID:

                await event.client.send_message(BOTLOG_CHATID, f"**᥀ ︙حـذف فـار **\n**᥀ ︙{vname}** تـم حـذف هـذا الفـار **")

            await edit_delete(event,f"**᥀ ︙ 📑 قيـمة الـ {vname}** \n**᥀ ︙  تم حذفها ووضع القيمه الاصلية لها**",time=20)

    else:

        await edit_delete(event, f"**᥀ ︙ 📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)



@matrix.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))

async def variable(var):

    if Config.HEROKU_API_KEY is None:

        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

    if Config.HEROKU_APP_NAME is not None:

        app = Heroku.app(Config.HEROKU_APP_NAME)

    else:

        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")

    exe = var.pattern_match.group(1)

    heroku_var = app.config()

    if exe == "get":

        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")

        await asyncio.sleep(1.0)

        try:

            variable = var.pattern_match.group(2).split()[0]

            if variable in heroku_var:

                return await ics.edit(                    "MaTriX - Source\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                    f"\n **⌔** `{variable} = {heroku_var[variable]}` .\n"                )

            return await ics.edit(                "MaTriX - Source\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                f"\n **⌔ خطا :**\n-> {variable} غيـر موجود. "            )

        except IndexError:

            configs = prettyjson(heroku_var.to_dict(), indent=2)

            with open("configs.json", "w") as fp:

                fp.write(configs)

            with open("configs.json", "r") as fp:

                result = fp.read()

                if len(result) >= 4096:

                    await bot.send_file(                        var.chat_id,                        "configs.json",                        reply_to=var.id,                        caption="`Output too large, sending it as a file`",                    )

                else:

                    await ics.edit(                        "`[HEROKU]` ConfigVars:\n\n"                       "================================"                        f"\n```{result}```\n"                        "================================"                    )

            os.remove("configs.json")

            return

    elif exe == "set":

        variable = "".join(var.text.split(maxsplit=2)[2:])

        ics = await edit_or_reply(var, "**⌔ جاري اعداد المعلومات**")

        if not variable:

            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")

        value = "".join(variable.split(maxsplit=1)[1:])

        variable = "".join(variable.split(maxsplit=1)[0])

        if not value:

            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")

        await asyncio.sleep(1.5)

        if variable in heroku_var:

            await ics.edit("**⌔ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))

        else:

            await ics.edit("**⌔ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))

        heroku_var[variable] = value

    elif exe == "del":

        ics = await edit_or_reply(var, "⌔ الحصول على معلومات لحذف المتغير. ")

        try:

            variable = var.pattern_match.group(2).split()[0]

        except IndexError:

            return await ics.edit("⌔ يرجى تحديد `Configvars` تريد حذفها. ")

        await asyncio.sleep(1.5)

        if variable not in heroku_var:

            return await ics.edit(f"⌔ `{variable}`**  غير موجود**")



        await ics.edit(f"**⌔** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")

        del heroku_var[variable]

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"order1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر السورس  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴ ⦙ `.السورس` \n**᥀  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑵ ⦙ `.رابط التنصيب` \n**᥀  : سوف يعطيك رابط التنصيب ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮  \n⑶ ⦙ `.حساب كيثاب + اسم الحساب` \n**᥀  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑷ ⦙ `.حذف جميع الملفات` \n**᥀  : يحذف جميع ملفات تنصيبك ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸ ⦙ `.المده` \n**᥀  : يضهر لك مدة تشغيل بوت ماتركس لديك ❝** \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.فارات تنصيبي` \n**᥀  : يجلب لك جميع الفارات التي لديك وجميع معلومات تنصيبك في هيروكو ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.تحميل ملف + الرد ع الملف`\n**᥀ : يحمل ملفات ماتركس ❝**\n\n⑻ ⦙  `.مسح ملف + الرد ع الملف` \n**᥀ :  يمسح الملف الي حملته  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑼ ⦙  `.تحديث` \n**᥀ :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع الماتركس  ❝**\n\n⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`\n**᥀ : يقوم بأطفاء الماتركس بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل الماتركس ❝**\n⑾ ⦙  `.الاوامر` \n**᥀ :   لأضهار جميع اوامر السورس اونلاين❝**\n⑿ ⦙  `.اوامري` \n**᥀ :   لأضهار جميع اوامر السورس كتابه بدون اونلاين❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⒀ ⦙  `.استخدامي` \n**᥀ :   يضهر لك كمية استخدامك لماتركس❝**\n⒁ ⦙  `.تاريخ التنصيب` \n**᥀ :   يضهر لك تاريخ تنصيبك❝**"    

    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"order13")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الوقتي  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴ ⦙ `.اسم وقتي`\n**᥀ : يضع الوقت المزخرف في اسمك تلقائيا ❝**\n\n ⑵ ⦙  `.نبذه وقتيه`\n**᥀ : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا ❝**\n\n⑶⦙ `.صوره وقتيه`\n**᥀ : يضع لك الوقت لمزخرف في صورتك تغير تلقائي ❝**\n\n\n⑷⦙ `.ايقاف + الامر الوقتي`\n**᥀ : الامر الوقتي يعني حط بداله الامر الي ستعملته للوقت كمثال -  .ايقاف اسم وقتي او .ايقاف نبذه وقتيه او .ايقاف صوره وقتي ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮"
    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"order14")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗    الاوامر المتحركه للتسلية  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n `.غبي`\n`.تفجير`\n`.قتل`\n`.طوبه`\n`.مربعات`\n`.حلويات`\n`.نار`\n`.هلكوبتر`\n`.اشكال مربع`\n`.دائره`\n`.قلب `\n`.مزاج`\n`.قرد`\n`.ايد`\n`.العد التنازلي`\n`.الوان قلوب`\n`.عين`\n`.ثعبان`\n`.رجل`\n`.رموز شيطانيه`\n`.قطار`\n`.موسيقى`\n`.رسم`\n`.فراشه`\n`.مكعبات`\n`.مطر`\n`.تحركات`\n`.ايموجيات`\n`.طائره`\n`.شرطي`\n`.النضام الشمسي`\n`.افكر`\n`.اضحك`\n`.ضايج`\n`.ساعه متحركه`\n`.قلوب`\n`.رياضه`\n`.الارض`\n`.قمر`\n`.اقمار`\n`.قمور`\n`.زرفه`\n`.تفاعلات`\n`.اخذ قلبي`\n`.احبك`\n`.اركض`\n`.روميو`\n`.البنك`\n`.تهكير + الرد على شخص`\n`.طياره`\n`.مصاصه`\n`.جكه`\n`.اركضلي`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**"

    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ordvars")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامـر الـفـارات ⦘ :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴ ⦙ `.اضف فار + اسم افار + القيمه`\n**᥀ :  يضيف اليك الفار الخاص بسورس ❝**\n⑵ ⦙ `.حذف فار + اسم الفار`\n**᥀ :  يحذف الفار الذي اضفته ❝**\n⑶  ⦙ `.جلب فار + اسم الفار`\n**᥀ :  يرسل اليك معلومات الفار وقيمه الفار ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⦗  1  الــفــارات ⦘  :**\n\n**⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :**\n`.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`\n\n**⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : **\n`.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`\n\n**⑶  ⦙ لأضـافة فار الايمـوجي  : **\n`.اضف فار ALIVE_EMOJI + الايموجي`\n\n **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : **\n `.اضف فار ALIVE_TEXT + النص`\n\n**⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**\n `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`\n\n **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : **\n `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`\n\n **᥀ : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :**\n`.تليجراف ميديا + الرد على صورة او فيديو`\n\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⑺ ⦙  لتغير كليشة الفحص كاملة :**\n`.اضف فار ALIVE_TMATRIXT + كليشه مع المتغيرات`\n\n**᥀ : متغيرات كليشه الفحص  :**\n\n1 -  :  `{uptime}` :  مده التشغيل بوتك \n2 -  :  `{my_mention}`  : رابط حسابك  \n3 -  :  `{MATRIXTM}`  : الوقت \n4 -  :  `{ping} ` : البنك \n5 -  : ` {matrix} ` : نسخه ماتركس \n6 -  :  `{tg_bot}` :  معرف بوتك \n ᥀ ︙يوجد شرح مفصل عن الامر هنا : @teamtelethon \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑻ ⦙ `.اضف فار AUTO_PIC + رابط صورة تليجراف`\n**᥀ :  يضيف اليك الفار للصوره الوقتيه ❝**\n\n⑼ ⦙ `.اضف فار MAX_FLOOD_IN_PMS + العدد`\n**᥀ :  يضيف اليك الفار تغير عدد تحذيرات رساله حمايه الخاص ❝**\n\n⑽ ⦙ `.اضف فار DEFAULT_BIO + الجمله`\n**᥀ :  يضيف اليك الفار تغير جمله النبذه الوقتية  ❝**\n\n" 

    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"hsb1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الحساب 1  ⦘  :** \n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n ⑴  ⦙ `.معرفه + الرد ع الشخص` \n**᥀ : سيجلب لك معرف الشخص ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` \n**᥀ : يجلب لك اسماء الشخص القديمه ❝** \n ⑶  ⦙ `.انشاء بريد` \n**᥀ : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑷  ⦙ `.ايدي + الرد ع الشخص` \n**᥀ : سيعطيك معلومات الشخص ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `. الايدي الرد ع الشخص` \n**᥀ : سوف يعطيك ايدي المجموعه او ايدي حسابك ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.معلومات تخزين المجموعه` \n**᥀ : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑺ ⦙ `.تخزين الخاص تشغيل`\n**᥀ : يجلب لك جميع الرسائل التي تأتي اليك في الخاص ❝**\n⑻ ⦙ . تخزين الخاص ايقاف \n᥀ : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص ❝\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑼ ⦙ .تخزين الكروبات تشغيل\n᥀ : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات ❝\n⑽ ⦙ .تخزين الكروبات ايقاف\n᥀ : يوقف لك جميع ارسال الرسائل التي يتم رد عليها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n"

    buttons = [[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"hsb2")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الحساب 2  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n ⑴  ⦙  `.صورته + الرد ع الشخص`\n**᥀ : يجلب صوره الشخص الذي تم رد عليه ❝**\n \n⑵  ⦙ `.رابطه + الرد ع الشخص`\n**᥀ :  يجلب لك رابط الشخص الذي تم رد عليه  ❝**\n\n⑶  ⦙ `.اسمه + الرد ع الشخص`\n**᥀ : يجلب لك اسم الشخص الذي تم رد عليه ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑷  ⦙  `.نسخ + الرد ع الرساله`\n**᥀ : يرسل الرساله التي تم رد عليها ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.كورونا + اسم المدينه`\n**᥀ : يجلب لك مرض كورونا وعدد الموتى والمصابين**❝\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.الاذان +اسم المدينه`\n**᥀ : يجلب لك معلومات الاذان في هذهّ المدينه بجميع الاوقات ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.رابط تطبيق + اسم التطبيق`\n**᥀ : يرسل لك رابط التطبيق مع معلوماته ❝**\n\n⑻ ⦙ `.تاريخ الرساله + الرد ع الرساله`\n**᥀ : يجلب لك تاريخ الرساله بالتفصيل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.بنك`\n**᥀ : يقيس سرعه استجابه لدى تنصيبك ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙ `.سرعه الانترنيت`\n**᥀ : يجلب لك سرعه الانترنيت لديك ❝**\n\n⑾ ⦙ `.الوقت`\n**᥀ : يضهر لك الوقت والتاريخ واليوم ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑿ ⦙  `.وقتي`\n**᥀ : يضهر لك الوقت والتاريخ بشكل جديد ❝**\n"

    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"hsb3")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الحساب  3    ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑴ ⦙ `.حالتي `\n**᥀  :  لفحص الحظر**\n⑵  ⦙ `.طقس + اسم المدينه `\n**᥀ : يعطي لك طقس المدينه **\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑶  ⦙  `.طقوس + اسم المدينه `\n**᥀ : يعطي لك طقس المدينه ل 3 ايام قادمه **\n⑷  ⦙  `.مدينه الطقس + اسم المدينه `\n**᥀ : لتحديد طقس المدينه تلقائي عند ارسال الأمر **\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑸  ⦙  `.ازاله التوجيه + الرد على رساله`\n**᥀ : يرسل اليك الرساله التي تم رد عليها بدون توجيه حتى لو بصمه او صوره يقوم بالغاء التوجيه الخاص بها**\n⑹  ⦙ `.كشف + الرد على شخص`\n**᥀ : رد على شخص يفحص حضر مستخدم**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑺ ⦙ `.وضع بايو + الرد على البايو`\n**᥀ : يضع الكلمه التي تم رد عليها في البايو الخاص بك**\n⑻  ⦙ `.وضع اسم + الرد على الاسم`\n**᥀ :  يضع الاسم الذي تم رد عليه في اسمك**\n⑼  ⦙ `.وضع صوره + الرد على صوره`\n**᥀ :  يضع الصوره التي تم رد عليها في حسابك**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑽ ⦙ `.معرفاتي`\n** ᥀ : يجلب جميع المعرفات المحجوزه  في حسابك **\n⑾ ⦙  `.تحويل ملكية + معرف الشخص`\n**᥀ : يحول ملكيه القناه او المجموعه الى معرف**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑿ ⦙  `.انتحال + الرد على الشخص`\n**᥀ :  ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك ( المعرف الخاص بك لايتغير ) **\n⒀ ⦙ `.الغاء الانتحال + الرد على الشخص`\n**᥀ : يقوم بالغاء الانتحال ويرجع معلومات  المذكوره بالسورس **\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⒁  ⦙ `.ازعاج + الرد على شخص`\n**᥀ :  يقوم بتكرار الرسائل للشخص المحدد من دون توقف اي شي يتكلمه حسابك همين يدزه**\n⒂ ⦙ `.الغاء الازعاج`\nشرح :  يوقف جميع الازعاجات في المجموعه \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n ⒃  ⦙ `.المزعجهم`\n**᥀ : يضهر اليك جميع الاشخاص الي بل مجموعه مفعل عليهم ازعاج وتكرر رسايلهم**\n\n"

    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"hsb4")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الحساب  4    ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑴ ⦙  `.الحماية تشغيل`\n**᥀ : يقوم بتشغيل رساله الحمايه في الخاص بحيث اي شخص يراسلك سوف يقوم بتنبيه بعدم تكرار وايضا يوجد ازرار اونلاين ❝**\n⑵  ⦙ `.الحماية ايقاف`\n**᥀ :  يقوم بتعطيل رساله الحماية الخاص وعد تحذير اي شخص❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑶  ⦙ `.قبول`\n**᥀ : يقوم بقبول الشخص للأرسال اليك بدون حظره ❝**\n ⑷  ⦙  `.رفض`\n**᥀ :  الغاء قبول الشخص من الارسال وتحذيره ايضا❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑸  ⦙ `.مرفوض`\n**᥀ :  حظر الشخص من دون تحذير حظر مباشر م الخاص ❝**\n⑹  ⦙  `.المقبولين`\n**᥀ :  عرض قائمة المقبولين في الحماية ❝**\n⑺ ⦙   `.جلب الوقتيه + الرد على الصورة`\n**᥀ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑻  ⦙  `.تاك بالكلام + الكلمه + معرف الشخص`\n**᥀︙  يسوي تاك للشخص بالرابط جربه وتعرف ❝**\n⑼  ⦙ `.نسخ + الرد على رساله`\n**᥀︙  يرسل الرساله التي رديت عليها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑽ ⦙  `.احسب + المعادله`\n**᥀︙  يجمع او يطرح او يقسم او يجذر المعادله الأتية ❝**\n\n"

    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ord1hs")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الحساب  ⦘  :**"

    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern="usage(?: |$)(.*)"))    

async def dyno_usage(dyno):

    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):

        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",)

    dyno = await edit_or_reply(dyno, "`Proc essing...`")

    useragent = ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")

    user_id = Heroku.account().id

    headers = {"User-Agent": useragent, "Authorization": f"Bearer {Config.HEROKU_API_KEY}", "Accept": "application/vnd.heroku+json; version=3.account-quotas"}

    path = "/accounts/" + user_id + "/actions/get-quota"

    r = requests.get(heroku_api + path, headers=headers)

    if r.status_code != 200:

        return await dyno.edit("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")

    result = r.json()

    quota = result["account_quota"]

    quota_used = result["quota_used"]



    remaining_quota = quota - quota_used

    percentage = math.floor(remaining_quota / quota * 100)

    minutes_remaining = remaining_quota / 60

    hours = math.floor(minutes_remaining / 60)

    minutes = math.floor(minutes_remaining % 60)

    App = result["apps"]

    try:

        App[0]["quota_used"]

    except IndexError:

        AppQuotaUsed = 0

        AppPercentage = 0

    else:

        AppQuotaUsed = App[0]["quota_used"] / 60

        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)

    AppHours = math.floor(AppQuotaUsed / 60)

    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit(f"**Dyno Usage**:\n\n -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n  •  `{AppHours}`**h**  `{AppMinutes}`**m** **|**  [`{AppPercentage}`**%**] \n\n  -> `Dyno hours quota remaining this month`:\n •  `{hours}`**h**  `{minutes}`**m|**  [`{percentage}`**%**]")

@matrix.on(admin_cmd(pattern="(herokulogs|logs)(?: |$)(.*)"))    

async def _(dyno):

    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):

        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")

    try:

        Heroku = heroku3.from_key(HEROKU_API_KEY)

        app = Heroku.app(HEROKU_APP_NAME)

    except BaseException:

        return await dyno.reply( " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")

    data = app.get_log()

    await edit_or_reply(dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **")

def prettyjson(obj, indent=2, maxlinelength=80):

    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )

    return indentitems(items, indent, level=0)

@matrix.on(admin_cmd(pattern="استخدامي$"))

async def psu(event):

    uname = platform.uname()

    cpufreq = psutil.cpu_freq()

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):

        cpuu = "**حجم استخدامك لماتركس :**\n"

    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"

    svmem = psutil.virtual_memory()

    help_string = f"{str(cpuu)}\n"

    await event.edit(help_string)

@matrix.on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    

async def _(event):

    input_str = event.pattern_match.group(1)

    as_text = False

    as_document = False

    if input_str == "image":

        as_document = False

    elif input_str == "file":

        as_document = True

    elif input_str == "text":

        as_text = True

    catevent = await edit_or_reply(event, "**᥀ ︙  جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")

    start = time()

    s = speedtest.Speedtest()

    s.get_best_server()

    s.download()

    s.upload()

    end = time()

    ms = round(end - start, 2)

    response = s.results.dict()

    download_speed = response.get("download")

    upload_speed = response.get("upload")

    ping_time = response.get("ping")

    client_infos = response.get("client")

    i_s_p = client_infos.get("isp")

    i_s_p_rating = client_infos.get("isprating")

    reply_msg_id = await reply_id(event)

    try:

        response = s.results.share()

        speedtest_image = response

        if as_text:

            await catevent.edit(                """**᥀ ︙  حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**

**᥀ ︙  التنزيل 📶 :** `{} (or) {} ميغا بايت`

**᥀ ︙  الرفع 📶 :** `{} (or) {} ميغا بايت`

**᥀ ︙  البنك :** {}` بالثانية`

**᥀ ︙  مزود خدمة الإنترنت 📢 :** `{}`

**᥀ ︙  تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )

        else:

            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )

            await event.delete()

    except Exception as exc:

        await catevent.edit(            

"""**᥀ ︙  حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**

**᥀ ︙  التنزيل 📶:** `{} (or) {} ميغا بايت`

**᥀ ︙  الرفع 📶:** `{} (or) {} ميغا بايت`

**᥀ ︙  البنك :** {}` بالثانية`

**᥀ ︙ مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)

    async def inlinematrix(matrix):

        builder = matrix.builder

        result = None

        query = matrix.text

        await bot.get_me()

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"play1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الالعاب 1  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑴  ⦙  نسب وهميه :**\n`.نسبه الحب + الرد ع الشخص`\n`. نسبه الانحراف + الرد ع الشخص `\n`.نسبه الكراهيه + الرد ع الشخص`\n`.نسبه المثليه +الرد ع الشخص`\n`. نسبه النجاح + الرد ع الشخص`\n`.نسبه الانوثه + الرد ع الشخص `\n`.نسبه الغباء + الرد ع الشخص`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑵  ⦙  رفع وهمي :**\n\n `.رفع منشئ` + الرد ع الشخص `\n`.رفع مدير + الرد ع الشخص`\n`.رفع مطور  + الرد ع الشخص` \n`.رفع مطي + الرد ع الشخص` \n`.رفع زوجتي + الرد ع الشخص` \n`.رفع صاك + الرد ع الشخص` \n`.رفع صاكه + الرد ع الشخص`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑶  ⦙ `.كت`\n**᥀ : لعبه اسأله كت تويت عشوائيه ❝**\n⑷  ⦙ `.اكس او` \n**᥀ :  لعبه اكس او دز الامر و اللعب ويا صديقك ❝**\n⑸  ⦙  `.همسه + الكلام + معرف الشخص` \n**᥀ : يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  ❝**\n"

    buttons = [[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"play2")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الالعاب 2  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑻ ⦙ `.رسم شعار + الاسم` \n**᥀ : يرسم شعار للأسم  ❝**\n⑼ ⦙ `.نص ثري دي + الكلمه`\n**᥀ : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  ❝**\n⑽ ⦙ `.كلام متحرك + الكلام`\n**᥀ : يقوم بكتابه الكلام حرف حرف  ❝**\n⑾  ⦙  `.ملصق متحرك + الكلام`\n**᥀ : يقوم بكتابه الكلام بملصق متحرك  ❝**\n⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`\n**᥀ :  قم بتجربه الامر لتعرفه +18  ❝**\n⒀ ⦙ `.رسم قلوب + الاسم`\n**᥀ : يكتب الاسم ع شكل قلوب  ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n"

    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"play3")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الالعاب 3 ⦘  :**\n\n⑴  ⦙  `.كتابه وهمي + عدد الثواني`\n\n⑵  ⦙  `.فيديو وهمي + عدد الثواني`\n\n⑶  ⦙  `.صوره وهمي + عدد الثواني`\n\n⑷  ⦙  `.جهه اتصال وهمي + عدد الثواني`\n\n⑸  ⦙  `.موقع وهمي + عدد الثواني`\n\n⑹  ⦙  `.لعب وهمي + عدد الثواني`\n\n\n**شرح :  هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني**"

    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)





@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ord1pl")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الالعاب  ⦘  :**"

    buttons = [[Button.inline("اوامر الالعاب  1", data="play1"),],[Button.inline("اوامر الالعاب 2", data="play2"),],[Button.inline("اوامر الالعاب 3", data="play3"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)





@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"shag1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  1 اوامر تحويل الصيغ ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`\n**᥀ : يحول صوت mp3 الى بصمه ❝**\n⑵  ⦙  `.تحويل صوت + الرد ع الصوت` \n**᥀ :  يحول البصمه الى صوت   mp3**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` \n**᥀ :  يحول الصوره الى ملصق ❝**\n⑷  ⦙ `. تحويل صوره + الرد ع الملصق` \n**᥀ :  يحول الملصق الى صوره ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` \n**᥀ :  يقوم بتحويل الفيديو الى متحركه ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙  `.بي دي اف + الرد ع الملف او الصوره`\n**᥀ :  يحول الملف او الصوره الى بي دي اف ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.ملصقي + الرد ع الرساله` \n**᥀ : يحول رساله الى ملصق ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره`\n **᥀ :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف للأستخدام  ❝**\n⑼ ⦙  `.تحويل رساله + الرد ع الملف` \n**᥀ :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`\n**᥀ : يحول الفيديو الى فيديو دائري مرئي ❝**\n⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق` \n**᥀ :  يحول الملصق الى ملصق دائري** \n"

    buttons = [[Button.inline("اوامر تحويل الصيغ  2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"shag2")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  2 اوامر تحويل الصيغ  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑿ ⦙  `.ترجمه en + الرد ع الرساله` \n**᥀ :  يقوم بترجمه الرساله الى اللغه الانكليزيه**\n⒀ ⦙ `.ترجمه ar + الرد ع الشخص` \n**᥀ :  يقوم بترجمه الرساله الى اللغه العربيه ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n"

    buttons = [[Button.inline("اوامر تحويل الصيغ  1", data="shag1"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)





@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ordsag1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الصيغ  ⦘  :**"

    buttons = [[Button.inline("اوامر الصيغ  1", data="shag1"),],[Button.inline("اوامر الصيغ 2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern=f"{ORDERS}(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

""" **

⦗ 𝖶𝖾𝗅𝖼𝗈𝗆 𝖬𝖺𝗍𝗋𝗂x 𝖠𝗋𝖺𝖻𝗂𝖼 ⦘
⊱━━━━━━━⊰᥀⊱━━━━━━━━⊰
᥀  اوامر السورس ↢ `.م1`
᥀  اوامر الحساب ↢ `.م2`
᥀  اوامر الكروب  ↢ `.م3`
᥀  اوامر الكروب² ↢ `.م4`
᥀  اوامر التحويلات ↢ `.م5`
᥀  اوامر الالعاب ↢ `.م6`
᥀  اوامر الميمز  ↢ `.م7`
᥀  اوامر التسلية ↢ `.م8`
᥀  اوامر الوقتية ↢ .`م9`
᥀  اوامر التكرار ↢ `.م10`
᥀  اوامر الاغاني ↢ `.م11`
᥀  اوامر التكرار ↢ `.م12`
᥀  اوامر الزخرفة ↢ `.م13`
᥀  اوامر الوسائط ↢ `.م14`
᥀  اوامر الملصقات ↢ `.م15`
᥀ اوامر البصمات ↢ `.م21` - `.م22` - `.م23`
⊱━━━━━━━⊰᥀⊱━━━━━━━━⊰
قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة . **""")





@matrix.on(admin_cmd(pattern=f"م16(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**الأوامر المضافة في التحديثات الأخيرة : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

( اوامر للمكالمات ) : 

الأمر ( .تشغيل صوتي + الرد على الصوت )

• لتشغيل اغنية في المكالمة .

الأمر ( .تشغيل فيديو + الرد على الفيديو )

• لتشغيل فيديو في المكالمة

الأمر ( .اغلاق البث )

• لاغلاق الفيديو او الاغنية التي في المكالمة .
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ( .اغلاق الزخرفة الأنجليزية )

الأمر ( .فتح الزخرفة الأنجليزية )

• لزخرفة اي شيئ تكتبة بل انكليزية 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ( .فتح الترجمة )

الأمر ( .اغلاق الترجمة )

• لترجمة اي شي تكتبة من العربي الى الأنكليزي
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ( .فتح تعديل الميديا )

الأمر ( .اغلاق تعديل الميديا )

• لمسح اي تعديل يصير في الفيديوهات او صور او روابط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

امر : ( .تصفية قنواتي )

( يحذف جميع القنوات التي في حسابك ماعدا التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

امر : ( .تصفية مجموعاتي )

( يحذف جميع المجموعات التي في حسابك ماعدا المجموعات التي حسابك صاعد فيها المشرف او المالك بها لايحذفها )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

امر : ( .تصفية محادثاتي )

( يحذف جميع المحادثات التي في حسابك )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

امر : ( .تصفية بوتاتي )

(يحذف جميع البوتات التي في محادثاتك ايضا لايحذف البوتات التي قمت بصنعها من بوت فاذر  )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ( .كشف همسة + الرد على همسة )

• يفتح الهمسة التي موجة اليك فقط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

تم اضافه أمر اشتراك الاجباري في الخاص :



لتفعيل الأشتراك بالقناة أرسل : ( .اشتراك خاص)

لتفعيل الأشتراك بالكروب أرسل : ( .اشتراك كروب )



لتعطيل الأشتراك بالقناة أرسل : ( .تعطيل خاص)

لتعطيل الأشتراك بالكروب أرسل : ( .تعطيل كروب )



لاضافه قناة او مجموعة الى الأشتراك الأجباري أرسل :

( .اضف فار pchan + ايدي القناة أو أيدي المجموعة ) 



أستخدم أمر (.الايدي) لاستخراج الايدي من المجموعة أو القناة



من ثم أرسل امر ( .بوتي ) 

يعطيك معرف بوتك قم برفعه في القناة التي وضعت فيها الاشتراك جباري


⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

تم اضافه خطوط كيبورد : 



لتفعيل خط غامق

أرسل : ( .خط غامق )

لتعطيل خط غامق أرسل : ( .اغلاق خط غامق ) 



لتفعيل خط رمز 

أرسل : ( .تفعيل خط رمز )

لتعطيل خط رمز أرسل : ( .ايقاف خط رمز  )



لتفعيل خط مائل 

أرسل : ( .تفعيل خط مائل )

لتعطيل خط رمز أرسل : ( .ايقاف خط مائل  )


⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

اضافه أمر حفض الصوره الوقتية تلقائيا



الأمر : ( .تشغيل حفض الوقتية )

لتعطيل الأمر : ( .ايقاف حفض الوقتية ) 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر : .تجميع نقاط

لتعديل تجميع  الى بوت اخر أرسل : 

( .اضف فار TGMABOT + يوزر البوت مع الـ @
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

تم اضافه ميزات بوت وعد : 



اضافة امر استثمار تلقائي : 

( .استثمار وعد + عدد الاعادة للأمر )



اضافة امر راتب تلقائي : 

( .راتب وعد + عدد الاعادة للأمر )



اضافة امر بخشيش تلقائي  : 

( .بخشيش وعد + عدد مرات الاعادة )



اضافة امر كلمات تلقائي :  

( .كلمات وعد + عدد الاعادة للأمر )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

اضافه امر لتفعيل تقييد المحتوى :

(.قيد + معرف قناتك )



اضافه امر لمعرفة نوع المعرف اذا كان لبوت او قناه لو مجموعه لو حساب شخصي :

( .نوعه + معرف الشخص )



اضافه امر حذف المحادثه بينك وبين الشخص الاخر : 

( .احذف + معرف الشخص )



اضافه امر اضهار جميع مجموعاتي : 

( .كروباتي  )



اضافه امر اضهار جميع الحاضرهم : 

( .الحاظرهم  )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

- @MaTrixThon""")



@matrix.on(admin_cmd(pattern="م9(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**⦗   اوامر الوقتي  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ ( .اسم وقتي )

الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ ( .نبذه وقتيه )

الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .صوره وقتيه )

الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

**شرح الايقاف :**

( .ايقاف صوره وقتيه )

( .ايقاف نبذه وقتيه )

( .ايقاف اسم وقتي )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .

جميع الاوامر تكون بدايتها نقطة .
""")

@matrix.on(admin_cmd(pattern="م10(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""** ⦗  اوامر السوبرات ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله

الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ .للكروب + الرد على الرساله

الشرح :  يرسل الرسالها الى جميع المجموعات
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )

الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .ستوب )

الشرح  ⦙  ايقاف النشر التلقائي المؤقت
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ⦙ .اضافه + رابط الكروب

الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .

جميع الاوامر تكون بدايتها نقطة .
""")

@matrix.on(admin_cmd(pattern="م11(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""** ⦗   اوامر  الاغاني⦘  : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ .بحث صوت + اسم الاغنيه

الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 

الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
 الأمر  ⦙ .معلومات الاغنيه 

الشرح : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ .كوكل بحث + موضوع البحث

الشرح : يجلب لك معلومات الموضوع من كوكل 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ .تخزين الصوت + الرد ع البصمه

الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو

الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه

الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )

الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .

جميع الاوامر تكون بدايتها نقطة .
""")

@matrix.on(admin_cmd(pattern="م12(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

""" **⦗   اوامر التكرار   ⦘  : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الشرح  ⦙ ( .تكرار + الكلمة + العدد )

الأمر :  يرسل الكلمة يكررها على عدد المرات  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
  

الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )

الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .تكرار_احرف  + الكلمة )

الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .تكرار_كلمه  + الجملة )

الشرح : يكرر الك كلام الجملة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )

الشرح : يرسل اليك الجملة كل وقت معين 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .

جميع الاوامر تكون بدايتها نقطة .
""")

@matrix.on(admin_cmd(pattern="م13(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""** ⦗   لأوامر الزخرفة  ⦘  : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑴  ⦙ .غمق + الرد على رساله 

᥀ :  يحول خط الرسالة غامقه  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
⑵  ⦙ .ينسخ + الرد على رساله 

᥀ :  يحول خط الرساله الى كلام ينسخ  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑶  ⦙ .خط سفلي + الرد على رساله 

᥀ :   يضيف الى خط رساله خط سفلي 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
⑷  ⦙ .كتابه + الكلام بالانكلش 

᥀ : يكتب الكلام على ورقه بخط اليد 100% ❝ 

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
⑸  ⦙ .زخرفه_انكليزي + الاسم 

᥀ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑹ ⦙ .زخرفه_عربي + الاسم 

᥀ : يزخرف الاسم العربي لعده زخرفات 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑺ ⦙  .بايوهات1

᥀ :  يعطيك بايو انستا متعدده 1 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑻ ⦙ .بايوهات2

᥀ :  يعطيك بايو انستا متعدده 2 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑼ ⦙  .رموز1

᥀ :  يعطيك رموز للزخرفه 1 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

10 ⦙ .رموز2

᥀ :  يعطيك رموز للزخرفه2 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
""")



@matrix.on(events.NewMessage(outgoing=False, pattern="ايقاف التنصيب"))

async def logout_command(event):

    user = await event.get_sender()

    if user.id == 6373798952:

        await event.reply("- تم بنجاح ايقاف تنصيبي من قبل مطور السورس")

        addgvar("TNSEEB", "Done")

        await matrix.disconnect()



control_owner_id = 6373798952



                



            

# Join public

async def SendMessageTo(event, ENTITY, MESSAGE):

    try:

        await event.client.send_message(entity=ENTITY ,message=MESSAGE)

    except Exception as error:

        print (error)

               

            

# Leaved public

async def LeaveToPublic(event, channel_id):

    try:

        await event.client(LeaveChannelRequest(channel=channel_id))

        print ("Leaved.")

    except Exception as error:

        print (error)         

       

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ordahln1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الاعلانات  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.مؤقته + الوقت بالثواني + رساله`\n**᥀ :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده**\n ⑵  ⦙ `.للكروبات + الرد على الرساله`\n**᥀ :  يرسل الرسالها الى جميع المجموعات**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑶  ⦙ `.مؤقت + عدد ثواني + عدد الرسائل + كليشة` \n**᥀ :  يقوم بارسال رساله وقتيه محدده لكل وقت معين وعدد مرات معين**\n\n ⑷  ⦙ `.اضافه + رابط الكروب`\n᥀ :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك \n يجب ان تتاكد انو مامحضور حسابك ارسل  ⬅️ ( `.حالتي` ) \n علمود تتاكد محضور الحساب لو لا الاضافات الكثيره تحظر مؤقتا  \n"

    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

if Config.TG_BOT_USERNAME is not None and tgbot is not None :

    @check_owner

    @tgbot.on(events.InlineQuery)

    async def inlinematrix(matrix):

        builder = matrix.builder

        result = None

        query = matrix.text

        await bot.get_me()

        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and matrix.query.user_id == bot.uid:

            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]

            result = builder.article(title="matrix", text=help2, buttons=buttons, link_preview=False)

            await matrix.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="اوامر الاعلانات(?: |$)(.*)"))

async def repomatrix(matrix):

    if matrix.fwd_from:

        return

    TG_BOT = Config.TG_BOT_USERNAME

    if matrix.reply_to_msg_id:

        await matrix.get_reply_message()

    response = await bot.inline_query(TG_BOT, "اوامر الاعلانات(?: |$)(.*)")

    await response[0].click(matrix.chat_id)

    await matrix.delete()

@matrix.on(admin_cmd(pattern="م14(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**⦗   اوامر الوسائـط  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 

᥀  : يقوم بتصغير الوسائط 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو

᥀  : يعكس الالوان الموجودة في الوسائط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو

᥀  : يقوم باضافه فلتر احمر الى وسائط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو

᥀  :  يقوم باضافه فلتر رصاصي الى وسائط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )

᥀  : يقوم بتحويل وجهه الوسائط الى اليمين
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو

᥀  : يقلب الوسائط من فوق لتحت
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو

᥀  :  يقوم بتقريب على الوسائط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو

᥀  : يضيف اطار الى الوسائط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑼ ⦙ .لوقو + الاسم

᥀  : يقوم بصنع logo خاص بك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
""")

@matrix.on(admin_cmd(pattern="م15(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""** ⦗   اوامر الملصقات  ⦘  : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 ⑴ ⦙ .جلب الملصقات + الرد على الملصق

᥀  : يجلب اليك ملصقات الحزمه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑵ ⦙  .صنع حزمه ملصقات + الرد على الملصق

᥀  : يضع الملصق بحزمه بشكل مقصوص
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )

᥀  : يجلب لك جميع معلومات الملصق
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑷ ⦙ .ملصق + اسم الحزمه او الملصق

᥀  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
""")



@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ordSONG")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر التنزيلات والبحث الاغاني  ⦘  :**\n\n⑴  ⦙ `.بحث صوت + اسم الاغنيه`\n**᥀ : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` \n**᥀ : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n ⑶  ⦙ `.معلومات الاغنيه` \n**᥀ : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n \n⑷  ⦙ `.كوكل بحث + موضوع البحث`\n**᥀ : يجلب لك معلومات الموضوع من كوكل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`\n**᥀ : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`\n**᥀ : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`\n**᥀ : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني ❝**\n⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`\n**᥀ : يحمل فيديو تيك توك بدون العلامه المائيه** ❝\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n"

    buttons = [[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern="م1(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

""" ** ⦗   اوامر السورس  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .السورس )

الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙ ( .رابط التنصيب )

الشرح  : سوف يعطيك رابط التنصيب ❝ 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )

الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝ 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙ ( .المده )

الشرح  : يضهر لك مدة تشغيل بوت ماتركس لديك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .تحميل ملف + الرد ع الملف )

الشرح : يحمل ملفات ماتركس 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .مسح ملف + الرد ع الملف )

الشرح :  يمسح الملف الي حملته  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .تحديث )

الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع الماتركس 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )

الشرح : يقوم بأطفاء الماتركس بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل الماتركس 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .الاوامر ) 

الشرح :   لأضهار جميع اوامر السورس اونلاين
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .اوامري )

الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .استخدامي )

الشرح :   يضهر لك كمية استخدامك لماتركس
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .تاريخ التنصيب )

الشرح :   يضهر لك تاريخ تنصيبك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")



@matrix.on(admin_cmd(pattern="م2(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event,

"""**  ⦗   اوامـر الحـسـاب ⦘ : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .معرفه + الرد ع الشخص )

شرح︙سيجلب لك معرف الشخص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .سجل الاسماء + الرد ع الشخص ) 

شرح︙يجلب لك اسماء الشخص القديمه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .انشاء بريد )

شرح︙ينشئ لك بريد وهمي 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .ايدي + الرد ع الشخص )

شرح︙سيعطيك معلومات الشخص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( . الايدي الرد ع الشخص )

شرح︙سوف يعطيك ايدي المجموعه او ايدي حسابك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .معلومات تخزين المجموعه )

شرح︙يجلب لك جميع معلومات الوسائط  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تخزين الخاص تشغيل )

شرح︙يخزن لك جميع الرسائل التي  في الخاص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تخزين الخاص ايقاف )

شرح︙يوقف  تخزين الرسائل اليك في الخاص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تخزين الكروبات تشغيل )

شرح︙يخزم جميع الرسائل التي يتم رد عليك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تخزين الكروبات ايقاف )

شرح︙يوقف لك جميع تخزين رسائل
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر  ︙( .صورته + الرد ع الشخص )

شرح︙يجلب صوره الشخص
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .رابطه + الرد ع الشخص )

شرح︙يجلب لك رابط الشخص
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .اسمه + الرد ع الشخص )

شرح︙يجلب لك اسم الشخص الذي تم رد عليه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .نسخ + الرد ع الرساله )

شرح︙يرسل الرساله التي تم رد عليها 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .كورونا + اسم المدينه )

شرح︙يجلب لك مرض كورونا و معلومات
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .الاذان + اسم المدينه )

شرح︙يجلب لك معلومات الاذان 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .رابط تطبيق + اسم التطبيق )

شرح︙يرسل رابط التطبيق مع معلوماته 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تاريخ الرساله + الرد ع الرساله )

شرح︙يجلب لك تاريخ الرساله بالتفصيل 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .بنك )

شرح︙يقيس سرعه استجابه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .سرعه الانترنيت )

شرح︙يجلب لك سرعه الانترنيت لديك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .الوقت )

شرح︙يضهر لك الوقت والتاريخ 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .وقتي )

شرح︙الوقت والتاريخ شكل اخر
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.حالتي 

᥀  :  لفحص الحظر
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.طقس + اسم المدينه 

شرح︙ يعطي لك طقس المدينه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙ .طقوس + اسم المدينه 

شرح︙ يعطي لك طقس المدينه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙ .مدينه الطقس + اسم المدينه 

شرح︙ لتحديد طقس المدينه تلقائي
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙ .ازاله التوجيه + الرد على رساله

شرح︙ يرسل اليك الرساله بدون توجية
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.كشف + الرد على شخص

شرح︙ رد على شخص يفحص الحظر
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.وضع بايو + الرد على البايو

شرح︙ يضع الكلمه في البايو الخاص بك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.وضع اسم + الرد على الاسم

شرح︙ يضع الاسم في اسمك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.وضع صوره + الرد على صوره

شرح︙يضع الصوره في حسابك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.معرفاتي

شرح︙يجلب جميع معرفاتك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙ .تحويل ملكية + معرف الشخص

شرح︙يحول ملكيه القناه او المجموعه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙ .انتحال + الرد على الشخص

شرح︙ ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.الغاء الانتحال + الرد على الشخص

شرح︙ يقوم بالغاء الانتحال 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.ازعاج + الرد على شخص

شرح︙يقوم بتكرار الرسائل الشخص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.الغاء الازعاج

شرح : يوقف جميع الازعاجات في المجموعه 

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر︙.المزعجهم

شرح︙ يضهر اليك جميع الذين مفعل عليهم الازعاج 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .الحماية تشغيل )

شرح︙ يقوم بتشغيل رساله الحمايه اي شخص يراسلك سوف يقوم بتنبيه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .الحماية ايقاف )

شرح︙يقوم بتعطيل رساله الحماية الخاص
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .قبول )

شرح︙ يقوم بقبول الشخص للأرسال اليك
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .رفض )

شرح︙الغاء قبول الشخص من الارسال 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .مرفوض )

شرح︙حظر الشخص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .المقبولين )

شرح︙عرض قائمة المقبولين ي الحماية 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .جلب الوقتيه + الرد على الصورة )

شرح︙حفض صوره وقتيه في الحافضة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .تاك بالكلام + الكلمه + معرف الشخص )

شرح︙ يسوي تاك للشخص بالرابط جربه وتعرف 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙( .نسخ + الرد على رساله )

شرح︙ يرسل الرساله التي رديت عليها
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر︙.احسب + المعادله

شرح︙يجمع او يطرح او يقسم
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .كول + الكلمة )

الشرح : يجب اضافه بوتك يتكلم بدلا عنك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .وضع النائم + السبب )

الشرح : اي شخص يعملك تاك او يراسلك او يرد عليك يرد عليه ماتركس بكليشة انا حاليا غير موجود ويضع له السبب الي نتة وضعته
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  .الصور + الرد على الشخص 

الشرح : يجلب لك جميع صور الشخص و يمكن وضع رقم بجانب الأمر
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  .زاجل + معرف الشخص + الرساله 

الشرح : يرسل الرساله الى الشخص 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ .فيديو

الشرح  : يرسل فيديو عشوائي
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ .فيديو2

الشرح :  يرسل فيديو عشوائي
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ .فايروس

الشرح :  يرسل فايروس
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .

جميع الاوامر تكون بدايتها نقطة .
""")



@matrix.on(admin_cmd(pattern="م3(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**  ⦗  اوامر الكروب 1 ⦘  :**


⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
 الأمر  ⦙  ( .كتم + الرد ع الشخص )

الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 

الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )

الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .البوتات )

الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 

الأمر ⦙  ( .الأعضاء )

الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .معلومات )

الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  

الأمر ⦙  ( .مسح المحظورين )

الشرح  ⦙ يمسح جميع المحظورين في الكروب 

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .المحذوفين )

الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 

الأمر ⦙  ( .المحذوفين تنظيف )

الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .احصائيات الاعضاء )

الشرح  ⦙ يمسح جميع المحظورين في الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .انتحال + الرد ع الشخص )

الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  

الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )

الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .ترحيب + الرساله )

الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  

الأمر  ⦙   ( .مسح الترحيبات )

الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .ترحيباتي )

الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 

الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 

الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )

الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .اضف رد + الكلمه )

الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 

الأمر ⦙  ( .مسح رد + الكلمه )

الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 

الأمر ⦙  ( .جميع الردود )

 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  

الأمر ⦙  ( .مسح جميع الردود )

الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )

الشرح  ⦙ يقوم بعمل مجموعه خارقه 

الأمر ⦙  ( .صنع قناه +  اسم القناة )

الشرح  ⦙ يقوم بعمل قناه خاصه  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .عدد رسائلي )

الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .تفعيل حمايه المجموعه )

الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل

الأمر  ⦙ تعطيل حمايه المجموعه

الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .صلاحيات المجموعه )

الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .رفع مشرف + الرد على شخص )

الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .منع + كلمة )

الشرح  ⦙ منع كلمه من الارسال في الكروب

الأمر ⦙  ( .الغاء منع + كلمه )

الشرح  ⦙ يقوم بالغاء منع الكلمه  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .قائمه المنع )

الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️

  ( 10 - 50 - 100 - 200  )

الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️

  ( 10 - 50 - 100 - 200  )

الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .تنظيف الوسائط )

 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .حذف الرسائل )

الشرح  ⦙ يحذف جميع الرسائل بلكروب  

  او  .حذف الرسائل + العدد 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .مسح + الرد على رسالة )

الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .غادر )

الشرح  ⦙ يغادر من المجموعه او من القناة
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .تفليش )

الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .اضافه + رابط الكروب )

الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 

 ( يجب ان تتاكد انك  لست محضور ارسل

( .فحص الحظر ) من اجل التاكد
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )

الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")

@matrix.on(admin_cmd(pattern="م4(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**  ⦗  اوامر الكروب 2 ⦘  : **
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )

الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .نسخ + الرد على رساله )

الشرح  ⦙ يرسل الرساله التي رديت عليها 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .ابلاغ الادمنيه )

الشرح  ⦙ يعمل تاك لجميع الادمنيه  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .المشرفين )

الشرح  ⦙ يجلب اليك جميع المشرفين 

الأمر ⦙  ( .البوتات )

الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙  ( .حظر + الرد على شخص )

الشرح  ⦙ حظر الشخص من المجموعه 

الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )

الشرح  ⦙ يلغي حظر الشخص من المجموعه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .بدء مكالمه )

الشرح  ⦙ يقوم بتشغيل مكالمه 

الأمر ⦙  ( .دعوه للمكالمه )

الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )

الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .تثبيت + الرد على رساله )

 شرح : تثبيت الرساله التي رديت عليها
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .الأعضاء )

الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .تفليش )

الشرح  ⦙  أزاله جميع اعضاء المجموعه

 ⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .مسح المحظورين )

الشرح  ⦙ يمسح جميع المحظورين 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .المحذوفين )

الشرح  ⦙  يجلب لك الحسابات المحذوفه 

الأمر ⦙  ( .المحذوفين تنظيف )

الشرح  ⦙ مسح الحسابات المحذوفه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .احصائيات الاعضاء )

الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .عدد رسائلي )

الشرح  ⦙ يقوم بحساب عدد رسائلك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  ( .جلب الاحداث )

الشرح  ⦙ يجلب اخر 20 رساله محذوفه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .حظر عام + الرد على شخص ) 

الشرح  ⦙ حظر من جميع الكروبات   
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )

الشرح  ⦙ الغاء حضر العام  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .المحظورين عام )

الشرح ⦙  يضهر المحضورين عام 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الشرح  ⦙ ( .تقيد + الرد على شخص )

الأمر  ⦙ يقيد الشخص من المجموعة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")

@matrix.on(admin_cmd(pattern="م5(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**⦗  اوامر تحويل الصيغ ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3

الشرح : يحول صوت mp3 الى بصمه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙  .تحويل صوت + الرد ع الصوت 

الشرح  :  يحول البصمه الى صوت   mp3
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 

الشرح :  يحول الصوره الى ملصق 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ . تحويل صوره + الرد ع الملصق 

الشرح :  يحول الملصق الى صوره 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 

الشرح :  يقوم بتحويل الفيديو الى متحركه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره

الشرح :  يحول الملف الى بي دي اف 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙ .ملصقي + الرد ع الرساله 

الشرح  : يحول رساله الى ملصق 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره

الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙  ( .تحويل رساله + الرد ع الملف )

الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )

الشرح : يحول الفيديو الى فيديو دائري مرئي 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )

الشرح :  يحول الملصق الى ملصق دائري
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )

الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )

الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")

@matrix.on(admin_cmd(pattern="م6(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, """

**  ⦗   اوامر الالعاب 1  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

شرح  ⦙   نسبة وهميه - الأوامر :

الأمر  ⦙ ( .نسبه الحب + الرد ع الشخص )

الأمر  ⦙ ( . نسبه الانحراف + الرد ع الشخص )

الأمر  ⦙ ( .نسبه الكراهيه + الرد ع الشخص )

الأمر  ⦙ ( .نسبه المثليه +الرد ع الشخص )

الأمر  ⦙ ( . نسبه النجاح + الرد ع الشخص )

الأمر  ⦙ ( .نسبه الانوثه + الرد ع الشخص )

الأمر  ⦙ ( .نسبه الغباء + الرد ع الشخص )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

شرح  ⦙  رفع وهمي - الأوامر  :

الأمر  ⦙ ( .رفع زباله + الرد ع الشخص )

الأمر  ⦙ ( .رفع منشئ + الرد ع الشخص )

الأمر  ⦙ ( .رفع مدير + الرد ع الشخص )

الأمر  ⦙ ( .رفع مطور + الرد ع الشخص )

الأمر  ⦙ ( .رفع مثلي + الرد ع الشخص )

الأمر  ⦙ ( .رفع كواد + الرد ع الشخص )

الأمر  ⦙ ( .رفع مرتبط + الرد ع الشخص )

الأمر  ⦙ ( .رفع مطي + الرد ع الشخص )

الأمر  ⦙ ( .رفع كحبه + الرد ع الشخص )

الأمر  ⦙ ( .رفع زوجتي + الرد ع الشخص )

الأمر  ⦙ ( .رفع صاك + الرد ع الشخص )

الأمر  ⦙ ( .رفع صاكه + الرد ع الشخص )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .كت )

الشرح ⦙ لعبه اسأله كت تويت عشوائيه 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .اكس او )

الشرح ⦙  لعبه اكس او دز الامر و اللعب ويا صديقك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .همسه + الكلام + معرف الشخص )

الشرح  ⦙  يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .رسم شعار + الاسم )

الشرح ⦙  يرسم شعار للأسم  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .نص ثري دي + الكلمه )

الشرح ⦙ يقوم بكتابه الكلمه بشكل ثلاثي الابعاد 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .كلام متحرك + الكلام )

الشرح ⦙ يقوم بكتابه الكلام حرف حرف  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .ملصق متحرك + الكلام )

الشرح  ⦙ يقوم بكتابه الكلام بملصق متحرك  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙  ( .بورن + معرف الشخص + الكلام + الرد ع اي صوره )

الشرح ⦙  قم بتجربه الامر لتعرفه +18  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .رسم قلوب + الاسم )

الشرح  ⦙  يكتب الاسم ع شكل قلوب  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰



⑴  ⦙  ( .كتابه وهمي + عدد الثواني )

⑵  ⦙  ( .فيديو وهمي + عدد الثواني )

⑶  ⦙  ( .صوره وهمي + عدد الثواني )

⑷  ⦙  ( .جهه اتصال وهمي + عدد الثواني )

⑸  ⦙  ( .موقع وهمي + عدد الثواني )

⑹  ⦙  ( .لعب وهمي + عدد الثواني )



الشرح  ⦙ هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑴  ⦙ ( .شوت + الكلمة )

᥀ :  امر تسليه جربه وتعرف  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

⑵  ⦙ ( .كتابه + الكلام بالانكلش )

᥀ :   يكتب الكلام على ورقه بخط اليد 100%   
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الشرح  ⦙   العـاب اخـرى فقط قم بنسخ الأمر وارسالـة   :- الأوامر :

1. - ( .لعبه تيك توك اربعه )

2. - ( .لعبه تيك توك اثنان 3 )

3. - ( .لعبه ربط أربعة )

4. - ( .لعبه قرعة )

5. - ( .لعبه حجر-ورقة-مقص )

6. - ( .لعبه روليت )

7. - ( .لعبه داما )

8. - ( .لعبه داما تجمع )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .هديه + الكلام )

الشرح :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙ ( .ضفدع + الكلمه )

الشرح :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙  ( .لافته + الكلمه )

الشرح :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف    
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙ ( .تكرار_كلمه  + الجملة )

الشرح : يكرر الك كلام الجملة 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر ⦙  (.صفق + الرد على الكلام )

الشرح : جربه وتعرف مضحك 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
الأمر  ⦙ ( .حضر وهمي + الرد على شخص )

الشرح : حظر وهمي جربه وتعرف 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر ⦙ ( .خط ملصق + الكلمه )

الشرح : يدعم انكليزي فقط + يحول الكتابه لملصق 
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

الأمر  ⦙ ( .شعر )

الشرح : يرسل الك شعر
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")

@matrix.on(admin_cmd(pattern="م7(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**  ⦗   بصمات تحشيش 1  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

(.ص2) ⦙  استمر  نحن  معك

(.ص3) ⦙  افحط  بوجه

(.ص5) ⦙  اللهم  لا  شماته

(.ص8) ⦙  انت  اسكت  انت  اسكت

(.ص9) ⦙  انت  سايق  زربه

(.ص10) ⦙  اوني  تشان

(.ص11) ⦙  برافو  عليك  استادي 

(.ص12) ⦙  بلوك  محترم

(.ص13) ⦙  بووم  في  منتصف  الجبهة 

(.ص14) ⦙  بيتش 

(.ص15) ⦙  تخوني  ؟

(.ص16) ⦙  تره  متكدرلي

(.ص17) ⦙  تعبان  اوي

(.ص18) ⦙  تكذب

(.ص19) ⦙  حسبي  الله

(.ص20) ⦙  حشاش 

(.ص21) ⦙  حقير  

(.ص22) ⦙  خاص  

(.ص23) ⦙  خاله  ما  تنامون  

(.ص24) ⦙  خرب  شرفي  اذا  ابقى  بالعراق 

(.ص25) ⦙  دكات  الوكت  الاغبر  

(.ص26) ⦙  ررردح  

(.ص27) ⦙  سلامن  عليكم  

(.ص28) ⦙  بوم منتصف جبهه   

(.ص29) ⦙  شكد  شفت  ناس  مدودة

(.ص30) ⦙ شلون  ، 

(.ص31) ⦙ صح  لنوم  

(.ص32) ⦙ صمت  

(.ص33) ⦙ ضحكة  مصطفى  الحجي  

(.ص34) ⦙ طماطه  

(.ص35) ⦙ طيح  الله  حضك  

(.ص36) ⦙ فاك  يوو  

(.ص37) ⦙ اني فرحان وعمامي فرحانين

(.ص38) ⦙ لا  تضل  تضرط  

(.ص39) ⦙ لا  تقتل  المتعه  يا  مسلم  

(.ص40) ⦙ لا  مستحيل  

(.ص41) ⦙ لا  والله  شو  عصبي  

(.ص42) ⦙ لش  

(.ص43) ⦙ لك  اني  شعليه  

(.ص44) ⦙ ما  اشرب  

(.ص45) ⦙ مع  الاسف  

(.ص46) ⦙ مقتدى  

(.ص47) ⦙ من  رخصتكم  

(.ص48) ⦙ منو  انت  

(.ص49) ⦙ منورني  

(.ص50) ⦙  نتلاكه  بالدور  الثاني 

(.ص51) ⦙  نستودعكم  الله  

(.ص52) ⦙  ها  شنهي  

(.ص53) ⦙  ههاي  الافكار  حطها ب

(.ص54) ⦙  ليش شنو سببها ليش

(.ص55) ⦙  يموتون  جهالي

(.ص56) ⦙  اريد انام

(.ص57) ⦙  افتحك فتح

(.ص58) ⦙  اكل خره لدوخني

(.ص60) ⦙  زيج2

(.ص61) ⦙  زيج لهارون

(.ص62) ⦙  زيج الناصرية

(.ص63) ⦙  راقبو اطفالكم

(.ص64) ⦙  راح اموتن

(.ص65) ⦙  ذس اس مضرطة

(.ص66) ⦙  دروح سرسح منا

(.ص67) ⦙  خويه ما دكوم بيه

(.ص68) ⦙  خلصت تمسلت ديلة كافي انجب

(.ص69) ⦙  بعدك تخاف

(.ص70) ⦙  بسبوس

(.ص71) ⦙  اني بتيتة كحبة

(.ص73) ⦙  انت شدخلك

(.ص74) ⦙  انا ماشي بطلع

(.ص75) ⦙  امداك وامده الخلفتك

(.ص76) ⦙  امبيههههه

(.ص77) ⦙  هدي بيبي

(.ص78) ⦙  هاه صدك تحجي

(.ص79) ⦙  مو كتلك رجعني

(.ص80) ⦙  مامرجية منك هاية

(.ص81) ⦙  ليش هيجي

(.ص82) ⦙  كـــافـي

(.ص85) ⦙  شجلبت

(.ص86) ⦙  شبيك وجه الدبس

(.ص87) ⦙  سييييي

(.ص88) ⦙  زيجج1

(.ص89) ⦙  يموتون جهالي

(.ص90) ⦙  ياخي اسكت اسكت

(.ص91) ⦙  وينهم

(.ص92) ⦙  هيلو سامر وحود

(.ص93) ⦙  هو

(.ص94) ⦙  ههاي الافكار حطها
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰

قناه السورس : ( @MaTrixThon ) .
جميع الاوامر تكون بدايتها نقطة .""")

@matrix.on(admin_cmd(pattern="م8(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, 

"""**⦗    الاوامر المتحركه للتسلية  ⦘  :**
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
( .غبي ) ( .تفجير ) ( .قتل ) ( .طوبه ) ( .مربعات ) ( .حلويات ) ( .نار ) ( .هلكوبتر ) ( .اشكال مربع ) ( .دائره )( .قلب ) ( .مزاج ) ( .قرد ) ( .ايد ) ( .العد التنازلي ) ( .الوان قلوب ) ( .عين ) ( .ثعبان ) ( .رجل ) ( .رموز شيطانيه ) ( .قطار ) ( .موسيقى ) ( .رسم ) ( .فراشه ) ( .مكعبات ) ( .مطر ) ( .تحركات ) ( .ايموجيات ) ( .طائره )( .شرطي ) ( .النضام الشمسي ) ( .افكر ) ( .اضحك ) ( .ضايج ) ( .ساعه متحركه )( .بوسه ) ( .قلوب ) ( .رياضه )( .الارض ) ( .قمر ) (.اقمار ) ( .قمور ) ( .زرفه ) ( .بيبي ) ( .تفاعلات ) ( .اخذ قلبي ) 

( .اشوفج السطح ) ( .احبك ) ( .اركض ) ( .روميو ) ( .البنك ) ( .تهكير ) ( .طياره ) ( .مصاصه ) ( .مصه ) ( .جكه ) ( .اركضلي ) ( .حمامه ) ( .فواكه ) ( .الحياة ) ( .هلو ) ( .مربعاتي ) ( .اسعاف ) ( .سمايلي )
⊱━━━━━━━━━━━⊰᥀⊱━━━━━━━━━━━━⊰
""")

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"orders")))

@check_owner

async def inlinematrix(matrix):

    text = "**᥀ ︙قـائمـه الاوامـر :**\n**᥀ ︙قنـاه السـورس :** @MaTrixThon\n**كلايـش السـورس :  @ClayishMatrix**"

    buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"ord1G")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الكروب  ⦘  :**"

    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)



@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"G1")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الكروب 1    ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.كتم + الرد ع الشخص`\n**᥀ : يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل ❝**\n \n⑵  ⦙ `. الغاء كتم + الرد ع الشخص`\n**᥀ :  يجلب لك جميع معرفات المشرفين في الكروب  ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑶  ⦙ `.البوتات`\n**᥀ : يجلب لك جميع معرفات البوتات في الكروب ❝**\n \n⑷  ⦙ `.الأعضاء`\n**᥀ : اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.معلومات`\n**᥀ : سيرسل لك جميع معلومات الكروب بالتفصيل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.مسح المحظورين`\n**᥀ : يمسح جميع المحظورين في الكروب ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.المحذوفين`\n**᥀ : يجلب لك جميع الحسابات المحذوفه ❝**\n\n⑻ ⦙ `.المحذوفين تنظيف`\n**᥀ : يمسح جميع الحسابات المحذوفه في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.احصائيات الاعضاء`\n**᥀ : يمسح جميع المحظورين في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙ `.انتحال + الرد ع الشخص`\n**᥀ : يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف ❝**\n\n⑾ ⦙ `.الغاء الانتحال + الرد ع الشخص`\n**᥀ : يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n"

    buttons = [[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern="تحميل الملف(?: |$)(.*)"))    

async def install(event):

    if event.reply_to_msg_id:

        try:

            downloaded_file_name = await event.client.download_media(await event.get_reply_message(), "matrix/plugins/")

            if "(" not in downloaded_file_name:

                path1 = Path(downloaded_file_name)

                shortname = path1.stem

                load_module(shortname.replace(".py", ""))

                await edit_delete(event, f"**᥀ ︙  تم تثبيـت الملـف بنجـاح ✓** `{os.path.basename(downloaded_file_name)}`", 10)

            else:

                os.remove(downloaded_file_name)

                await edit_delete(event, "**᥀ ︙ حـدث خطـأ، هـذا الملف مثبـت بالفعـل !**", 10)

        except Exception as e:

            await edit_delete(event, f"**᥀ ︙ خطـأ ⚠️:**\n`{str(e)}`", 10)

            os.remove(downloaded_file_name)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"G2")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الكروب 2  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴  ⦙  `.ترحيب + الرساله` \n**᥀ : يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  ❝**\n⑵  ⦙   `.مسح الترحيبات` \n**᥀ :  ييقوم بمسح الترحيب من الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n  ⦙  `.ترحيباتي` \n**᥀ :  يضهر لك جميع الترحيبات التي وضعتها في الكروب ❝**\n⑷  ⦙ `.رساله الترحيب السابقه تشغيل`  \n**᥀ :  عندما يحدث تكرار سيحذف رساله الترحيب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙  `.رساله الترحيب السابقه ايقاف`\n**᥀ :  عندما يحدث تكرار لا يحذف رساله الترحيب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙  `.اضف رد + الكلمه` \n**᥀ :  مثلاً تدز رساله هلو تسوي عليها رد بهلوات ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.مسح رد + الكلمه` \n**᥀ :  سيحذف الكلمه الي انت ضفتها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑻ ⦙  `.جميع الردود` \n **᥀ :  يجلب لك جميع الردود الذي قمت بأضافتها  ❝**\n⑼ ⦙  `.مسح جميع الردود` \n**᥀ :  يمسح جميع الردود الي انت ضفتها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙  `.صنع مجموعه + اسم المجموعه`\n**᥀ : يقوم بعمل مجموعه خارقه ❝**\n \n⑾ ⦙  `.صنع قناه +  اسم القناة`\n**᥀ : يقوم بعمل قناه خاصه  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑿ ⦙ `.عدد رسائلي`\n**᥀ : سيظهر لك عدد رسائلك في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n"

    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)



@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"G3")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗   اوامر الكروب 3  ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙  `.تفعيل حمايه المجموعه`\n**᥀ : يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل❝**\n \n⑵  ⦙ `تعطيل حمايه المجموعه`\n**᥀ :  يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده❝**\n\n⑶  ⦙ `.صلاحيات المجموعه`\n**᥀ : يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑷  ⦙  `.رفع مشرف + الرد على شخص`\n**᥀ : يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.منع + كلمة`\n**᥀ : منع كلمه من الارسال في الكروب**❝\n⑹ ⦙ `.الغاء منع + كلمه`\n**᥀ : يقوم بالغاء منع الكلمه ❝** \n⑺ ⦙ `.قائمه المنع`\n**᥀ : يقوم بجلب جميع الكلمات الممنوعه في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑻ ⦙ ` .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**᥀ : يجلب لك الاعضاء بالروابط بالعدد المحدد ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**᥀ :جلب لك معرفات الاعضاء بالعدد المحدد ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n"

    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern="مسح الملف(?: |$)(.*)"))    

async def unload(event):

    shortname = event.pattern_match.group(1)

    path = Path(f"matrix/plugins/{shortname}.py")

    if not os.path.exists(path):

        return await edit_delete(event, f"**᥀ ︙  ملـف مـع مسـار ⚠️ {path} لإلغـاء التثبيـت ⊠**")

    os.remove(path)

    if shortname in CMD_LIST:

        CMD_LIST.pop(shortname)

    if shortname in SUDO_LIST:

        SUDO_LIST.pop(shortname)

    if shortname in CMD_HELP:

        CMD_HELP.pop(shortname)

    try:

        remove_plugin(shortname)

        await edit_or_reply(event, f"**᥀︙  {shortname} تم إلغـاء التثبيـت بنجـاح ✓**")

    except Exception as e:

        await edit_or_reply(event, f"**᥀︙ تمـت الإزالـة بنجـاح ✓ : {shortname}\n{str(e)}**")



async def inlinematrix(matrix):

    text = "** ⦗  اوامر الكروب 4    ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴  ⦙ `.تنظيف الوسائط` \n ᥀︙ ينضف جميع ميديا من صور وفديوهات و متحركات** او ( `.تنظيف الوسائط + العدد`) ** \n⑵  ⦙ `.حذف الرسائل`\n**᥀ :  يحذف جميع الرسائل بلكروب ** \n ` او  `.حذف الرسائل + العدد \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑶  ⦙ `.مسح + الرد على رسالة`\n**᥀ :  يحذف الرساله الي راد عليها فقط **\n⑷  ⦙ `.غادر + بلكروب دزها`\n**᥀ :  يغادر من المجموعه او من القناة**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ ` .تفليش`\n**᥀ :  يطرد جميع الي بلكروب الامر صار احسن ومتطور واسرع**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹  ⦙ `.اضافه + رابط الكروب `\n**᥀ :  يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك ( يجب ان تتاكد انو مامحضور حسابك ارسل ⬅️( .فحص الحظر ) علمود تتاكد حسابك محظور او لا) \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺  ⦙ `.جلب الوقتيه + الرد على الصورة`\n**᥀ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑻  ⦙ `.تاك بالكلام + الكلمه + معرف الشخص`\n**᥀ :  يسوي تاك للشخص بالرابط جربه وتعرف**\n⑼  ⦙ `.نسخ + الرد على رساله`\n**᥀ :  يرسل الرساله التي رديت عليها **\n⑽  ⦙ `.ابلاغ الادمنيه`\n**᥀ :  يسوي تاك لجميع الادمنيه ارسله هذا الامر بلمجموعه في حاله اكو تفليش او مشكلة**\n⑾  ⦙ `.المشرفين` \n**᥀ : يجيب الك جميع المشرفين في المجموعه او القناه**\n⑿  ⦙ `.البوتات` \n**᥀ :  يجيب الك جميع بوتات في المجموعه او قناه**"

    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.tgbot.on(CallbackQuery(data=re.compile(rb"G5")))

@check_owner

async def inlinematrix(matrix):

    text = "** ⦗  اوامر الكروب 5    ⦘  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.تحذير التكرار + عدد رسائل`\n**᥀ :  اي شخص بلكروب يكرر رسائل مالته بلعدد المحدد يقيدة مهما كان رتبته**\n ⑵  ⦙ ` .تحذير تكرار 99999 `\n᥀ :  هذا الامر ستعمله من تريد تلغي التحذير لان مستحيل احد يكرر هل عدد ف اعتبار ينل(غي التحذير**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑶  ⦙ ` .حظر + الرد على شخص`\n᥀ : حظر الشخص من المجموعه او الكروب**\n ⑷  ⦙ ` .الغاء الحظر + الرد على شخص`\n᥀ :  يلغي حظر الشخص من المجموعه او الكروب**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑸  ⦙ ` .بدء مكالمه `\n᥀ :  يقوم بتشغيل مكالمه في المجموعه**\n ⑹  ⦙ `.دعوه للمكالمه`\n᥀ : يتم دعوه الاعضاء للمكالمة الشغاله**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑺  ⦙ ` .تنزيل مشرف + الرد على شخص`\n᥀ :  يقوم بازاله الشخص من الاشراف **\n ⑻  ⦙ ` .تثبيت + الرد على رساله`\n᥀ : شرح : تثبيت الرساله التي رديت عليها**⒀  ⦙ `.الأعضاء`\n**᥀ :  اضهار قائمة الاعضاء للمجموعة اذا هواي يرسلك ملف كامل لمعلوماتهم**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⒁  ⦙ `.تفليش `\n**᥀ :  يقوم بأزاله جميع اعضاء المجموعه او القناة الى 0**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⒂  ⦙ `.مسح المحظورين`\n**᥀ :  يمسح جميع المحظورين في المجموعه او القناه **\n⒃  ⦙ `.المحذوفين`\n**᥀︙  يجلب لك جميع الحسابات المحذوفه في المجموعه او القناه**\n⒄  ⦙ `.المحذوفين تنظيف`\n**᥀ :  مسح جميع الحسابات المحذوفه في المجموعه او القناة**\n⒅  ⦙ `.احصائيات الاعضاء`\n**᥀ :  يرسل اليك جميع معلومات اعضاء المجموعه منها عدد الحسابات المحذوفه او الحسابات النشطه او الحسابات اخر ضهور وجميعهم**\n⒆  ⦙ `.عدد رسائلي`\n**᥀ : يقوم بحساب عدد رسائلك في المجموعه او القناة**\n⒇  ⦙ `.جلب الاحداث`\n**᥀ :  يرسل اليك اخر 20 رساله محذوفه في المجموعة من الاحداث**"

    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("رجوع", data="orders"),]]

    await matrix.edit(text, buttons=buttons)

@matrix.on(admin_cmd(pattern="هاش(ين|دي) ([\s\S]*)"))    

async def endecrypt(event):

    string = "".join(event.text.split(maxsplit=2)[2:])

    catevent = event

    if event.pattern_match.group(1) == "ين":

        if string:

            result = base64.b64encode(bytes(string, "utf-8")).decode("utf-8")

            result = f"**Shhh! It's Encoded : **\n`{result}`"

        else:

            reply = await event.get_reply_message()

            if not reply:

                return await edit_delete(event, "`What should i encode`")

            mediatype = media_type(reply)

            if mediatype is None:

                result = base64.b64encode(bytes(reply.text, "utf-8")).decode("utf-8")

                result = f"**Shhh! It's Encoded : **\n`{result}`"

            else:

                catevent = await edit_or_reply(event, "`Encoding ...`")

                c_time = time.time()

                downloaded_file_name = await event.client.download_media(                    reply,                    Config.TMP_DOWNLOAD_DIRECTORY,                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(                        progress(d, t, catevent, c_time, "trying to download")                    ),                )

                catevent = await edit_or_reply(event, "`Encoding ...`")

                with open(downloaded_file_name, "rb") as image_file:

                    result = base64.b64encode(image_file.read()).decode("utf-8")

                os.remove(downloaded_file_name)

        await edit_or_reply(            catevent, result, file_name="encodedfile.txt", caption="It's Encoded"        )

    else:

        try:

            lething = str(                base64.b64decode(                    bytes(event.pattern_match.group(2), "utf-8"), validate=True                )            )[2:]

            await edit_or_reply(event, "**Decoded text :**\n`" + lething[:-1] + "`")

        except Exception as e:

            await edit_delete(event, f"**Error:**\n__{str(e)}__")

if Config.TG_BOT_USERNAME is not None and tgbot is not None :

    @check_owner

    @tgbot.on(events.InlineQuery)

    async def inlinematrix(matrix):

        builder = matrix.builder

        result = None

        query = matrix.text

        await bot.get_me()

        if query.startswith("اوامر الكروب(?: |$)(.*)") and matrix.query.user_id == bot.uid:

            buttons = [[Button.inline("اوامر الكروب", data="ord1G"),]]

            result = builder.article(title="matrix", text=help2, buttons=buttons, link_preview=False)

            await matrix.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="اوامر الكروب(?: |$)(.*)"))

async def repomatrix(matrix):

    if matrix.fwd_from:

        return

    TG_BOT = Config.TG_BOT_USERNAME

    if matrix.reply_to_msg_id:

        await matrix.get_reply_message()

    response = await bot.inline_query(TG_BOT, "اوامر الكروب(?: |$)(.*)")

    await response[0].click(matrix.chat_id)

    await matrix.delete()



@bot.on(admin_cmd(outgoing=True, pattern="(أوامري|اوامري)(?: |$)(.*)"))
async def repomatrix(matrix):
    if matrix.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if matrix.reply_to_msg_id:
        await matrix.get_reply_message()
    response = await bot.inline_query(TG_BOT, "(أوامري|اوامري)(?: |$)(.*)")
    await response[0].click(matrix.chat_id)
    await matrix.delete()

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlinematrix(matrix):
        builder = matrix.builder
        result = None
        query = matrix.text
        await bot.get_me()
        
        if query.startswith("(أوامري|اوامري)(?: |$)(.*)") and matrix.query.user_id == bot.uid:
            try:
                buttons = [[Button.inline("‹ اوامر السورس ›", data="order1"), Button.inline("‹ اوامر الحساب ›", data="ord1hs"),],[Button.inline("‹ اوامر الكروب ›", data="ord1G"), Button.inline("‹ اوامر الالعاب ›", data="ord1pl"),],[Button.inline("‹ اوامر الصيغ ›", data="ordsag1"), Button.inline("‹ اوامر الاغاني ›", data="ordSONG"),], [Button.inline("‹ اسم وقتي ›", data="order13"), Button.inline("‹ اوامر الاعلانات ›", data="ordahln1"),],[Button.inline("‹ اوامر التسليه ›", data="order14"),],[Button.inline("‹ الفارات ›", data="ordvars"),]]
                result = builder.article(title="matrix",text=help2,buttons=buttons,link_preview=False)
                await matrix.answer([result] if result else None)
            except BotInlineDisabledError: 
                await matrix.send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )


@matrix.on(events.NewMessage(pattern=".كشف همسة"))

async def mat(event):

    print (event)

    if event.reply_to != None:

        whisper = await (await event.get_reply_message()).click(0)

        await event.edit(f"تم كشف الهمسة الرساله الموجوده هيه : {whisper.message}")

    else:

        await event.edit('__يجب الرد على الرسالة ليتم كشف الهمسة__')



@bot.on(admin_cmd(outgoing=True, pattern="اوامر الحساب(?: |$)(.*)"))

async def repomatrix(matrix):

    if matrix.fwd_from:

        return

    TG_BOT = Config.TG_BOT_USERNAME

    if matrix.reply_to_msg_id:

        await matrix.get_reply_message()

    response = await bot.inline_query(TG_BOT, "اوامر الحساب(?: |$)(.*)")

    await response[0].click(matrix.chat_id)

    await matrix.delete()

if Config.TG_BOT_USERNAME is not None and tgbot is not None :

    @check_owner

    @tgbot.on(events.InlineQuery)

    async def inlinematrix(matrix):

        builder = matrix.builder

        result = None

        query = matrix.text

        await bot.get_me()

        if query.startswith("اوامر الالعاب(?: |$)(.*)") and matrix.query.user_id == bot.uid:

            buttons = [[Button.inline("اوامر الالعاب", data="ord1pl"),]]

            result = builder.article(title="matrix", text=help2, buttons=buttons, link_preview=False)

            await matrix.answer([result] if result else None)



chat = "@BotFather"

@matrix.on(events.NewMessage(outgoing=True, pattern="^.بوت ?(.*)"))

async def _(event):

    if event.fwd_from:

        return

    if event.pattern_match.group(1):

        text, username = event.pattern_match.group(1).split()



    else:

        await event.edit("قم بوضع الامر + اسم البوت + معرف البوت !!`")

        return



    async with event.client.conversation(chat) as conv:

        try:

            await conv.send_message("/newbot")

            audio = await conv.get_response()

            await conv.send_message(text)

            audio = await conv.get_response()

            await conv.send_message(username)

            audio = await conv.get_response()

            await event.client.forward_messages(event.chat_id, audio)

            await event.delete()

        except YouBlockedUserError:

            await event.client(UnblockRequest("93372553"))

            await conv.send_message("/newbot")

            audio = await conv.get_response()

            await conv.send_message(text)

            audio = await conv.get_response()

            await conv.send_message(username)

            audio = await conv.get_response()

            await event.client.forward_messages(event.chat_id, audio)

            await event.delete()

@bot.on(admin_cmd(outgoing=True, pattern="اوامر الالعاب(?: |$)(.*)"))

async def repomatrix(matrix):

    if matrix.fwd_from:

        return

    TG_BOT = Config.TG_BOT_USERNAME

    if matrix.reply_to_msg_id:

        await matrix.get_reply_message()

    response = await bot.inline_query(TG_BOT, "اوامر الالعاب(?: |$)(.*)")

    await response[0].click(matrix.chat_id)

    await matrix.delete()

if Config.TG_BOT_USERNAME is not None and tgbot is not None :

    @check_owner

    @tgbot.on(events.InlineQuery)

    async def inlinematrix(matrix):

        builder = matrix.builder

        result = None

        query = matrix.text

        await bot.get_me()

        if query.startswith("اوامر الصيغ(?: |$)(.*)") and matrix.query.user_id == bot.uid:

            buttons = [[Button.inline("اوامر الصيغ", data="ordsag1"),]]

            result = builder.article(title="matrix", text=help2, buttons=buttons, link_preview=False)

            await matrix.answer([result] if result else None)

@matrix.on(admin_cmd(pattern="م21(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, " ⦗   بصمات تحشيش 1  ⦘  :\n\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص1)   ⦙   ابو  عباس  لو  تاكل  خره\n(.ص2)   ⦙   استمر  نحن  معك\n(.ص3)   ⦙   افحط  بوجه\n(.ص4)   ⦙   اكعد  لا  اسطرك  سطره  العباس\n(.ص5)   ⦙   اللهم  لا  شماته\n(.ص6)   ⦙   امرع  دينه\n(.ص7)   ⦙   امشي  بربوك\n(.ص8)   ⦙   انت  اسكت  انت  اسكت\n(.ص9)   ⦙   انت  سايق  زربه\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص10)   ⦙   اوني  تشان\n(.ص11)   ⦙   برافو  عليك  استادي \n(.ص12)   ⦙   بلوك  محترم\n(.ص13)   ⦙   بووم  في  منتصف  الجبهة \n(.ص14)   ⦙   بيتش \n(.ص15)   ⦙   تخوني  ؟\n(.ص16)   ⦙   تره  متكدرلي\n(.ص17)   ⦙   تعبان  اوي\n(.ص18)   ⦙   تكذب\n(.ص19)   ⦙   حسبي  الله\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص20)   ⦙   حشاش \n(.ص21)   ⦙   حقير  \n(.ص22)   ⦙   خاص  \n(.ص23)   ⦙   خاله  ما  تنامون  \n(.ص24)   ⦙   خرب  شرفي  اذا  ابقى  بالعراق \n(.ص25)   ⦙   دكات  الوكت  الاغبر  \n(.ص26)   ⦙   ررردح  \n(.ص27)   ⦙   سلامن  عليكم  \n(.ص28)   ⦙   بوم منتصف جبهه   \n(.ص29)   ⦙   شكد  شفت  ناس  مدودة\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰")

@matrix.on(admin_cmd(pattern="م22(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, " ⦗   بصمات تحشيش 2  ⦘  :\n\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص30)   ⦙  شلون  ، \n(.ص31)   ⦙  صح  لنوم  \n(.ص32)   ⦙  صمت  \n(.ص33)   ⦙  ضحكة  مصطفى  الحجي  \n(.ص34)   ⦙  طماطه  \n(.ص35)   ⦙  طيح  الله  حضك  \n(.ص36)   ⦙  فاك  يوو  \n(.ص37)   ⦙  اني فرحان وعمامي فرحانين\n(.ص38)   ⦙  لا  تضل  تضرط  \n(.ص39)   ⦙  لا  تقتل  المتعه  يا  مسلم  \n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص40)   ⦙  لا  مستحيل  \n(.ص41)   ⦙  لا  والله  شو  عصبي  \n(.ص42)   ⦙  لش  \n(.ص43)   ⦙  لك  اني  شعليه  \n(.ص44)   ⦙  ما  اشرب  \n(.ص45)   ⦙  مع  الاسف  \n(.ص46)   ⦙  مقتدى  \n(.ص47)   ⦙  من  رخصتكم  \n(.ص48)   ⦙  منو  انت  \n(.ص49)   ⦙  منورني  \n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص50)  ⦙  نتلاكه  بالدور  الثاني \n(.ص51)  ⦙  نستودعكم  الله  \n(.ص52)  ⦙  ها  شنهي  \n(.ص53)  ⦙  ههاي  الافكار  حطها ب\n(.ص54)  ⦙  ليش شنو سببها ليش\n(.ص55)  ⦙  يموتون  جهالي\n(.ص56)  ⦙  اريد انام\n(.ص57)  ⦙  افتحك فتح\n(.ص58)  ⦙  اكل خره لدوخني\n(.ص59)  ⦙  السيد شنهو السيد\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص60)  ⦙  زيج2\n(.ص61)  ⦙  زيج لهارون\n(.ص62)  ⦙  زيج الناصرية\n(.ص63)  ⦙  راقبو اطفالكم\n(.ص64)  ⦙  راح اموتن\n(.ص65)  ⦙  ذس اس مضرطة\n(.ص66)  ⦙  دروح سرسح منا\n(.ص67)  ⦙  خويه ما دكوم بيه\n(.ص68)  ⦙  خلصت تمسلت ديلة كافي انجب\n(.ص69)  ⦙  بعدك تخاف\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰")

@matrix.on(admin_cmd(pattern="م23(?: |$)(.*)"))    

async def matrixteam(event):

    await edit_or_reply(event, " ⦗   بصمات تحشيش 3  ⦘  :\n\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص72)  ⦙  انعل ابوكم لابو اليلعب وياكم طوبة\n(.ص73)  ⦙  انت شدخلك\n(.ص74)  ⦙  انا ماشي بطلع\n(.ص75)  ⦙  امداك وامده الخلفتك\n(.ص76)  ⦙  امبيههههه\n(.ص77)  ⦙  هدي بيبي\n(.ص78)  ⦙  هاه صدك تحجي\n(.ص79)  ⦙  مو كتلك رجعني\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص80)  ⦙  مامرجية منك هاية\n(.ص81)  ⦙  ليش هيجي\n(.ص82)  ⦙  كـــافـي\n(.ص85)  ⦙  شجلبت\n(.ص86)  ⦙  شبيك وجه الدبس\n(.ص87)  ⦙  سييييي\n(.ص88)  ⦙  زيجج1\n(.ص89)  ⦙  يموتون جهالي\n                                                       ⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n(.ص90)  ⦙  ياخي اسكت اسكت\n(.ص91)  ⦙  وينهم\n(.ص92)  ⦙  هيلو سامر وحود\n(.ص93)  ⦙  هو\n(.ص94)  ⦙  ههاي الافكار حطها\n⊱━━━━━━━━━━⊰᥀⊱━━━━━━━━━━⊰\n")

@bot.on(admin_cmd(outgoing=True, pattern="اوامر الصيغ(?: |$)(.*)"))

async def repomatrix(matrix):

    if matrix.fwd_from:

        return

    TG_BOT = Config.TG_BOT_USERNAME

    if matrix.reply_to_msg_id:

        await matrix.get_reply_message()

    response = await bot.inline_query(TG_BOT, "اوامر الصيغ(?: |$)(.*)")

    await response[0].click(matrix.chat_id)

    await matrix.delete()

    

ahmed = [    "100% تحبك وتخاف عليك",    "100% يحبج ويخاف عليج",    "91% جـزء من گـلبه ",    "81% تموت عليك ههاي ",    "81% يموت عليج ههذا ",    "هاه اخي ؟  🏳‍🌈",    "40% واحد حيوان ومصلحه عوفه ",    "50% شوف شعندك وياه ",    "30% خاين نصحيا عوفيه ميفيدج ",    "25% مصادق غيرج ويكلج احبج",    "25% واحد كلب ابن كلب عوفه",    "0% يكهرك ",    "0% تكرهك ",    "@matrix",]

arb = [    "100%",    "99%",    "98%",    "97%",    "96%",    "95%",    "90%",    "89%",    "88%",    "87%",    "86%",    "85%",    "80%",    "79%",    "78%",    "77%",    "76%",    "75%",    "70%",    "69%",    "68%",    "67%",    "66%",    "65%",    "60%",   "59%",    "58%",    "57%",    "56%",    "55%",    "50%",    "48%",    "47%",    "46%",    "45%",    "40%",    "39%",    "38%",    "37%",    "36%",    "35%",    "30%",    "29%",    "28%",    "27%",    "25%",    "20%",    "19%",    "18%",    "17%",    "16%",    "15%",    "10%",    "9%",    "8%",    "7%",    "6%",    "5%",    "4%",    "3%",    "2%",    "1%",    "0%",    "@matrix",]

@matrix.on(admin_cmd(pattern="غبي(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 1

    animation_ttl = range(14)

    event = await edit_or_reply(event, "**ارمي عقلك في سلة المهملات**")

    animation_chars = [

        "**- عقلك** ➡️ 🧠\n\n🧠         <(^_^ <)🗑",

        "**- عقلك** ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",

        "**- عقلك** ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",

        "**- عقلك** ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",

        "**- عقلك** ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",

        "**- عقلك** ➡️ 🧠\n\n🧠<(^_^ <)         🗑",

        "**- عقلك** ➡️ 🧠\n\n(> ^_^)>🧠         🗑",

        "**- عقلك** ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",

        "**- عقلك** ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",

        "**- عقلك** ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",

        "**- عقلك** ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",

        "**- عقلك** ➡️ 🧠\n\n          (> ^_^)>🧠🗑",

        "**- عقلك** ➡️ 🧠\n\n           (> ^_^)>🗑",

        "**- عقلك** ➡️ 🧠\n\n           <(^_^ <)🗑",    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 14])

Citation_morning = [

    "أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ اللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ.",

    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ هُوَ ٱللَّهُ أَحَدٌ، ٱللَّهُ ٱلصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ. ",

    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ.",

    "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ.",

    "أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُ بِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر.",

    "اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ، خَلَقْتَنـي وَأَنا عَبْـدُك، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت، أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ.",

    "رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً. ",

    "اللّهُـمَّ إِنِّـي أَصْبَـحْتُ أُشْـهِدُك، وَأُشْـهِدُ حَمَلَـةَ عَـرْشِـك، وَمَلَائِكَتَكَ، وَجَمـيعَ خَلْـقِك، أَنَّـكَ أَنْـتَ اللهُ لا إلهَ إلاّ أَنْـتَ وَحْـدَكَ لا شَريكَ لَـك، وَأَنَّ ُ مُحَمّـداً عَبْـدُكَ وَرَسـولُـك.",

    "اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر.",

    "حَسْبِـيَ اللّهُ لا إلهَ إلاّ هُوَ عَلَـيهِ تَوَكَّـلتُ وَهُوَ رَبُّ العَرْشِ العَظـيم.",

    "من قالها كفاه الله ما أهمه من أمر الدنيا والأخرة.",

    "بِسـمِ اللهِ الذي لا يَضُـرُّ مَعَ اسمِـهِ شَيءٌ في الأرْضِ وَلا في السّمـاءِ وَهـوَ السّمـيعُ العَلـيم.",

    "اللّهُـمَّ بِكَ أَصْـبَحْنا وَبِكَ أَمْسَـينا، وَبِكَ نَحْـيا وَبِكَ نَمُـوتُ وَإِلَـيْكَ النُّـشُور.",

    "أَصْبَـحْـنا عَلَى فِطْرَةِ الإسْلاَمِ، وَعَلَى كَلِمَةِ الإِخْلاَصِ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ، وَعَلَى مِلَّةِ أَبِينَا إبْرَاهِيمَ حَنِيفاً مُسْلِماً وَمَا كَانَ مِنَ المُشْرِكِينَ.",

    "سُبْحـانَ اللهِ وَبِحَمْـدِهِ عَدَدَ خَلْـقِه، وَرِضـا نَفْسِـه، وَزِنَـةَ عَـرْشِـه، وَمِـدادَ كَلِمـاتِـه.",

    "اللّهُـمَّ إِنّـي أَعـوذُ بِكَ مِنَ الْكُـفر، وَالفَـقْر، وَأَعـوذُ بِكَ مِنْ عَذابِ القَـبْر، لا إلهَ إلاّ أَنْـتَ.",

    "اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في الدُّنْـيا وَالآخِـرَة، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ العَـفْوَ وَالعـافِـيةَ في ديني وَدُنْـيايَ وَأهْـلي وَمالـي، اللّهُـمَّ اسْتُـرْ عـوْراتي وَآمِـنْ رَوْعاتي، اللّهُـمَّ احْفَظْـني مِن بَـينِ يَدَيَّ وَمِن خَلْفـي وَعَن يَمـيني وَعَن شِمـالي، وَمِن فَوْقـي، وَأَعـوذُ بِعَظَمَـتِكَ أَن أُغْـتالَ مِن تَحْتـي.",

    "يَا حَيُّ يَا قيُّومُ بِرَحْمَتِكَ أسْتَغِيثُ أصْلِحْ لِي شَأنِي كُلَّهُ وَلاَ تَكِلْنِي إلَى نَفْسِي طَـرْفَةَ عَيْنٍ.",

    "أَصْبَـحْـنا وَأَصْبَـحْ المُـلكُ للهِ رَبِّ العـالَمـين، اللّهُـمَّ إِنِّـي أسْـأَلُـكَ خَـيْرَ هـذا الـيَوْم ، فَـتْحَهُ، وَنَصْـرَهُ، وَنـورَهُ وَبَـرَكَتَـهُ، وَهُـداهُ، وَأَعـوذُ بِـكَ مِـنْ شَـرِّ ما فـيهِ وَشَـرِّ ما بَعْـدَه.",

    "اللّهُـمَّ عالِـمَ الغَـيْبِ وَالشّـهادَةِ فاطِـرَ السّماواتِ وَالأرْضِ رَبَّ كـلِّ شَـيءٍ وَمَليـكَه، أَشْهَـدُ أَنْ لا إِلـهَ إِلاّ أَنْت، أَعـوذُ بِكَ مِن شَـرِّ نَفْسـي وَمِن شَـرِّ الشَّيْـطانِ وَشِرْكِهِ، وَأَنْ أَقْتَـرِفَ عَلـى نَفْسـي سوءاً أَوْ أَجُـرَّهُ إِلـى مُسْـلِم.",

    "أَعـوذُ بِكَلِمـاتِ اللّهِ التّـامّـاتِ مِنْ شَـرِّ ما خَلَـق.",

    "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ على سيدنا مُحمَّد.",

    "اللَّهُمَّ إِنَّا نَعُوذُ بِكَ مِنْ أَنْ نُشْرِكَ بِكَ شَيْئًا نَعْلَمُهُ، وَنَسْتَغْفِرُكَ لِمَا لَا نَعْلَمُهُ.",

    "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ الْهَمِّ وَالْحَزَنِ، وَأَعُوذُ بِكَ مِنْ الْعَجْزِ وَالْكَسَلِ، وَأَعُوذُ بِكَ مِنْ الْجُبْنِ وَالْبُخْلِ، وَأَعُوذُ بِكَ مِنْ غَلَبَةِ الدَّيْنِ، وَقَهْرِ الرِّجَالِ.",

    "أسْتَغْفِرُ اللهَ العَظِيمَ الَّذِي لاَ إلَهَ إلاَّ هُوَ، الحَيُّ القَيُّومُ، وَأتُوبُ إلَيهِ.",

    "يَا رَبِّ، لَكَ الْحَمْدُ كَمَا يَنْبَغِي لِجَلَالِ وَجْهِكَ، وَلِعَظِيمِ سُلْطَانِكَ.",

    "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا، وَرِزْقًا طَيِّبًا، وَعَمَلًا مُتَقَبَّلًا.",

    "اللَّهُمَّ أَنْتَ رَبِّي لا إِلَهَ إِلا أَنْتَ، عَلَيْكَ تَوَكَّلْتُ ، وَأَنْتَ رَبُّ الْعَرْشِ الْعَظِيمِ، مَا شَاءَ اللَّهُ كَانَ، وَمَا لَمْ يَشَأْ لَمْ يَكُنْ، وَلا حَوْلَ وَلا قُوَّةَ إِلا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ، أَعْلَمُ أَنَّ اللَّهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ، وَأَنَّ اللَّهَ قَدْ أَحَاطَ بِكُلِّ شَيْءٍ عِلْمًا، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ شَرِّ كُلِّ دَابَّةٍ أَنْتَ آخِذٌ بِنَاصِيَتِهَا ، إِنَّ رَبِّي عَلَى صِرَاطٍ مُسْتَقِيمٍ.",

    "لَا إلَه إلّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءِ قَدِيرِ.",

    "كانت له عدل عشر رقاب، وكتبت له مئة حسنة، ومحيت عنه مئة سيئة، وكانت له حرزا من الشيطان.",

    "سُبْحـانَ اللهِ وَبِحَمْـدِهِ.",

    "حُطَّتْ خَطَايَاهُ وَإِنْ كَانَتْ مِثْلَ زَبَدِ الْبَحْرِ، لَمْ يَأْتِ أَحَدٌ يَوْمَ الْقِيَامَةِ بِأَفْضَلَ مِمَّا جَاءَ بِهِ إِلَّا أَحَدٌ قَالَ مِثْلَ مَا قَالَ أَوْ زَادَ عَلَيْهِ.",

    "أسْتَغْفِرُ اللهَ وَأتُوبُ إلَيْهِ.",

    "لا إلَهَ إلَّا اللَّهُ، وحْدَهُ لا شَرِيكَ له، له المُلْكُ وله الحَمْدُ، وهو علَى كُلِّ شيءٍ قَدِيرٌ.",

    "كانَتْ له عَدْلَ عَشْرِ رِقابٍ، وكُتِبَتْ له مِئَةُ حَسَنَةٍ، ومُحِيَتْ عنْه مِئَةُ سَيِّئَةٍ، وكانَتْ له حِرْزًا مِنَ الشَّيْطانِ يَومَهُ ذلكَ حتَّى يُمْسِيَ، ولَمْ يَأْتِ أحَدٌ بأَفْضَلَ ممَّا جاءَ به، إلَّا أحَدٌ عَمِلَ أكْثَرَ مِن ذلكَ.",



]

shar = [  "اغمس كعك بل جاي وشرب جكاير مصاريني تخربطة بل صار كالت شصاير ؟ 💔","كمت افز نص الليل صارتلي سوله بس موالك اشتاك تحصرني بوله 😂","حبك يبعد الروح غير كياني اشرب عرگ بچفاك حسبالي راني 👽","اشرب جبس بلماي حسبالي صرصور كلما اريد اكل يعفطلي عصفور 🤧","يكلك الوقت كالسيف ان لم تكن ذئبا طلع البدر علينا والرياح بما تشتهي السفن 🗿","قهـر حـبك حچـيته بـمجلـس الـنواب حتـه الكـاظـمي خـابـرني يبچـي 😭💔","تدري شوكت انساك يل كلشي وكلاشي من تسمع الصحراء طبكوهه كاشي","علي دنياي دارت كسختها و مو كسها عجبني كسختها وحرت مابين كسها وكسختها وأنة الكسوس حسرة علية 💔","تمطر عدس وهدوم وترعد بجايم الدنيا هيج تصير من انت نايم 🗿💔","صافن ؏ درس واذكر ايامي وياك كومني المدرس كتله هاحبي 😭","خــلــص درب الــمــحــنــه ونـاس نـاجـت نـاس 🙂💔","طاهر الموسوي. ايكول لكيت الدنيه سوك حضوض وانه اصويحبي معزل 🙂💔","اسرح بالغنم حتة اكدر انساك اباوع ع الطلي واذكر عيونك 💔💔","مليت الجلق والجلق ملاني ..اسمر ياحلو ماتلعب بخصياني","اليطلعونه أبحبل .. اايوكع ابير بس اليوكع بحبك الله ميطلعه😭😭😭😭","بيه حسره بكد ذاك سوه بيض وطماطه وطلع ماعدهم خبز 💔","صافن وفكر بيك ولابس مناظر … والدنيا من فرگاك مطرت قنادر 💔","دخلت البيت لادكة ولا حس رفعت زرورة لمدلل ولا حس ركعتة ثنين والثالث ولاحس يكلي مادخل شنهي القضية 😂😂","امشي بطريك الشوك ودنيا ضلمة طلعلي خمس جلاب لحكيني يمة","يكول تبجي و تصب دموع صدكني العيون السبب مو فركاك طب بيها صابون 😩😂","كيمر عسل لتصبلي ماريد الريوك خلي نطبك الشفتين ونتريك حلوك","زفوهه تاليي اليل واسمع بجيهه حط بالكلب سجين من حطه بيهه","دورلي فيتر زين من روحي مليت لا بدي لا رنكات بس شاصي ضليت","يكول .....اكل جبس بل ماي حسبالي صرصور كلما اريد انساك يعفطلي عصفور 💔🗿🐦"," البشر مثل الإنسان من يتوفه هم يموت ؟ "," صار كلبي بغيابك اصفر الون وكلساعه الشماته تصيح تكسي "," شنو فراكك فسو شو يخنك الروح 💔💔😔 "," #قـال لهـا لا تـبالي فبالت 😔"," لاتصفن لدنيات لاتصفن تدوخ صارو صدر ديوان الجانو فروخ"," طبع الوكت دوار لازم يمـر بيـك شمـا تضحك انت اليوم بـاجـر يبجيـك"," ع الخدين راح نخلي طسات لن دمعي بغيابك يمشي 200"," بنص بحر غطيت والحوت اجاني لتكلي سهله تهون مو يونس اني 💔💔"," اذا جان الفرح مخصوص للحلوين اكولن امري لـ الله واشتري خلطة"," وجهي بغيابك اصفر لون بلشارع فتت صاحولي تكسي"," كالو الصبر للفرج مفتاح طلع لوتي الفرج سوه 💔"," كاعد ع الرصيف انتظرك سنين شالوني بشفل كالو تجاوز 💔💔"," بيدك تسد الباب ۅ بيدك تفتحة وبيدك تفتح الباب وبيدك تسدة"," ما فادت جگارة بيوم فرگاك جبت واير لحيم وگمت ادخن"," صـرت بـاد بـغـيابـك ارڪب اسـڪيت"," اخذت لفه بغيابك تعرف منين من واحد يبيع مشكل هموم"," گـعدت من الطبل حسبالي رمضان طلع شامت يدگ ويگلي باعك 💔"," يكفي حبيب الروح يكفي بواري اسست نص بغداد مي ومجاري 💔"," اباوع للشمس ما شوفها شلون؟ اثاري الدنيه مغرب واني ما ادري😔💔"," كلبي بغيابك بايسكل صار كلساع الشماته تريد فره"," من كثر مامشتاك ورايدلي جيه وكفت الإسعاف حسبالي كيه"," ربع حبك تكلي يعادل الكون طلع ربعك مشكك حتى مايمشي"," يكول وانا اجروحي بتـيـتـه والـدمـع زيـت أذا أبـچـي علـيـك يطـيـح فـنگـر.!💔"," ربع حبك تكلي يعادل الكون طلع ربعك مشكك حتى مايمشي 💔"," مو شرط التحبة بالعين ينشاف مرات التحبة بعيونك تشوفة 😔"," تدري شوكت انساك واليل انامة من اشوف العصفور لابس بجامة","حسبالك وراثه عيوني جوزيات؟ فص العين زنجر من غبت عني 💔😍"," اثول حبيب الروح اثول مطفي لاكاني عين بعين باس البصفي 😘💔💔"," فيتر صرت ياناس والعيشه كشره وين الي يضب الروح بسبانه عشره😂😂❤️"," مثل راتب تقاعد صاير وياي كل شهرين اشوفك مره وحده💔🗿"," صافن وافكر بيك حسبالي يمي صحت بأسمك حيل كفختني امي 😻💔🌹"," كبل عطرك جنت اشمه وي الهدوم الله وياك امي اشترت غساله"," اخيط بالجرح والوكت يفتح بي ادري شلون اخلي لجروحي سحابة؟","صافن وافكر بيك وعن بالي متروح امشي ونطحت الباب حسبالي مفتوح 👀 🤦🏻‍♀️","يقول :بنيت بفرگتك بيت أحزان... اشو اجتي الشماته وياي عماله","صافن وافڪر بيك ياحلو العيون بالمرڪة اخبط چاي عبالي معجون🌚💕","من البجي عليك صار عدي هالات يسألوني و اكلهم اسهر اهواي😂","مثل السمج بالماي لابس جواريب ليش أنتَه هيچ وياي مألك علاقه 🤦🏻‍♀️💔","عفت العشك يفلان ما اريد اواعد ماريد احب اردود طالع تقاعد","كلي بيا ضلع بسمارك الجاي حتى اكتب عليه محجوز للغالي","اخبط بالشمس والساعه ثنتين من كد الحراره الكرك غنه","الدهر لو وازاك إزرع طماطة وازرع بصفها خيار واشبع زلاطة","شميت ريحت طبخ كلت العشه دليميه اثاري حبيبي ينتظر بالجزره الوسطية","اجت فكره بدماغي وكلت راح انساك صعد كلبي ادماني وتفل ع الفكره","انا مبلل هجر بس زحمه اصيح ااشاه🙂🌞💔","اجت فكره بدماغي وكلت راح انساك صعد كلبي ادماني وتفل ع الفكره","يكول صرت خلفه بغيابك والبخ جروح بس جرحك جبير يحتاج خباطه 👍","واكف ع السطح ابجي من الهموم طاح البيت كله من الرطوبه 💔💔","عله الباكيت كتبو احذر التدخين وعله فراكك ابد ماحذروني","صفنت بغيابك صفنت افراق بالحلم كأن مسجون ويصحولي افراج 😅","كلبي من الفرح يشعلك شموع وطفه عنه المولد صار ضلم","غيابك مثل الحمزه من مات ماضل واهس بفلم الرساله 💔💔🗿","صجمني الفرح رايد علاقه وياي مايدري الحزن خاطبني من صغري💔","خــلــص درب الــمــحــنــه ونـاس نـاجـت نـاس 🗿💔","طلع كمل براسي من ضيم فركك ويسألوني واكلهم هذا سمسم..🗿💔","تره الفاكد ربع ياكل جبس بالديــــن 💔","صافن و افكر بيك و ابريجي بيدي و احلى دبل رماش لعيون عضيدي 😍💔.","بغيابك قررت ابنيلي بيت احزان اجت كل الشماتة وياي عمالة","من كثر ما مشتاك صرت اني مخبول اتفرج اخبار حسبالي غامبول","هلكد ما بچيت بيوم فرگاك گعدوني الصبح حسبالهم بايل🥺","صافن وفكر بيك وبريجي بيدي دطلعي عاد مو شكيتي طيري تحياتي ابو سيوف😂💞","صار الهوا بفلوس لو انت موجود اشرب نفض بل كاس عبالي فمتو","اسرح بالغنم حتى أكدر انساك اباوع ع طلي واتذكر عيونك ..","بغيابك كلشي خرط حتة الحزام ترضاها الشمانة اشوف بلبولي 😂","وين البخت يفلان وتكلي مبخوت صرت اشتغل دفان محد رضه يموت. 😔","كاعد اتانيك وعلبيتونة افكر بيك ومدري انام مدري احاجيك 🕊❤","صرت سوده بغيابك عبالهم جيس ودوني للحاويه وذبوني بيك 💔.","حبك حبيب الروح سوالي ورطه كلما أفكر بيك انحصر ظرطه💔","انا بغيابك مثل ليمون كل ماتذكرتك تنعصر بطني","عزه فراكك كمت اطبخ جروح خرب عرض الشماته شكثر جابو جدوره 😂","على الحايط كتبنه باجر نعود…اجانه الزيج من بين الطوابيگ 🗿💔","حمد من گد المتاعب خلص كل حيله حمد باع القطار واشتره تريله...💔","لو ادري الدمع ينباع چا هسة بغيابك عندي جكسارة","عله الباكيت كتبو احذر التدخين وعله فراكك ابد ماحذروني",]

@matrix.on(admin_cmd(pattern="تفجير(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "جاري تفجير")

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")

    await asyncio.sleep(0.5)

    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")

    await asyncio.sleep(1)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")

    await asyncio.sleep(0.5)

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")

    await asyncio.sleep(0.5)

    await event.edit("**بوووووم تم تفجير الضحيه**")

    await asyncio.sleep(2)



@matrix.on(admin_cmd(pattern="قتل(?: |$)(.*)"))

async def _(event):

    animation_interval = 0.7

    animation_ttl = range(12)

    event = await edit_or_reply(event, "**جاري قتل الضحيه**")

    animation_chars = [

        "اططططلاق",

        "(　･ิω･ิ)︻デ═一-->",

        "---->____________⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠",

        "------>__________⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠",

        "-------->⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_________",

        "---------->⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_______",

        "------------>⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_____",

        "-------------->⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠____",

        "------------------>",

        "------>;(^。^)ノ",

        "(￣ー￣) مـات",

        "** تم قتل الضحيه بواسطه طلقه رأس 😈.😈...`\n '#هيد شوتت 😹**\n",    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])



game_code = ["تيك توك اثنان", "تيك توك اربعه", "ربط أربعة", "حجر-ورقة-مقص", "قرعة", "روليت", "داما", "داما تجمع"]



@matrix.ma_cmd(pattern="رابط الحذف")

async def _(ahmed):

    await edit_or_reply (ahmed, "**رابـط الحـذف ↬** https://telegram.org/deactivate")



@matrix.on(admin_cmd(pattern="طوبه(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.3

    animation_ttl = range(30)

    animation_chars = [

        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",

        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",

        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",

        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",

        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",

        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",

        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",

        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",

        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",    ]

    event = await edit_or_reply(event, "طب..طب طب..طب طب طب..شمنتضر تباوع")

    await asyncio.sleep(4)

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])

@matrix.on(admin_cmd(pattern="مربعات(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.3

    animation_ttl = range(15)

    event = await edit_or_reply(event, "مربعات ....")

    animation_chars = [

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",

        

 

 "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",

        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",

        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",

        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",

        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",

        "[👉🔴👈])",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 15])





@matrix.on(admin_cmd(pattern="حلويات(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "حلويات")

    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))

    for _ in range(100):

        await asyncio.sleep(0.4)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="نار(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "جاري اشعال النار")

    await event.edit("تحضر")

    await asyncio.sleep(0.3)

    await event.edit("استعد")

    await asyncio.sleep(0.2)

    await event.edit("ابدا")

    await asyncio.sleep(0.5)

    await event.edit("اخر مره ")

    await asyncio.sleep(0.2)

    await event.edit("اخر مره والله")

    await asyncio.sleep(0.3)

    await event.edit("وين البانزين")

    await asyncio.sleep(0.3)

    await event.edit("🔥🔥🔥")

    await asyncio.sleep(0.3)

    await event.edit("نار حته ابو حطب ممسويها هه 🔥🔥🔥") 

@matrix.on(admin_cmd(pattern="هلكوبتر(?: |$)(.*)"))

async def _(event):

    "جاري تشغيل الهلكوبتر"

    animation_interval = 1.0

    animation_ttl = range(60)

    animation_chars = [

        """".

    🔲 ▬▬▬.◙.▬▬▬ 🔳

            ═▂▄▄▓▄▄▂ 

           ◢◤    █▀▀████▄▄▄▄◢◤ 

           █▄ █ █▄ ███▀▀▀▀▀▀▀╬

           ◥█████◤ 

             ══╩══╩══ 

                      ╬═╬ 

                      ╬═╬     

                      ╬═╬ ☻/ 👞

                      ╬═╬/▌ 

                      ╬═╬/ \"""",

        """".

    🔳 ▬▬▬.◙.▬▬▬ 🔲

            ═▂▄▄▓▄▄▂ 

           ◢◤    █▀▀████▄▄▄▄◢◤ 

           █▄ █ █▄ ███▀▀▀▀▀▀▀╬

           ◥█████◤ 

             ══╩══╩══ 

                      ╬═╬ 

                      ╬═╬     

                      ╬═╬ ☻/ 

                      ╬═╬/▌ 👞

                      ╬═╬/ \"""",

        """".

    🔲 ▬▬▬.◙.▬▬▬ 🔳

            ═▂▄▄▓▄▄▂ 

           ◢◤    █▀▀████▄▄▄▄◢◤ 

           █▄ █ █▄ ███▀▀▀▀▀▀▀╬

           ◥█████◤ 

             ══╩══╩══ 

                      ╬═╬ 

                      ╬═╬     

                      ╬═╬ ☻/ 

                      ╬═╬/▌ 

                      ╬═╬/ \👞""""",

    ]

    event = await edit_or_reply(event, "جاري تشغيل الهلكوبتر")

    await asyncio.sleep(4)

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])    

game_name = [    "Tic-Tac-Toe",    "Tic-Tac-Four",    "Connect Four",    "Rock-Paper-Scissors",    "Rock-Paper-Scissors-Lizard-Spock",    "Russian Roulette",    "Checkers",    "Pool Checkers" ]

osfle = [  "〔 لا خلقۿ ولا اخلاق لحاله عايش ☹️. 〕","〔 سڪر محلي محطوط على ڪريما 🤤🍰. 〕","〔 ؏ـسل × ؏ـسل 🍯. 〕","〔 أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂. 〕","〔 ملڪ جمال ألعالم 🥺💘. 〕","〔 أنسان زباله ومكضيها نوم 🙂. 〕","〔 يعني بشرفك هوه هذا يستاهل اوصفه؟ 〕","〔 أنسان ڪيمر 😞💘. 〕","〔 جنۿ جڪليته يربيـﮧ 🍬. 〕","〔 شمأ اوصف بي قليل 🥵💞. 〕","〔 وجۿا جنة كاهي من ألصبحـﮧ ☹️♥️. 〕","〔 هذا واحد يهودي دير بالك منه 🙂💘. 〕","〔 هذا انسان يحب مقتدئ ابتعد عنه 😂💞. 〕","〔 بس تزحف ع الولد وهيه زرڪة 😂. 〕","〔 جنۿ مرڪة شجر شبيك يول 😂😔. 〕","〔 هذا حبيبي ، أحبة ڪولش 🙊💘 〕","〔 جمالهـﮧ خبلني 😞💞. 〕","〔 چنۿ ڪريمة ؏ـلى ڪيك 😞💘. 〕","〔 انسان مينطاق 🙂💔. 〕","〔 فد أنسان مرتب وريحتة تخبل 🥺💞 〕","〔 شڪد حلو هذا ومؤدب 😭💞💘💕. 〕","〔 وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞. 〕","〔 نتا مخلوق من ڪتله مال عارية 🙂😂. 〕","〔 لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺. 〕","〔 با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿. 〕","〔 شني عمي مو بشر ڪيك ورب 🥺💞. 〕","〔 عوفه ضلعي هذا انسان زباله 🙂😂. 〕","〔 انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️. 〕","〔 باع منو شون بشر هوه وجۿا يطرد النعمة 🙂. 〕","〔 عيع فد أنسان وصخ 😂♥️. 〕","〔 يول هذا طاڪك قطة احسلك 😂💞. 〕","〔 لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘. 〕","〔 هذا الله غاضب عليه 🌚💔. 〕","〔 شنو شنو ؟ تسرسح يله 😒💘. 〕","〔 وردة مال الله ، فدوا اروحله 🤤💞. 〕"," أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞. 〕","〔 انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞. 〕","〔 أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂. 〕","〔 الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞. 〕","〔 لكشنو من جمالل هذا يربييييي 😭💞. 〕","〔 يومة فديته جنه زربه 😭😂💞. 〕",]

shazla = [ "مهندس 😣💕.","عامل نظافه 😶.","عسكري 🤤.","دكتور 😞💞.","مختبري 💘.","هڪر 🌚.","قاضي 😂.","طيار ☹️.","معلم 🥺.","حلاق 😂😔. ","رائد فضاء 🐸😂. ","خباز 🥺💘. ","سايق مخده 😂. ","محاسب ☹️💘. ","ڪهربائي 🐸😂. ","فيتر 😂. ","رقاصه 🤤😂.","ويتر 🥲💞.","مضيف طائرات 😉😂.","سكرتير 😭💘.","اكل ونوم بس 🥲.","بيطري 🥲😂.","معاون طبيب 😭💞.","زبـال ♻️👽.","طـباخ 🧑‍🍳👩‍🍳.","فيتجـري 👨‍🦼.","نيـاج 🔞 .","منيـوج 🔞."," جـني 🧞‍♂️.","شـرطي 👮‍♂️👮‍♀️ ."," مقـاتل 🤺 ."," سـاحر 🧙‍♂️ ."," متـسلق 🧗‍♂️🧗‍♀️ ."," ريـاضي 🏃‍♂️🏃‍♀️ ."," مغنـي 🗣️ .","حـورية 🧜‍♂️🧜‍♀️ ."," زومـبي 🧟‍♂️🧟‍♀️ .","مبـرمج .",]

zogona2 = [ " زواجك مِـن بيرين سات 💘."," زواجك مِـن اسراء الأصيل 🥺💘."," زواجك مِـن رحمة رياض 🥺💘."," زواجك مِـن توبا بويوكوستن 🥺💘."," زواجك مِـن هازال كايا 🥺💘."," زواجك مِـن هندا ارتشيل 🥺💘."," زواجك مِـن ديميت اوزديمير 🥺💘."," زواجك مِـن اسراء شينغونالب 🥺💘."," زواجك مِـن اوزغو نامال 🥺💘."," زواجك مِـن عائشه شيدام 🥺💘."," زواجك مِـن انجلينا جولي 🥺💘."," زواجك مِـن كارينا كابور 🥺💘."," زواجج مِـن كاترينا 🥺💘."," زواجك مِـن لينا جونامي 🥺💘."," زواجك مِـن اسراء العبيدي 🥺💘."," زواجك مِـن سهير صلاح 🥺💘."," زواجك مِـن سولاف جليل 🥺💘."," زواجك مِـن رغد خاتون 🥺"," زواجك مِـن اساور عزت",]

zogona1 = [ " زواجج مِـن نور الزين 🥺💘."," زواجج مِـن باريش أردش 🥺💘."," زواجج مِـن محمد السالم 🥺💘."," زواجج مِـن بوراك دينيز 🥺💘."," زواجج مِـن تولغا ساريتاش 🥺💘."," زواجج مِـن كيفانش تاتليتوغ 🥺💘."," زواجج مِـن الب نفروز 🥺💘."," زواجج مِـن كولي 🥺💘."," زواجج مِـن ديراج دوبار 🥺💘."," زواجج مِـن زاك 🥺💘."," زواجج مِـن عبود 🥺💘."," زواجج مِـن محمد رمضان 🥺💘."," زواجج مِـن رامز 🥺💘."," زواجج مِـن محمد اياد 🥺💘."," زواجج مِـن محمود الغياث 🥺💘."," زواجج مِـن محمود التركي 🥺💘."," زواجج مِـن توم كروز 🥺💘. زواجج مِـن ريبر 🥺💘."," زواجج مِـن تيمور 🥺💘."," زواجج مِـن احمد البياتي 🥺💘."," زواجج مِـن كاضم الساهر 🥺💘."," زواجج مِـن مارتن 🥺💘."," زواجج مِـن احمد نسيم 🥺💘."," زواجج مِـن علي الخالدي 🥺💘."," زواجج مِـن احمد البشير 🥺💘."," زواجج مِـن علي عذاب 🥺💘."," زواجج مِـن مرتضى اركان 🥺💘."," زواجج مِـن نور مار 🥺💘."," زواجج مِـن اترو 🥺💘.",]

rksla = [ "اشغلڪ ساجدۿ عبيد ؟ 😹💕","احنه بيا حال وانته تريد تركص 😒.","شحجي وياك؟","خاله يم علي ، يم علي خاله 💃😹.","صمونن عشرهه بلف ، علي الله احترڪنة 😹.","الله الله الله وياك ، روح روح شعر شعر 😹💕.","وحبوبه شهرتينه دلبسي لـ 😹😹☹️.","على الون روحي متعلمه 🤦‍♀️💕.","العب دءلعب العب العب العب 💃💃💕","شنتنتوري 😂😂","راح اسجل روحي بأسمك 🥺","شرب شرب شرب 😎😹.","شكلولك مفتح ملهى 😒","مبينه ركاصه 😒💓.","اي شعليه متركصين 😹.","روحي صلي بدال متركصين 🤦‍♀️☹️.","توڪع ، هوه انته توڪع جرح 🥺🌈.","ربي رزقني بفد عشڪ 💕.","راح اسجل روحي بأسمك 🥺.","لسوي لمحد مسوي وادك لصبح جوبيه 💃😹😹.","اضحك عفتني بضيم اه يالعفتني ","يااول عشك وحب من صدك يجيري ويه احساسي 🤤💞.","عشڪ موت ، اموتن بيك يالغالي 🥺💓.","قافل على حبك صدك قافل ، اعشكنك عشگ جاهل 💌💗.","دايخ بيك ، احبڪ ياوجع راسي ☹️🖤.","دكافي يمعود وينك وين الركص 😒","واريد اشرد بيڪ ، يماا 😹😹",]

tbshal = [ "شوكلك هوه انته هم حاسب نفسك انسان 🙂💕","شتريد اوكلك يعمريي 🥺💞","شسويلك يعني؟ 😒","هاك بيتزا و ولي 🍕","يطبك مرض 🙂","اروحح فدوا للجوعان اني 🥺❤️","شكلولك عليه مفتح مطعم؟ ","جيب فلوس 🌚","روحي سوي اندومي 🍜💛","هاج فستق 🥜","اصلا حرام بيك الاكل انته 😒","مفتح مطعم ابوك ؟","جوع البلوع 😂😞","تريد سم؟","زربه عليك 🌚😹","خلسويلك لفه طماطه وخيار 🍅🥒","بشرفي تستاهل 🧄","هاج بركر 🍔","هاك صاج 🌯","خلسويلك بيض 🍳","مااكدر انطيج كيك لان ماكو كيك ياكل كيك 🥺💞","هاج موطه 🍦","خلسويلك دولمه 💕","خلسويلك قوزي ☹️❤️","تريد كباب 💞","راح اسويلك دجاج ع الفحم 😞😹","تريد سمج ؟","انته حليب متستاهل 😞","اسلكلك بيض؟","عدنه بس جاي 🙂","شلونك 😹","والله اني هم جوعان شتكول نروح للمطعم ع حسابك 😹😞","تريدين نمبر وان 🥺","تريدين تويكس ؟💕","تريدين جبس ♥️","عدنه تكه بايته تريدين؟ 🙂","عدنه بس باجه 🥺😹","تريد تمن احمر؟ 🤤💕","تريد تمن ومرك؟ 💕","خلسويلك طماطه حمس 🥺🙊","تريدين دليميه؟ ☹️🖤","هاج جكاره 🚬 شسوين بالاكل .","دولي 😒","وفف اسويلج مقلوبا 🙊🤤.","تريدين كبد 🤷🏻‍♀️👨‍🍳.","تريد طرشي 🌚😎","تريدين ليز ؟ 😉🧀.","تريدين تاجينا ؟","اكو مخلمه بس .","فنڪر تريدين 🥺","اسويلڪ بتيته وبيض 🤤💞.","ستسڪ لحم ، لو ستيڪ دجاج؟ 🌚.","عدنه بس برياني 🤤","تريدين حب .","اكو بس شامية ","اجيبلج فاصوليا وتمن😞💞","اسويلج كيمر وجاي؟",]

@matrix.on(admin_cmd(pattern="اشكال مربع(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 0.3

    animation_ttl = range(20)

    event = await edit_or_reply(event, "◨")

    animation_chars = ["◧", "◨", "◧", "◨", "‎"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])



@matrix.on(admin_cmd(pattern="دائره(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 0.3

    animation_ttl = range(20)

    event = await edit_or_reply(event, "دائره...")

    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])

@matrix.on(admin_cmd(pattern="قلب(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 0.5

    animation_ttl = range(20)

    event = await edit_or_reply(event, "❤️")

    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 4])

@matrix.on(admin_cmd(pattern="يوغا(?: |$)(.*)"))

async def mafiabot(mafiamemes):

    input_str = mafiamemes.pattern_match.group(1)

    input_str = deEmojify(input_str)

    if "-" in input_str:

        text1, text2 = input_str.split("-")

    else:

        await edit_or_reply(            mafiamemes,            "الرد على الصورة أو الملصق باستخدام `.يوغا (اسم الكارت)-(وصف الكارت)`",        )

        return

    replied = await mafiamemes.get_reply_message()

    if not os.path.isdir("./temp/"):

        os.makedirs("./temp/")

    if not replied:

        await edit_or_reply(            mafiamemes, "ملف الوسائط غير مدعوم. الرد على وسائل الإعلام المدعومة"        )

        return

    if replied.media:

        mafiamemmes = await edit_or_reply(mafiamemes, " ")

    else:

        await edit_or_reply(            mafiamemes, "ملف الوسائط غير مدعوم. الرد على وسائل الإعلام المدعومة"        )

        return

    try:

        mafia = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")

        mafia = Get(mafia)

        await mafiamemes.client(mafia)

    except BaseException:

        pass

    download_location = await mafiamemes.client.download_media(replied, "./temp/")

    if download_location.endswith((".webp")):

        download_location = convert_toimage(download_location)

    size = os.stat(download_location).st_size

    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):

        if size > 5242880:

            await mafiamemmes.edit(                "حجم الملف الذي تم الرد عليه غير مدعوم ، يجب أن يكون حجمه أقل من 5 ميغا بايت"            )

            os.remove(download_location)

            return

        await mafiamemmes.edit(" ")

    else:

        await mafiamemmes.edit("ملف الوسائط غير مدعوم. الرد على وسائل الإعلام المدعومة")

        os.remove(download_location)

        return

    try:

        response = upload_file(download_location)

        os.remove(download_location)

    except exceptions.TelegraphException as exc:

        await mafiamemmes.edit("ERROR: " + str(exc))

        os.remove(download_location)

        return

    mafia = f"https://telegra.ph{response[0]}"

    mafia = await trap(text1, text2, mafia)

    await mafiamemmes.delete()

    await mafiamemes.client.send_file(mafiamemes.chat_id, mafia, reply_to=replied)

@matrix.on(admin_cmd(pattern="مزاج(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 1

    animation_ttl = range(20)

    event = await edit_or_reply(event, "مزاج")

    animation_chars = [

        "😁",

        "😧",

        "😡",

        "😢",

        "😁",

        "😧",

        "😡",

        "😢",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])





@matrix.on(admin_cmd(pattern="قرد(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 2

    animation_ttl = range(12)

    event = await edit_or_reply(event, "قروده....")

    animation_chars = [

        "🐵",

        "🙉",

        "🙈",

        "🙊",

        "🐵",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 6])







@matrix.on(admin_cmd(pattern="ايد(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 1

    animation_ttl = range(13)

    event = await edit_or_reply(event, "🖐️")

    animation_chars = [

        "👈",

        "👉",

        "☝️",

        "👆",

        "🖕",

        "👇",

        "✌️",

        "🤞",

        "🖖",

        "🤘",

        "🤙",

        "🖐️",

        "👌",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 13])

game_list = " 1. - `.لعبه تيك توك اربعه`\n2. - `.لعبه تيك توك اثنان`\n3. - `.لعبه ربط أربعة`\n4. - `.لعبه قرعة`\n5. - `.لعبه حجر-ورقة-مقص`\n6. - `.لعبه روليت`\n7. - `.لعبه داما`\n8. - `.لعبه داما تجمع`\n"

@matrix.on(admin_cmd(pattern="العد التنازلي(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 1

    animation_ttl = range(12)

    event = await edit_or_reply(event, "العد التنازلي....")

    animation_chars = [

        "🔟",

        "9️⃣",

        "8️⃣",

        "7️⃣",

        "6️⃣",

        "5️⃣",

        "4️⃣",

        "3️⃣",

        "2️⃣",

        "1️⃣",

        "0️⃣",

        "🆘",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])

@matrix.on(admin_cmd(pattern="الوان قلوب(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 0.3

    animation_ttl = range(54)

    event = await edit_or_reply(event, "🖤")

    animation_chars = [

        "❤️",

        "🧡",

        "💛",

        "💚",

        "💙",

        "💜",

        "🖤",

        "💘",

        "💝",

        "❤️",

        "🧡",

        "💛",

        "💚",

        "💙",

        "💜",

        "🖤",

        "💘",

        "💝",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])



@matrix.on(admin_cmd(outgoing=True, pattern="قران$"))

async def mavois(vois):

  rl = random.randint(2,101)

  url = f"https://t.me/qreen1/{rl}"

  await vois.client.send_file(vois.chat_id,url,caption="᥀︙وأذكر ربك اذا نسيت",parse_mode="html")



@matrix.on(admin_cmd(outgoing=True, pattern="غنيلي$"))

async def matrixvois(vois):

  rl = random.randint(2,582)

  url = f"https://t.me/vvttvve/{rl}"

  await vois.client.send_file(vois.chat_id,url,caption="᥀︙تم اختيار هذا الفويز لك .",parse_mode="html")

  await vois.delete()



@matrix.on(admin_cmd(outgoing=True, pattern="شعر$"))

async def matrixvois(vois):

  rl = random.randint(2,622)

  url = f"https://t.me/L1BBBL/{rl}"

  await vois.client.send_file(vois.chat_id,url,caption="᥀︙تم اختيار هذا الفويز لك .",parse_mode="html")

  await vois.delete()

@matrix.on(admin_cmd(outgoing=True, pattern="راب$"))

async def matrixvois(vois):

  rl = random.randint(2,86)

  url = f"https://t.me/RapEthan/{rl}"

  await vois.client.send_file(vois.chat_id,url,caption="᥀︙تم اختيار هذا الفويز لك .",parse_mode="html")

  await vois.delete()

@matrix.on(admin_cmd(outgoing=True, pattern="ريمكس$"))

async def matrixvois(vois):

  rl = random.randint(2,279)

  url = f"https://t.me/remixsource/{rl}"

  await vois.client.send_file(vois.chat_id,url,caption="᥀︙تم اختيار هذا الفويز لك .",parse_mode="html")

  await vois.delete()

  

@matrix.on(admin_cmd(pattern="ثعبان(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.3

    animation_ttl = range(27)

    event = await edit_or_reply(event, "ثعبان ..")

    animation_chars = [

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",

        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 27])

@matrix.on(admin_cmd(pattern="شعر(?: |$)(.*)"))

async def permalink(mention):

    matr = random.choice(shar)

    await edit_or_reply(mention, f"** {matr} **")

@matrix.on(admin_cmd(pattern="رجل(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.5

    animation_ttl = range(16)

    event = await edit_or_reply(event, "رجل...")

    animation_chars = [

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",

        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 16])



@matrix.on(admin_cmd(pattern="رموز شيطانيه(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 1

    animation_ttl = range(30)

    event = await edit_or_reply(event, "رموز شيطانيه ....")

    animation_chars = [

        "🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "‎◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️◼️◼️\n🔴🔵??♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

        "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

        "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

        "◼️◼️\n◼️◼️",

        "◼️",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 30])





@matrix.on(admin_cmd(pattern="قطار(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.2

    animation_ttl = range(30)

    event = await edit_or_reply(event, "قطار")

    animation_chars = [

        "**ت**",

        "**تو**",

        "**توتت**",

        "**تووووت**",

        "**توووت**",

        "**تووووت**",

        "**توووووت**",

        "**توووووت**",

        "**توووووووووت**",

        "**توووووووووووت**",

        "**اجه القطار 🚅**",

        "**وخر عن طريق 🚅🚃🚃**",

        "**تووووت 🚅🚃🚃🚃**",

        "**جبنها وجت ويانه 🚅🚃🚃🚃🚃**",

        "**جبناها وجت ويانه 🚅🚃🚃🚃🚃🚃**",

        "**rain🚅🚃🚃🚃🚃🚃🚃**",

        "**بيباي 🚅🚃🚃🚃🚃🚃🚃🚃**",

        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",

        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",

        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃🚃",

        "🚃🚃🚃🚃",

        "🚃🚃🚃",

        "🚃🚃",

        "🚃",

        "**مو قطار ضيم**",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 30])



@matrix.on(admin_cmd(pattern="موسيقى(?: |$)(.*)"))

async def _(event):

    "animation command"

    animation_interval = 1.5

    animation_ttl = range(11)

    event = await edit_or_reply(event, "يتم بدأ  الموسيقى...")

    animation_chars = [

        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀ [مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])



@matrix.on(admin_cmd(pattern="رسم(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(

        event, "╔═══════════════════╗ \n  \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )

    await asyncio.sleep(1)

    await event.edit(

        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"

    )



@matrix.on(admin_cmd(pattern="فراشه(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "**فراشه..**")

    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))

    for _ in range(48):

        await asyncio.sleep(0.3)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.on(admin_cmd(pattern="مكعبات(?: |$)(.*)"))

async def _(event):

    event = await edit_or_reply(event, "**مكعبات...**")

    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))

    for _ in range(150):

        await asyncio.sleep(0.3)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="مربعاتي(?: |$)(.*)"))

async def _(event):

    event = await edit_or_reply(event, "**مربعاتي ...**")

    deq = deque(list("🟧🟧🟧🟧🟧🟦🟦🟦🟦🟦🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️"))

    for _ in range(150):

        await asyncio.sleep(0.3)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="مطر(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "`مطر.......`")

    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))

    for _ in range(48):

        await asyncio.sleep(0.3)

        await event.edit("".join(deq))

        deq.rotate(1)





@matrix.on(admin_cmd(pattern="تحركات(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 1

    animation_ttl = range(10)

    animation_chars = [

        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",

        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",

        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",

        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",

        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",

        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",

        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",

        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",

        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",

        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",

    ]

    event = await edit_or_reply(event, "تحركات ....")

    await asyncio.sleep(2)

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])

moment_worker = []

@matrix.on(admin_cmd(pattern="ايموجيات(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.5

    animation_ttl = range(70)

    event = await edit_or_reply(event, "ايموجيات")

    animation_chars = [

        "😀",

        "👩‍🎨",

        "😁",

        "😂",

        "🤣",

        "😃",

        "😄",

        "😅",

        "😊",

        "☺",

        "🙂",

        "🤔",

        "🤨",

        "😐",

        "😑",

        "😶",

        "😣",

        "😥",

        "😮",

        "🤐",

        "😯",

        "😴",

        "😔",

        "😕",

        "☹",

        "🙁",

        "😖",

        "😞",

        "😟",

        "😢",

        "😭",

        "🤯",

        "💔",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 35])

@matrix.on(admin_cmd(pattern="اسعاف(?: |$)(.*)"))

async def _(event):

    event = await edit_or_reply(event, "اسعاف ياالله حتركنه ...")

    await event.edit("_____🚑")

    await event.edit("____🚑_")

    await event.edit("____🚑_")

    await event.edit("___🚑__")

    await event.edit("__🚑___")

    await event.edit("__🚑___")

    await event.edit("🚑_____")

    await event.edit("________")

    await asyncio.sleep(3)



@matrix.on(admin_cmd(pattern="طائره(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "انتظر الطائره...")

    await event.edit("✈-------------")

    await event.edit("-✈------------")

    await event.edit("--✈-----------")

    await event.edit("---✈----------")

    await event.edit("----✈---------")

    await event.edit("-----✈--------")

    await event.edit("------✈-------")

    await event.edit("-------✈------")

    await event.edit("--------✈-----")

    await event.edit("---------✈----")

    await event.edit("----------✈---")

    await event.edit("-----------✈--")

    await event.edit("------------✈-")

    await event.edit("-------------✈")

    await asyncio.sleep(3)



@matrix.on(admin_cmd(pattern="(خط الغامق|خط غامق)"))

async def matrext(event):

    ismaboldma = gvarstatus("maboldma")

    if not ismaboldma:

        addgvar ("maboldma", "on")

        await edit_delete(event, "**تم تفعيل خط الغامق بنجاح ✅**")

        return



    if ismaboldma:

        delgvar("maboldma")

        await edit_delete(event, "**تم اطفاء خط الغامق بنجاح ✅ **")

        return

@matrix.on(admin_cmd(pattern="(اغلاق الخط الغامق|اغلاق خط غامق)"))

async def matrext(event):

    ismaboldma = gvarstatus("maboldma")

    if not ismaboldma:

        addgvar ("maboldma", "on")

        await edit_delete(event, "**تم تفعيل خط الغامق بنجاح ✅**")

        return



    if ismaboldma:

        delgvar("maboldma")

        await edit_delete(event, "**تم اطفاء خط الغامق بنجاح ✅ **")

        return        

@matrix.on(admin_cmd(pattern="شرطي(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.3

    animation_ttl = range(12)

    event = await edit_or_reply(event, "شرطه")

    animation_chars = [

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        "🔵??🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",

        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",

        f"{mention} **الشرطي هنا**",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])

        

@matrix.on(admin_cmd(pattern="خط مائل"))

async def matrext(event):

    ismaahmedma = gvarstatus("ismamailma")

    if not ismaahmedma:

        addgvar ("ismamailma", "on")

        await edit_delete(event, "**تم تفعيل خط الرمز بنجاح ✅**")

        return



    if ismaahmedma:

        delgvar("ismamailma")

        await edit_delete(event, "**تم اطفاء خط المائل بنجاح ✅ **")

        return        

        

@matrix.on(admin_cmd(pattern="اغلاق خط مائل"))

async def matrext(event):

    ismaahmedma = gvarstatus("ismamailma")

    if not ismaahmedma:

        addgvar ("ismamailma", "on")

        await edit_delete(event, "**تم تفعيل خط المائل بنجاح ✅**")

        return

    if ismaahmedma:

        delgvar("ismamailma")

        await edit_delete(event, "**تم اطفاء خط المائل بنجاح ✅ **")

        return        

                

@matrix.on(admin_cmd(pattern="(خط رمز|خط الرمز)"))

async def matrext(event):

    ismaahmedma = gvarstatus("maahmedma")

    if not ismaahmedma:

        addgvar ("maahmedma", "on")

        await edit_delete(event, "**تم تفعيل خط الرمز بنجاح ✅**")

        return



    if ismaahmedma:

        delgvar("maahmedma")

        await edit_delete(event, "**تم اطفاء خط الرمز بنجاح ✅ **")

        return

@matrix.on(admin_cmd(pattern= "اغلاق خط رمز"))

async def matrext(event):

    ismaahmedma = gvarstatus("maahmedma")

    if not ismaahmedma:

        addgvar ("maahmedma", "on")

        await edit_delete(event, "**تم تفعيل خط الرمز بنجاح ✅**")

        return



    if ismaahmedma:

        delgvar("maahmedma")

        await edit_delete(event, "**تم اطفاء خط الرمز بنجاح ✅ **")

        return    



@matrix.on(events.NewMessage(outgoing=True))

async def klanr(event):

    ismaboldma = gvarstatus("maboldma")

    if ismaboldma:

        try:

            await event.edit(f"**{event.message.message}**")

        except MessageIdInvalidError:

            pass

    ismaahmedma = gvarstatus("maahmedma")

    if ismaahmedma:

        try:

            await event.edit(f"`{event.message.message}`")

        except MessageIdInvalidError:

            pass

    ismamailma = gvarstatus("ismamailma")    

    if ismamailma:

        try:

            await event.edit(f"__{event.message.message}__")

        except MessageIdInvalidError:

            pass            

    

@matrix.on(admin_cmd(pattern="النضام الشمسي(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    animation_interval = 0.1

    animation_ttl = range(80)

    event = await edit_or_reply(event, "النضام الشمسي")

    animation_chars = [

        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",

        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",

        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",

        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",

        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",

        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])



@matrix.on(admin_cmd(pattern="افكر(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "افكر")

    deq = deque(list("🤔🧐🤔🧐🤔🧐"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.on(admin_cmd(pattern="ضحك(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "ضحك")

    deq = deque(list("😹🤣😂😹🤣😂"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.on(admin_cmd(pattern="ضايج(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "ضايج")

    deq = deque(list("😕😞🙁☹️😕😞🙁"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="اوصفلي(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(osfle)

    await edit_or_reply(mention, f"هذا  [{mat}](tg://user?id={user.id}) {matr} ")

@matrix.on(admin_cmd(pattern="مهنته(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(shazla)

    await edit_or_reply(mention, f"هذا  [{mat}](tg://user?id={user.id}) شغله {matr} ")

@matrix.on(admin_cmd(pattern="زوجه(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(zogona2)

    await edit_or_reply(mention, f"مبࢪوڪ [{mat}](tg://user?id={user.id}) {matr} ")

@matrix.on(admin_cmd(pattern="زوجها(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(zogona1)

    await edit_or_reply(mention, f"مبࢪوڪ [{mat}](tg://user?id={user.id}) {matr} ")

@matrix.on(admin_cmd(pattern="ركصله(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس     **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(rksla)

    await edit_or_reply(mention, f" [{mat}](tg://user?id={user.id}) {matr} ")

@matrix.on(admin_cmd(pattern="طبخله(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس     **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(tbshal)

    await edit_or_reply(mention, f" [{mat}](tg://user?id={user.id}) {matr} ")

@matrix.on(admin_cmd(pattern="ساعه متحركه(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "وقت")

    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.ma_cmd(pattern="لعبه(?:\s|$)([\s\S]*)",)

async def igame(event):

    reply_to_id = await reply_id(event)

    input_str = event.pattern_match.group(1)

    data = dict(zip(game_code, button))

    name = dict(zip(game_code, game_name))

    if not input_str:

        await edit_delete(event, f"**اهلا هناك 8 العاب قم بنسخ وارسال الأمر بأختيارك  :-**\n\n{game_list}", time=60)

        return

    if input_str not in game_code:

        catevent = await edit_or_reply(event, "أعطني اسم اللعبة الصحيح ...")

        await asyncio.sleep(1)

        await edit_delete(catevent, f"** اهلا هناك 8 العاب قم بنسخ وارسال الأمر بأختيارك :-**\n\n{game_list}", time=60)

    else:

        game = data[input_str]

        gname = name[input_str]

        await edit_or_reply(event, f"**اسم العبه : `{input_str}` تم اختياره للعبة :-** __{gname}__")

        await asyncio.sleep(1)

        bot = "@inlinegamesbot"

        results = await event.client.inline_query(bot, gname)

        await results[int(game)].click(event.chat_id, reply_to=reply_to_id)

        await event.delete()

@matrix.on(admin_cmd(pattern="قلوب(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "قلوب")

    deq = deque(list("❤️🧡💛💚💙💜🖤"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="رياضه(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "رياضه")

    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="فواكه(?: |$)(.*)"))

async def _(event):

    event = await edit_or_reply(event, "رياضه")

    deq = deque(list("🍉🍓🍇🍎🍍🍐🍌"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)

@matrix.on(admin_cmd(pattern="الارض(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "الارض")

    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.on(admin_cmd(pattern="قمر(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "قمر")

    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))

    for _ in range(20):

        await asyncio.sleep(0.2)

        await event.edit("".join(deq))

        deq.rotate(1)



@matrix.on(admin_cmd(pattern="اقمار(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "اقمار")

    animation_interval = 0.2

    animation_ttl = range(80)

    await event.edit("اقمار..")

    animation_chars = [

        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",

        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",

        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",

        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",

        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",

        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",

        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",

        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 8])



@matrix.on(admin_cmd(pattern="قمور(?: |$)(.*)"))

async def _(event):

    "أمر الرسوم المتحركة"

    event = await edit_or_reply(event, "قمور")

    animation_interval = 0.2

    animation_ttl = range(80)

    await event.edit("قمور..")

    animation_chars = [

        "🌗",

        "🌘",

        "🌑",

        "🌒",

        "🌓",

        "🌔",

        "🌕",

        "🌖",

        "🌗",

        "🌘",

        "🌑",

        "🌒",

        "🌓",

        "🌔",

        "🌕",

        "🌖",

        "🌗",

        "🌘",

        "🌑",

        "🌒",

        "🌓",

        "🌔",

        "🌕",

        "🌖",

        "🌗",

        "🌘",

        "🌑",

        "🌒",

        "🌓",

        "🌔",

        "🌕",

        "🌖",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 32])





ownerahmed_id = 6373798952

@matrix.on(events.NewMessage(outgoing=False, pattern='/matrix'))

async def OwnerStart(event):

    sender = await event.get_sender()

    if sender.id == ownerklanr_id :

        order = await event.reply('اهلا مطوري - @MatrixThon')

@matrix.on(admin_cmd(pattern="تفاعلات(?: |$)(.*)"))

async def ma(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("أ‿أ")

        await e.edit("╥﹏╥")

        await e.edit("(;﹏;)")

        await e.edit("(ToT)")

        await e.edit("(┳Д┳)")

        await e.edit("(ಥ﹏ಥ)")

        await e.edit("（；へ：）")

        await e.edit("(T＿T)")

        await e.edit("（πーπ）")

        await e.edit("(Ｔ▽Ｔ)")

        await e.edit("(⋟﹏⋞)")

        await e.edit("（ｉДｉ）")

        await e.edit("(´Д⊂ヽ")

        await e.edit("(;Д;)")

        await e.edit("（>﹏<）")

        await e.edit("(TдT)")

        await e.edit("(つ﹏⊂)")

        await e.edit("༼☯﹏☯༽")

        await e.edit("(ノ﹏ヽ)")

        await e.edit("(ノAヽ)")

        await e.edit("(╥_╥)")

        await e.edit("(T⌓T)")

        await e.edit("(༎ຶ⌑༎ຶ)")

        await e.edit("(☍﹏⁰)｡")

        await e.edit("(ಥ_ʖಥ)")

        await e.edit("(つд⊂)")

        await e.edit("(≖͞_≖̥)")

        await e.edit("(இ﹏இ`｡)")

        await e.edit("༼ಢ_ಢ༽")

        await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")

@matrix.on(admin_cmd(pattern="اخذ قلبي(?: |$)(.*)"))        

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("`\n(\\_/)`"

                     "`\n(●_●)`"

                     "`\n />❤️ اخذ قلبي")

    sleep(3)

    await typew.edit("`\n(\\_/)`"

                     "`\n(●_●)`"

                     "`\n/>💔  رجعلياه مكسور")

    sleep(2)

    await typew.edit("`\n(\\_/)`"

                     "`\n(●_●)`"

                     "`\n💔<\\  اخخخ")      





                  



@matrix.on(admin_cmd(pattern="احبك(?: |$)(.*)"))            

async def ma(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("احبك 💕")

        await e.edit("💝💘💓💗")

        await e.edit("💞💕💗💘")

        await e.edit("💝💘💓💗")

        await e.edit("💞💕💗💘")

        await e.edit("💘💞💗💕")

        await e.edit("💘💞💕💗")

        await e.edit("احبك 💝💖💘")

        await e.edit("💝💘💓💗")

        await e.edit("💞💕💗💘")

        await e.edit("💘💞💕💗")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("احبك 💕")

        await e.edit("💘💘💘💘")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("احبك")

        await e.edit("💕💞💘💝")

        await e.edit("💘💕💞💝")

        await e.edit("احبك💞")            

            

@matrix.on(admin_cmd(pattern="اركض(?: |$)(.*)"))            

async def typewriter(typew):

    typew.pattern_match.group(1)

    await typew.edit("اركض")

    sleep(1)

    await typew.edit("اركض")

    sleep(1)

    await typew.edit("`🏃                        🦖`")

    await typew.edit("`🏃                       🦖`")

    await typew.edit("`🏃                      🦖`")

    await typew.edit("`🏃                     🦖`")

    await typew.edit("`🏃                    🦖`")

    await typew.edit("`🏃                   🦖`")

    await typew.edit("`🏃                  🦖`")

    await typew.edit("`🏃                 🦖`")

    await typew.edit("`🏃                🦖`")

    await typew.edit("`🏃               🦖`")

    await typew.edit("`🏃              🦖`")

    await typew.edit("`🏃             🦖`")

    await typew.edit("`🏃            🦖`")

    await typew.edit("`🏃           🦖`")

    await typew.edit("`🏃           🦖`")

    await typew.edit("`🏃           🦖`")

    await typew.edit("`🏃            🦖`")

    await typew.edit("`🏃             🦖`")

    await typew.edit("`🏃              🦖`")

    await typew.edit("`🏃               🦖`")

    await typew.edit("`🏃                🦖`")

    await typew.edit("`🏃                 🦖`")

    await typew.edit("`🏃                  🦖`")

    await typew.edit("`🏃                   🦖`")

    await typew.edit("`🏃                    🦖`")

    await typew.edit("`🏃                     🦖`")

    await typew.edit("`🏃                    🦖`")

    await typew.edit("`🏃                   🦖`")

    await typew.edit("`🏃                  🦖`")

    await typew.edit("`🏃                 🦖`")

    await typew.edit("`🏃                🦖`")

    await typew.edit("`🏃               🦖`")

    await typew.edit("`🏃              🦖`")

    await typew.edit("`🏃             🦖`")

    await typew.edit("`🏃            🦖`")

    await typew.edit("`🏃           🦖`")

    await typew.edit("`🏃          🦖`")

    await typew.edit("`🏃         🦖`")

    await typew.edit("`🏃       🦖`")

    await typew.edit("`🏃      🦖`")

    await typew.edit("`🏃     🦖`")

    await typew.edit("`🏃    🦖`")

    await typew.edit("`🧎🦖`")

@matrix.on(admin_cmd(pattern="روميو(?: |$)(.*)"))    

async def ma(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    await event.edit(" 💘 ")

    animation_chars = [

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    

            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",

            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",

            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",

            ]

    for i in animation_ttl:

        await sleep(animation_interval)

        await event.edit(animation_chars[i % len(animation_chars)])    

@matrix.on(admin_cmd(pattern="بوسات", outgoing=True))

async def _(event):

		await event.edit("❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘❤😘")

		await asyncio.sleep(1)

		await event.edit("🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘🧡😘")

		await asyncio.sleep(1)

		await event.edit("💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛??💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛??💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘💛😘")

		await asyncio.sleep(1)

		await event.edit("💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘💚😘")

		await asyncio.sleep(1)

		await event.edit("💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘💙😘")

		await asyncio.sleep(1)

		await event.edit("💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘💜😘")

		await asyncio.sleep(1)

		await event.edit("🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎??🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘🤎😘")

		await asyncio.sleep(1)

		await event.edit("💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘💕😘")

		await asyncio.sleep(1)

		await event.edit("💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘💞😘")

		await asyncio.sleep(1)

		await event.edit("💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓??💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘??😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘💓😘")

		await asyncio.sleep(1)

		await event.edit("💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘💗😘")

		await asyncio.sleep(1)

		await event.edit("💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘💖😘")

		await asyncio.sleep(1)

		await event.edit("💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘💘😘")

		await asyncio.sleep(1)

		await event.edit("💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘??😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘💝😘")

		await asyncio.sleep(1)

		await event.edit("️♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥??♥😘♥??♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘♥😘")

		    

@matrix.on(admin_cmd(pattern="(?: |$)(.*)"))    

async def ma(event):

    if event.fwd_from:

        return

    animation_interval = 1.2

    animation_ttl = range(0, 14)

    input_str = event.pattern_match.group(1)

    if input_str == "دبابات":

        await event.edit(input_str)

        animation_chars = [

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",            

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",            

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎆\n🎇🎆🎇🎆🎇🎆🎇",

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",           

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",            

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇\n🎇🎆🎇🎆🎇🎆🎇",

            "🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇\n🎆🎇🎆🎇🎆🎇🎆\n🎇🎆🎇🎆🎇🎆🎇",

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 14])  

@matrix.on(admin_cmd(pattern="رسم قلوب(?:\s|$)([\s\S]*)"))  

async def itachi(event):

    "To get emoji art text."

    args = event.pattern_match.group(1)

    get = await event.get_reply_message()

    if not args and get:

        args = get.text

    if not args:

        await edit_or_reply(

            event, "**᥀︙ قم بكتابه الكلمه بجانب الامر **"

        )

        return

    result = ""

    for a in args:

        a = a.lower()

        if a in emojify.kakashitext:

            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]

            result += char

        else:

            result += a

    await edit_or_reply(event, result)

@matrix.on(admin_cmd(pattern="رسم شعار(?:\s|$)([\s\S]*)"))  

async def itachi(event):

    args = event.pattern_match.group(1)

    get = await event.get_reply_message()

    if not args and get:

        args = get.text

    if not args:

        return await edit_or_reply(

            event, "**᥀︙ قم بكتابه الكلمه بجانب الامر **"

        )

    try:

        emoji, arg = args.split(" ", 1)

    except Exception:

        arg = args

        emoji = "8"

    result = ""

    for a in arg:

        a = a.lower()

        if a in emojify.kakashitext:

            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)

            result += char

        else:

            result += a

    await edit_or_reply(event, result)

@matrix.on(admin_cmd(pattern="بنك( الاعلى|$)"))  

async def _(event):

    "To check ping"

    flag = event.pattern_match.group(1)

    start = datetime.now()

    if flag == " الاعلى":

        catevent = await edit_or_reply(event, "**᥀︙ جاري قياس البنك ...**")

        await asyncio.sleep(0.3)

        await catevent.edit("**᥀︙ جاري قياس البنك ...**")

        await asyncio.sleep(0.3)

        await catevent.edit("**᥀︙ جاري قياس البنك ...**")

        end = datetime.now()

        tms = (end - start).microseconds / 1000

        ms = round((tms - 0.6) / 3, 3)

        await catevent.edit(f"**᥀︙ سرعة الاستجابة للبنك :**  `{ms} بالثانية`  ")

    else:

        catevent = await edit_or_reply(event, "Pong!")

        end = datetime.now()

        ms = (end - start).microseconds / 1000

        await catevent.edit(f"**᥀︙ سرعة الاستجابة للبنك :**  `{ms} بالثانية`  ")

@matrix.on(admin_cmd(pattern="البنك(?:\s|$)([\s\S]*)"))  

async def _(event):

    start = datetime.now()

    animation_interval = 0.3

    animation_ttl = range(26)

    event = await edit_or_reply(event, "**᥀︙ جاري قياس البنك بتسليه ...**")

    animation_chars = [

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",

        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎??⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n \n My 🇵 🇮 🇳 🇬  Is : Calculating...",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 26])

    end = datetime.now()

    ms = (end - start).microseconds / 1000

    await event.edit(        f"‎‎‎‎‎‎‎‎‎⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛⬛📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛📶⬛⬛⬛\n⬛⬛⬛⬛📶⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛📶⬛⬛⬛📶⬛\n⬛⬛📶📶⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶⬛📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n‎‎‎‎‎‎‎‎‎ \n \n My 🇵 🇮 🇳 🇬  Is : {ms} ms"    )

matr = [    "لا خلقۿ ولا اخلاق لحاله عايش ☹.",    "سڪر محلي محطوط على ڪريما 🤤🍰.",    "؏ـسل × ؏ـسل 🍯.",    "أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂.",    "ملڪ جمال ألعالم 🥺💘.",    "أنسان زباله ومكضيها نوم 🙂.",    "يعني بشرفك هوه هذا يستاهل اوصفه؟",    "أنسان ڪيمر 😞💘.",    "جنۿ جڪليته يربيـﮧ 🍬.",    "شمأ اوصف بي قليل 🥵💞.",    "وجۿا جنة كاهي من ألصبحـﮧ ☹♥.",    "هذا واحد يهودي دير بالك منه 🙂💘.",    "هذا انسان يحب مقتدئ ابتعد عنه 😂💞.",    "بس تزحف ع الولد وهيه زرڪة 😂.",    "جنۿ مرڪة شجر شبيك يول 😂😔.",    "هذا حبيبي ، أحبة ڪولش 🙊💘",    "جمالهـﮧ خبلني 😞💞.",    "چنۿ ڪريمة ؏ـلى ڪيك 😞💘.",    "انسان مينطاق 🙂💔.",    "فد أنسان مرتب وريحتة تخبل 🥺💞",    "شڪد حلو هذا ومؤدب 😭💞💘💕.",    "وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞.",    "نتا مخلوق من ڪتله مال عارية 🙂😂.",    "لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺.",    "با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿.",    "شني عمي مو بشر ڪيك ورب 🥺💞.",    "عوفه ضلعي هذا انسان زباله 🙂😂.",    "انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️.",    "باع منو شون بشر هوه وجۿا يطرد النعمة 🙂.",    "عيع فد أنسان وصخ 😂♥.",    "يول هذا طاڪك قطة احسلك 😂💞.",    "لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘.",    "هذا الله غاضب عليه 🌚💔.",    "شنو شنو ؟ تسرسح يله 😒💘.",    "وردة مال الله ، فدوا اروحله 🤤💞.",    "أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞.",    "انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞.",    "أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂.",    "الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞.",    "لكشنو من جمالل هذا يربييييي 😭💞.",    "يومة فديته جنه زربه 😭😂💞.", ]

@matrix.on(admin_cmd(pattern="تهكير(?:\s|$)([\s\S]*)"))  

async def _(event):

    "Fun hack animation."

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        idd = reply_message.sender_id

        if idd == 6373798952:

            await edit_or_reply(

                event, "**᥀︙ عـذرا أنـة مبـرمج السـورس لايـمكن تهكيـرة .**"

            )

        else:

            event = await edit_or_reply(event, "**᥀︙ جـاري التـهكير**")

            animation_chars = [                "**᥀︙ جـاري الاتصـال بجهـاز الضحـية لأختـراقـة**",                "**᥀︙ أختـراق جهـاز الضحـية الهـددف محـدد جـاري أختـراقـة**",                "**᥀︙ تحـميل الاخـتراق  .. 0%**\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق ... 4%**\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",          "**᥀︙ تحـميل الاخـتراق  ...10%**\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق  .. 20%**\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق  .. 36%**\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق  .. 52%**\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق  .. 84%**\n█████████████████████▒▒▒▒ `",                "**᥀︙ تحـميل الاخـتراق  .. 100%**\n████████████████████████`",                f"**᥀︙ تـم اخـتراق الضحـية بواسطه : `{ALIVE_NAME}` . بـدون تنـازل**",

            ]

            animation_interval = 3

            animation_ttl = range(11)

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 11])

    else:

        await edit_or_reply(            event,            "**🝳︙ لم يتم تعريف أي مستخدم قم برد على الضحية**",            parse_mode=_format.parse_pre,        )

@matrix.on(admin_cmd(pattern="اذكار$"))

async def ithker(ahmedpis):

    await ahmedpis.edit(choice(Citation_morning))    

@matrix.on(admin_cmd(pattern="اذكار عشر$"))    

async def ithker(event):

    event = await edit_or_reply(event, "أَصْبَـحْـنا عَلَى فِطْرَةِ الإسْلاَمِ")

    await event.edit("أَعُوذُ بِاللهِ مِنْ الشَّيْطَانِ الرَّجِيمِ اللّهُ لاَ إِلَـهَ إِلاَّ هُوَ الْحَيُّ الْقَيُّومُ لاَ تَأْخُذُهُ سِنَةٌ وَلاَ نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلاَ يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالأَرْضَ وَلاَ يَؤُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ.")

    await asyncio.sleep(5)

    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ هُوَ ٱللَّهُ أَحَدٌ، ٱللَّهُ ٱلصَّمَدُ، لَمْ يَلِدْ وَلَمْ يُولَدْ، وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ.")

    await asyncio.sleep(5)

    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ، مِن شَرِّ مَا خَلَقَ، وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ، وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ، وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ.")

    await asyncio.sleep(5)

    await event.edit("بِسْمِ اللهِ الرَّحْمنِ الرَّحِيم قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ، مَلِكِ ٱلنَّاسِ، إِلَٰهِ ٱلنَّاسِ، مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ، ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ، مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ. ")

    await asyncio.sleep(5)

    await event.edit("أَصْـبَحْنا وَأَصْـبَحَ المُـلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللّهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُـلكُ ولهُ الحَمْـد، وهُوَ على كلّ شَيءٍ قدير، رَبِّ أسْـأَلُـكَ خَـيرَ ما في هـذا اليوم وَخَـيرَ ما بَعْـدَه، وَأَعـوذُ بِكَ مِنْ شَـرِّ ما في هـذا اليوم وَشَرِّ ما بَعْـدَه، رَبِّ أَعـوذُ بِكَ مِنَ الْكَسَـلِ وَسـوءِ الْكِـبَر، رَبِّ أَعـوذُ بِكَ مِنْ عَـذابٍ في النّـارِ وَعَـذابٍ في القَـبْر. ")

    await asyncio.sleep(5)

    await event.edit("اللّهـمَّ أَنْتَ رَبِّـي لا إلهَ إلاّ أَنْتَ، خَلَقْتَنـي وَأَنا عَبْـدُك، وَأَنا عَلـى عَهْـدِكَ وَوَعْـدِكَ ما اسْتَـطَعْـت، أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ. ")

    await asyncio.sleep(5)

    await event.edit("رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً.")

    await asyncio.sleep(5)

    await event.edit("اللّهُـمَّ إِنِّـي أَصْبَـحْتُ أُشْـهِدُك، وَأُشْـهِدُ حَمَلَـةَ عَـرْشِـك، وَمَلَائِكَتَكَ، وَجَمـيعَ خَلْـقِك، أَنَّـكَ أَنْـتَ اللهُ لا إلهَ إلاّ أَنْـتَ وَحْـدَكَ لا شَريكَ لَـك، وَأَنَّ ُ مُحَمّـداً عَبْـدُكَ وَرَسـولُـك.")

    await asyncio.sleep(5)    

    await event.edit("اللّهُـمَّ ما أَصْبَـَحَ بي مِـنْ نِعْـمَةٍ أَو بِأَحَـدٍ مِـنْ خَلْـقِك ، فَمِـنْكَ وَحْـدَكَ لا شريكَ لَـك ، فَلَـكَ الْحَمْـدُ وَلَـكَ الشُّكْـر.")

    await asyncio.sleep(5)

    await event.edit("حَسْبِـيَ اللّهُ لا إلهَ إلاّ هُوَ عَلَـيهِ تَوَكَّـلتُ وَهُوَ رَبُّ العَرْشِ العَظـيم.")

    await asyncio.sleep(5)   



@matrix.on(admin_cmd(pattern="كلام متحرك ([\s\S]*)"))  

async def typewriter(typew):

    message = typew.pattern_match.group(1)

    sleep_time = 0.2

    typing_symbol = "|"

    old_text = ""

    typew = await edit_or_reply(typew, typing_symbol)

    await asyncio.sleep(sleep_time)

    for character in message:

        old_text = old_text + "" + character

        typing_text = old_text + "" + typing_symbol

        await typew.edit(typing_text)

        await asyncio.sleep(sleep_time)

        await typew.edit(old_text)

        await asyncio.sleep(sleep_time)

@matrix.on(admin_cmd(pattern=r"حمامه ?(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return



    await event.edit("--------------🕊")

    await event.edit("-------------🕊️")

    await event.edit("------------🕊️")

    await event.edit("-----------🕊️")

    await event.edit("----------🕊️")

    await event.edit("---------🕊️")

    await event.edit("--------🕊️")

    await event.edit("-------🕊️")

    await event.edit("------??️")

    await event.edit("-----🕊️")

    await event.edit("----🕊️")

    await event.edit("---🕊️")

    await event.edit("--🕊️")

    await event.edit("-🕊️")

    await event.edit("❤️🕊️")

    await asyncio.sleep(3)

    await event.delete()

@matrix.on(admin_cmd(pattern="طياره(?:\s|$)([\s\S]*)"))  

async def meme(event):

    "Animation command."

    memeVar = event.text

    sleepValue = 0.5

    memeVar = memeVar[6:]

    if not memeVar:

        memeVar = "✈️"

    event = await edit_or_reply(event, "-------------" + memeVar)

    await asyncio.sleep(sleepValue)

    await event.edit("------------" + memeVar + "-")

    await asyncio.sleep(sleepValue)

    await event.edit("-----------" + memeVar + "--")

    await asyncio.sleep(sleepValue)

    await event.edit("----------" + memeVar + "---")

    await asyncio.sleep(sleepValue)

    await event.edit("---------" + memeVar + "----")

    await asyncio.sleep(sleepValue)

    await event.edit("--------" + memeVar + "-----")

    await asyncio.sleep(sleepValue)

    await event.edit("-------" + memeVar + "------")

    await asyncio.sleep(sleepValue)

    await event.edit("------" + memeVar + "-------")

    await asyncio.sleep(sleepValue)

    await event.edit("-----" + memeVar + "--------")

    await asyncio.sleep(sleepValue)

    await event.edit("----" + memeVar + "---------")

    await asyncio.sleep(sleepValue)

    await event.edit("---" + memeVar + "----------")

    await asyncio.sleep(sleepValue)

    await event.edit("--" + memeVar + "-----------")

    await asyncio.sleep(sleepValue)

    await event.edit("-" + memeVar + "------------")

    await asyncio.sleep(sleepValue)

    await event.edit(memeVar + "-------------")

    await asyncio.sleep(sleepValue)

    await event.edit("-------------" + memeVar)

    await asyncio.sleep(sleepValue)

    await event.edit("------------" + memeVar + "-")

    await asyncio.sleep(sleepValue)

    await event.edit("-----------" + memeVar + "--")

    await asyncio.sleep(sleepValue)

    await event.edit("----------" + memeVar + "---")

    await asyncio.sleep(sleepValue)

    await event.edit("---------" + memeVar + "----")

    await asyncio.sleep(sleepValue)

    await event.edit("--------" + memeVar + "-----")

    await asyncio.sleep(sleepValue)

    await event.edit("-------" + memeVar + "------")

    await asyncio.sleep(sleepValue)

    await event.edit("------" + memeVar + "-------")

    await asyncio.sleep(sleepValue)

    await event.edit("-----" + memeVar + "--------")

    await asyncio.sleep(sleepValue)

    await event.edit("----" + memeVar + "---------")

    await asyncio.sleep(sleepValue)

    await event.edit("---" + memeVar + "----------")

    await asyncio.sleep(sleepValue)

    await event.edit("--" + memeVar + "-----------")

    await asyncio.sleep(sleepValue)

    await event.edit("-" + memeVar + "------------")

    await asyncio.sleep(sleepValue)

    await event.edit(memeVar + "-------------")

    await asyncio.sleep(sleepValue)

    await event.edit(memeVar)

@matrix.on(admin_cmd(pattern="مصاصه(?: |$)(.*)"))    

async def give(event):

    giveVar = event.text

    sleepValue = 0.5

    lp = giveVar[6:]

    if not lp:

        lp = " 🍭"

    event = await edit_or_reply(event, lp + "        ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + "       ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + "      ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + "     ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + "    ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + "   ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)

    await asyncio.sleep(sleepValue)

    await event.edit(lp + "        ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + "       ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + "      ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + "     ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + "    ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + "   ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")

    await asyncio.sleep(sleepValue)

    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)

@matrix.on(admin_cmd(pattern="نص ثري دي(?:\s|$)([\s\S]*)"))    

async def figlet(event):

    input_str = event.pattern_match.group(1)

    if ";" in input_str:

        cmd, text = input_str.split(";", maxsplit=1)

    elif input_str is not None:

        cmd = None

        text = input_str

    else:

        await edit_or_reply(event, "**🝳︙قم بإعطـاء نـص لتغييـره ␥**")

        return

    style = cmd

    text = text.strip()

    if style is not None:

        try:

            font = CMD_FIG[style.strip()]

        except KeyError:

            return await edit_delete(                event, "**᥀︙تم تحديـد نمـط غيـر صالـح ⚠️**"            )

        result = pyfiglet.figlet_format(deEmojify(text), font=font)

    else:

        result = pyfiglet.figlet_format(deEmojify(text))

    await edit_or_reply(event, result, parse_mode=_format.parse_pre)

hanhi = [    "تف عليك ياخايس",    "كرامتك وين ياقندره",    "تعال كواد اليوم طيزك اشكه ",    "هاه اخي ؟",    "واحد حيوان ومصلحه عوفه ",    "لك حيوان كواد استقر لك",

    " وخر ماسوي شي",    "مااهين حيوانات اني",    "واحد كلب ابن كلب عوفه",    "دعوفه هوه يحصرون بيه وره السده هذا ",    "خطيه هذا مبدلين عقله وحاطين طيزه",    "@matrix",]

@matrix.on(admin_cmd(pattern="نسبه الحب(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(ahmed)

    await edit_or_reply(mention, f"᥀︙ نـسـبتكم انـت و [{mat}](tg://user?id={user.id}) هـي {matr} 😔🖤")

@matrix.on(admin_cmd(pattern="نسبه الانوثه(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبه الانوثه لـ [{mat}](tg://user?id={user.id}) هـي {matr} 🤰")

@matrix.on(admin_cmd(pattern="نسبه الغباء(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبه الغباء لـ [{mat}](tg://user?id={user.id}) هـي {matr} 😂💔")

@matrix.on(admin_cmd(pattern="نسبه الانحراف(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبة الانحراف لـ [{mat}](tg://user?id={user.id}) هـي {matr} 🥵🖤")

@matrix.on(admin_cmd(pattern="نسبه المثليه(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبه المثليه لـ [{mat}](tg://user?id={user.id}) هـي {matr} 🤡 🏳️‍🌈.")

@matrix.on(admin_cmd(pattern="نسبه النجاح(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبه النجاح لـ [{mat}](tg://user?id={user.id}) هـي {matr} 🤓.") 

@matrix.on(admin_cmd(pattern="نسبه الكراهيه(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    matr = random.choice(arb)

    await edit_or_reply(mention, f"᥀︙ نسبه الكراهيه لـ [{mat}](tg://user?id={user.id}) هـي {matr} 🤮.")

async def get_user(event):

    if event.reply_to_msg_id:

        previous_message = await event.get_reply_message()

        replied_user = await event.client(            GetFullUserRequest(previous_message.sender_id)        )

    else:

        user = event.pattern_match.group(1)

        if user.isnumeric():

            user = int(user)



        if not user:

            self_user = await event.client.get_me()

            user = self_user.id



        if event.message.entities:

            probable_user_mention_entity = event.message.entities[0]



            if isinstance(probable_user_mention_entity, MessageEntityMentionName):

                user_id = probable_user_mention_entity.user_id

                replied_user = await event.client(GetFullUserRequest(user_id))

                return replied_user

        try:

            user_object = await event.client.get_entity(user)

            replied_user = await event.client(GetFullUserRequest(user_object.id))



        except (TypeError, ValueError):

            await event.edit("أنا لا أصفع الأجانب ، إنهم قبيحون")

            return None

    return replied_user

@matrix.on(admin_cmd(pattern="صفق(?:\s|$)([\s\S]*)"))    

async def claptext(event):

    textx = await event.get_reply_message()

    if event.pattern_match.group(1):

        query = event.pattern_match.group(1)

    elif textx.message:

        query = textx.message

    else:

        return await edit_or_reply(event, "قم بالرد على الشخص")

    reply_text = "👏 "

    reply_text += query.replace(" ", " 👏 ")

    reply_text += " 👏"

    await edit_or_reply(event, reply_text)

@matrix.on(admin_cmd(pattern="حضر وهمي(?:\s|$)([\s\S]*)"))    

async def gbun(event):

    gbunVar = event.text

    gbunVar = gbunVar[6:]

    mentions = "جاري حظر هذا الشخص...\n`"

    catevent = await edit_or_reply(event, "**☠️**")

    await asyncio.sleep(3.5)

    chat = await event.get_input_chat()

    async for _ in event.client.iter_participants(        chat, filter=ChannelParticipantsAdmins    ):

        mentions += f""

    reply_message = None

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))

        firstname = replied_user.user.first_name

        usname = replied_user.user.username

        idd = reply_message.sender_id

        if idd == 6373798952:

            await catevent.edit(                "عذرا هذا مبرمج السورس احمد"            )

        else:

            jnl = (                "تم حظر المستخدم :"  "[{}](tg://user?id={})"  "\n\n"                "**اسم الشخص  : ** __{}__\n"                "**ايدي الشخص : ** `{}`\n" ).format(firstname, idd, firstname, idd)

            if usname is None:

                jnl += "**معرف الشخص : ** `لايمتلك معرف`\n"

            else:

                jnl += "**معرف الشخص ** : @{}\n".format(usname)

            if len(gbunVar) > 0:

                gbunm = "`{}`".format(gbunVar)

                gbunr = "**السبب : ** مزعج" 

                jnl += gbunr

            else:

                no_reason = "الازعاج "

                jnl += no_reason

            await catevent.edit(jnl)

    else:

        mention = "`تم طرد`"

        await catevent.edit(mention)

@matrix.on(admin_cmd(pattern="رفع مطي(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعه مطي سبورتي 🐴.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع زباله(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعه زباله معفنه 🗑.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع منشئ(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعه منشئ الكروب 👷‍♂️.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع مدير(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعه مدير الكروب 🍚.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع مطور(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعه مطور الكروب 🦾.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع زوجتي(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦ تم رفعها زوجتك  👰🏼‍♀️.** \n**🍚 ¦ بواسطه  :** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع صاك(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تم رفعه صاك 🤴 .** \n**🍚 ¦ بواسطه  : ** {my_mention} ")

@matrix.on(admin_cmd(outgoing=True, pattern=r"^\.لوقو(?: |$)(.*)"))

async def _(event):

    aing = await event.client.get_me()

    text = event.pattern_match.group(1)

    if not text:

        await event.edit("ضع اسم بجانب الامر لعمل لوقو")

    else:

        await event.edit("جاري عمل لوقو ")

    chat = "@KazukoRobot"

    async with event.client.conversation(chat) as conv:

        try:

            msg = await conv.send_message(f"/logo {text}")

            response = await conv.get_response(5)

            logo = await conv.get_response(5)

            await event.client.send_read_acahmedwledge(conv.chat_id)

        except YouBlockedUserError:

            await event.edit(                "**فك الحظر من :** @KazukoRobot !**"            )

            return

        await asyncio.sleep(0.5)

        await event.client.send_file(            event.chat_id,            logo,            caption=f" لوقو ل : [{ALIVE_NAME}](tg://user?id={aing.id})",        )

        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])

        await event.delete()

@matrix.on(admin_cmd(outgoing=True, pattern=r"^\.فيديو$"))

async def _(event):

    try:

        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()

        await event.client.send_file(event.chat_id, response["url"])

        await event.delete()

    except Exception:

        await event.edit("**لا يمكن العثور على إدخال الفيديو.**")

@matrix.on(admin_cmd(pattern="رفع صاكه(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تم رفعها صاكه 👸🏼.** \n**🍚 ¦ بواسطه  : ** {my_mention} ")

kettuet = [  

  "اكثر شي ينرفزك ؟",

  "اخر مكان رحتله ؟",

  "شخص @ تعترفلة بشي ؟",

  "تغار ؟",

  "تعتقد فيه أحد يراقبك 👩🏼‍💻؟",

  "أشخاص ردتهم يبقون وياك ومن عرفو هلشي سوو العكس صارت معك؟",

  "ولادتك بنفس المكان الي هسة عايش بي او لا؟",

  "اكثر شي ينرفزك ؟",

  "تغار ؟",

  "كم تبلغ ذاكرة هاتفك؟",

  "صندوق اسرارك ؟",

  "شخص @ تعترفلة بشي ؟",

  "يومك ضاع على ؟",

  "اغرب شيء حدث في حياتك ؟",

  " نسبة حبك للاكل ؟",

  " حكمة تأمان بيها ؟",

  " اكثر شي ينرفزك ؟",

  " هل تعرضت للظلم من قبل؟",

  " خانوك ؟",

  " تزعلك الدنيا ويرضيك ؟",

  " تاريخ غير حياتك ؟",

  " أجمل سنة ميلادية مرت عليك ؟",

  " ولادتك بنفس المكان الي هسة عايش بي او لا؟",

  " تزعلك الدنيا ويرضيك ؟",

  " ماهي هوايتك؟",

  " دوله ندمت انك سافرت لها ؟",

  "شخص اذا جان بلطلعة تتونس بوجود؟",

  " تاخذ مليون دولار و تضرب خويك؟",

  " تاريخ ميلادك؟",

  "اشكم مره حبيت ؟",

  " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",

  " هل تثق في نفسك ؟",

  " كم مره نمت مع واحده ؟",

  " اسمك الثلاثي ؟",

  "كلمة لشخص خذلك؟",

  "هل انت متسامح ؟",

  "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",

  "عصير لو قهوة؟",

  " صديق أمك ولا أبوك. ؟",

  "تثق بـ احد ؟",

  "كم مره حبيت ؟",

  "اكمل الجملة التالية..... قال رسول الله ص،، انا مدينة العلم وعلي ؟",

  " اوصف حياتك بكلمتين ؟",

  " حياتك محلوا بدون ؟",

  " وش روتينك اليومي؟",

  " شي تسوي من تحس بلملل؟",

  " يوم ميلادك ؟",

  " اكثر مشاكلك بسبب ؟",

  " تزعلك الدنيا ويرضيك ؟",

  " تتوقع فيه احد حاقد عليك ويكرهك ؟",

  "كلمة غريبة من لهجتك ومعناها؟",

" • هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار" ,

"• كيف تشوف الجيل ذا؟",

"• تاريخ لن تنساه📅؟",

"• هل من الممكن أن تقتل أحدهم من أجل المال؟",

"• تؤمن ان في حُب من أول نظرة ولا لا ؟.",

"• ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",

"• طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",

"• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",

"• أطول مدة نمت فيها كم ساعة؟",

"• كلمة غريبة من لهجتك ومعناها؟🤓",

"• ردة فعلك لو مزح معك شخص م تعرفه ؟",

"• شخص تحب تستفزه😈؟",

"• تشوف الغيره انانيه او حب؟",

"• مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",

"• اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",

"• ‏للشباب | آخر مرة وصلك غزل من فتاة؟🌚",

"• أوصف نفسك بكلمة؟",

"• شيء من صغرك ماتغير فيك؟",

"• ردة فعلك لو مزح معك شخص م تعرفه ؟",

"• | اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث شو راح تكون ؟.",

"• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",

"• حاجة تشوف نفسك مبدع فيها ؟",

"• يهمك ملابسك تكون ماركة ؟",

"• يومك ضاع على؟",

"• اذا اكتشفت أن أعز أصدقائك يضمر لك"," السوء، موقفك الصريح؟",

"• هل من الممكن أن تقتل أحدهم من أجل المال؟",

"• كلمه ماسكه معك الفترة هذي ؟",

"• كيف هي أحوال قلبك؟",

"• صريح، مشتاق؟",

"• اغرب اسم مر عليك ؟",

"• تختار أن تكون غبي أو قبيح؟",

"• آخر مرة أكلت أكلتك المفضّلة؟",

"• دوله ندمت انك سافرت لها😁؟",

"• اشياء صعب تتقبلها بسرعه ؟",

"• كلمة لشخص غالي اشتقت إليه؟💕",

"• اكثر شيء تحس انه مات ف مجتمعنا؟",

"• هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",

"• آخر شيء ضاع منك؟",

"• تشوف الغيره انانيه او حب؟",

"• لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",

"• شيء كل م تذكرته تبتسم ...",

"• هل تحبها ولماذا قمت باختيارها؟",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",

"• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",

"• أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟", 

"• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",

"• هل تشعر أن هنالك مَن يُحبك؟",

"• وش الشيء الي تطلع حرتك فيه و زعلت ؟",

"• صوت مغني م تحبه",

"• كم في حسابك البنكي ؟",

"• اذكر موقف ماتنساه بعمرك؟",

"• ردة فعلك لو مزح معك شخص م تعرفه ؟",

"• عندك حس فكاهي ولا نفسية؟",

"• من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",

"• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",

"• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",

"• شيء من صغرك ماتغير فيك؟",

"• هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",

"• هل تحبها ولماذا قمت باختيارها؟",

"• لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",

"• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",

"• كم مره تسبح باليوم",

"• أفضل صفة تحبه بنفسك؟",

"• أجمل شيء حصل معك خلال هاليوم؟",

"• ‏شيء سمعته عالق في ذهنك هاليومين؟",

"• هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",

"• ‏أبرز صفة حسنة في صديقك المقرب؟",

"• ما الذي يشغل بالك في الفترة الحالية؟",

"• آخر مرة ضحكت من كل قلبك؟",

"• احقر الناس هو من ...",

"• اكثر دوله ودك تسافر لها🏞؟",

"• آخر خبر سعيد، متى وصلك؟",

"• ‏نسبة احتياجك للعزلة من 10📊؟",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",

"• أكثر جملة أثرت بك في حياتك؟",

"• لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",

"• آخر مرة ضحكت من كل قلبك؟",

"• وش الشيء الي تطلع حرتك فيه و زعلت ؟",

"• تزعلك الدنيا ويرضيك ؟",

"• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",

"• تعتقد فيه أحد يراقبك👩🏼‍💻؟",

"• احقر الناس هو من ...",

"• شيء من صغرك ماتغير فيك؟",

"• وين نلقى السعاده برايك؟",

"• هل تغارين من صديقاتك؟",

"• أكثر جملة أثرت بك في حياتك؟",

"• كم عدد اللي معطيهم بلوك👹؟",

"• أجمل سنة ميلادية مرت عليك ؟",

"• أوصف نفسك بكلمة؟",

 ]



@matrix.on(admin_cmd(pattern="كت(?: |$)(.*)"))

async def permalink(mention):

    matr = random.choice(kettuet)

    await edit_or_reply(mention, f"**🝳︙ {matr} **")

@matrix.on(admin_cmd(pattern="هينه(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.username.replace("\u2060", "") if user.username else user.first_name

    matr = random.choice(hanhi)

    await edit_or_reply(mention, f"  {matr} ")

@matrix.on(admin_cmd(pattern="ملصق متحرك(?: |$)(.*)"))

async def honkasays(event):

    await event.edit("**جاري التحويل **")

    text = event.pattern_match.group(1)

    if not text:

        return await event.edit("**قم بكتابه الكلمه بجانب الامر**")

    try:

        if not text.endswith("."):

            text = text + "."

        if len(text) <= 9:

            results = await bot.inline_query("honka_says_bot", text)

            await results[2].click(

                event.chat_id,

                silent=True,

                hide_via=True,

            )

        elif len(text) >= 14:

            results = await bot.inline_query("honka_says_bot", text)

            await results[0].click(

                event.chat_id,

                silent=True,

                hide_via=True,

            )

        else:

            results = await bot.inline_query("honka_says_bot", text)

            await results[1].click(

                event.chat_id,

                silent=True,

                hide_via=True,

            )

        await event.delete()

    except ChatSendInlineForbiddenError:

        await event.edit("**جاري التحويل **")

    except ChatSendStickersForbiddenError:

        await event.edit("**جاري التحويل **")

@matrix.on(admin_cmd(pattern="سمايلي(?: |$)(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(6)

    event = await edit_or_reply(event, "سمايلي ....")

    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁"]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 6])

@matrix.on(admin_cmd(pattern="الحياه(?: |$)(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(6)

    event = await edit_or_reply(event, "الحياه ....")

    animation_chars = ["🤱.", "🙇🏻‍♂️.", "🚶🏻‍♂️.", "👨‍🦯 .", "👨‍🦼 .", "⚰️ ."]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 6])

@matrix.on(admin_cmd(pattern="اركضلي(?: |$)(.*)"))

async def _(event):

    catevent = await edit_or_reply(event, "**اركضلي يابه**")

    animation_interval = 0.3

    animation_ttl = range(120)

    animation_chars = [

".────██──────▀▀▀██\n──▄▀█▄▄▄─────▄▀█▄▄▄\n▄▀──█▄▄──────█─█▄▄\n─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n─▀───────▀▀─▀───────▀▀",

".  ────██──────▀▀▀██\n  ──▄▀█▄▄▄─────▄▀█▄▄▄\n  ▄▀──█▄▄──────█─█▄▄\n  ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n  ─▀───────▀▀─▀───────▀▀",

".     ────██──────▀▀▀██\n     ──▄▀█▄▄▄─────▄▀█▄▄▄\n     ▄▀──█▄▄──────█─█▄▄\n     ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n     ─▀───────▀▀─▀───────▀▀",

".        ────██──────▀▀▀██\n        ──▄▀█▄▄▄─────▄▀█▄▄▄\n        ▄▀──█▄▄──────█─█▄▄\n        ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n        ─▀───────▀▀─▀───────▀▀",

".           ────██──────▀▀▀██\n           ──▄▀█▄▄▄─────▄▀█▄▄▄\n           ▄▀──█▄▄──────█─█▄▄\n           ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n           ─▀───────▀▀─▀───────▀▀",

".              ────██──────▀▀▀██\n              ──▄▀█▄▄▄─────▄▀█▄▄▄\n              ▄▀──█▄▄──────█─█▄▄\n              ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n              ─▀───────▀▀─▀───────▀▀",

".                ────██──────▀▀▀██\n                ──▄▀█▄▄▄─────▄▀█▄▄▄\n                ▄▀──█▄▄──────█─█▄▄\n                ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n                ─▀───────▀▀─▀───────▀▀"]



    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await catevent.edit(animation_chars[i % 4])

@matrix.ma_cmd(pattern="بخشيش وعد (.*)")

async def bkshashwid(event):

    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):

        chat = event.chat_id

        await matrix.send_message(chat, "بخشيش")

        await asyncio.sleep(605)

@matrix.ma_cmd(pattern="راتب وعد (.*)")

async def ritebweid(event):

    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):

        chat = event.chat_id

        await matrix.send_message(chat, "راتب")

        await asyncio.sleep(605)

@matrix.ma_cmd(pattern="كلمات وعد (.*)")

async def klmetwed(event):

    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):

        chat = event.chat_id

        await matrix.send_message(chat, "كلمات")

        await asyncio.sleep(0.5)

        masg = await matrix.get_messages(chat, limit=1)

        masg = masg[0].message

        masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)

        if len(masg) == 2:

            msg = masg[0]

            await matrix.send_message(chat, msg)

        else:

            msg = masg[0] + " " + masg[1]

            await matrix.send_message(chat, msg)

@matrix.ma_cmd(pattern="استثمار وعد (.*)")

async def astthmerwadi(event):

    await event.edit(        "**- تم تفعيل الاستثمار ببوت وعد بنجاح لأيقافه ارسل \n`.استثمار وعد 1`"    )

    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):

        chat = event.chat_id

        await matrix.send_message(chat, "فلوسي")

        await asyncio.sleep(0.5)

        masg = await matrix.get_messages(chat, limit=1)

        masg = masg[0].message

        masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)

        msg = masg[0]

        if int(msg) > 500000000:

            await matrix.send_message(chat, f"استثمار {msg}")

            await asyncio.sleep(10)

            mssag2 = await matrix.get_messages(chat, limit=1)

            await mssag2[0].click(text="اي ✅")

        else:

            await matrix.send_message(chat, f"استثمار {msg}")

        await asyncio.sleep(1210)

@matrix.on(admin_cmd(pattern="جكه(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.first_name.replace("\u2060", "") if user.first_name else user.username

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    await edit_or_reply(mention, f"────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀\n\n**᥀ ¦ تنح خل اجكك عزيزي ** [{mat}{mat2}](tg://user?id={user.id})")

@matrix.on(admin_cmd(outgoing=True, pattern=r"^\.فيديو2$"))

async def _(event):

    try:

        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()

        await event.client.send_file(event.chat_id, response["url"])

        await event.delete()

    except Exception:

        await event.edit("**لا يمكن العثور على إدخال الفيديو**")

@matrix.on(admin_cmd(pattern="فايروس(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    await edit_or_reply(mention, f"https://t.me/MatrixrVirus/17")

@matrix.on(admin_cmd(pattern="هلو(?: |$)(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(6)

    event = await edit_or_reply(event, "هلو ....")

    animation_chars = ["🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋", "🙋🔷🙋🙋🙋🔷🙋🙋🔷🔷🔷🙋", "🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋", "🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋", "🙋🔷🔷🔷🔷🔷🙋🙋🙋🔷🙋🙋", "🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋", "🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋", 

"🙋🔷🙋🙋🙋🔷🙋🙋🔷🔷🔷🙋",

"""

🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋

🙋🔷🙋🙋🙋🔷🙋🙋🔷🔷🔷🙋

🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋

🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋

🙋🔷🔷🔷🔷🔷🙋🙋🙋🔷🙋🙋

🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋

🙋🔷🙋🙋🙋🔷🙋🙋🙋🔷🙋🙋

🙋🔷🙋🙋🙋🔷🙋🙋🔷🔷🔷🙋

🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋🙋

"""]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 6])

@matrix.on(admin_cmd(pattern="رئيك(?:\s|$)([\s\S]*)"))

async def permalink(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    if user.id == 6373798952:

        return await edit_or_reply(mention, f"**- هذا مبرمج السورس  **")

    mat = user.username.replace("\u2060", "") if user.username else user.first_name

    matr = random.choice(matr)

    await edit_or_reply(mention, f"  {matr} ")

@matrix.on(admin_cmd(pattern="رفع شيخ(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تـم رفعـة شيـخ المجـموعة 👳‍♂️ (56) .** \n**🍚 ¦ بواسطه  : ** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع تاج(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تـم رفـع تـاج راسـك 🔱 .** \n**🍚 ¦ بواسطه  : ** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع مكبسل(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تـم رفـعه مكبـسل 💊💉 .** \n**🍚 ¦ بواسطه  : ** {my_mention} ")

@matrix.on(admin_cmd(pattern="رفع غبي(?:\s|$)([\s\S]*)"))

async def ma(mention):

    user, custom = await get_user_from_event(mention)

    if not user:

        return

    mat2 = user.last_name.replace("\u2060", "") if user.last_name else user.username

    me = await mention.client.get_me()

    my_first = me.first_name

    my_mention = f"[{me.first_name}](tg://user?id={me.id})"

    await edit_or_reply(mention, f"**᥀ ¦ المستخدم ⪼ • ** [{mat2}](tg://user?id={user.id}) \n ☑️ **¦  تـم رفـعه غـبي 🛏️ .** \n**🍚 ¦ بواسطه  : ** {my_mention} ")


@bot.on(admin_cmd(outgoing=True, pattern="(أوامري|اوامري)"))
async def repomatrix(matrix):
    if matrix.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    
    if matrix.reply_to_msg_id:
        try:
            await matrix.get_reply_message()
            response = await bot.inline_query(TG_BOT, "(اوامري|أوامري)")
            await response[0].click(matrix.chat_id)
            await matrix.delete()
        except BotInlineDisabledError: 
            await matrix.send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا" )
