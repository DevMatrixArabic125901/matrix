import re
import asyncio
import calendar
import json
import os
from telethon import events
from asyncio.exceptions import TimeoutError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ExportChatInviteRequest
from matrix import matrix
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import get_user_from_event, sanga_seperator
from bs4 import BeautifulSoup
from ..helpers.utils import _format
from datetime import datetime
from urllib.parse import quote
import barcode
import qrcode
import requests
from barcode.writer import ImageWriter
from bs4 import BeautifulSoup
from PIL import Image, ImageColor
from telethon.errors.rpcerrorlist import YouBlockedUserError
from matrix import matrix
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from matrix.utils import admin_cmd
from ..helpers import AioHttp
from ..helpers.utils import _catutils, _format, reply_id
LOGS = logging.getLogger(__name__)
IQMOG = re.compile(
    "[" 
    "\U0001F1E0-\U0001F1FF"      "\U0001F300-\U0001F5FF"      "\U0001F600-\U0001F64F"   "\U0001F680-\U0001F6FF"  
    "\U0001F700-\U0001F77F"      "\U0001F780-\U0001F7FF"      "\U0001F800-\U0001F8FF"     "\U0001F900-\U0001F9FF"      "\U0001FA00-\U0001FA6F"  
    "\U0001FA70-\U0001FAFF"      "\U00002702-\U000027B0"      
    "]+")

def iqtfy(inputString: str) -> str:
    return re.sub(IQMOG, "", inputString)

@matrix.on(admin_cmd(pattern="اكس او(?: |$)(.*)"))
async def iq(matrix):
    kn = matrix.pattern_match.group(1)
    if not kn:
        if matrix.is_reply:
            (await matrix.get_reply_message()).message

            return
    LLL5L = await bot.inline_query("xobot", f"{(iqtfy(kn))}")
    await LLL5L[0].click(
        matrix.chat_id,
        reply_to=matrix.reply_to_msg_id,
        silent=True if matrix.is_reply else False,
        hide_via=True)
@matrix.on(admin_cmd(pattern="همسه ?(.*)"))
async def iq(matrix):
    if matrix.fwd_from:
        return
    kkno = matrix.pattern_match.group(1)
    donttag = "@whisperBot"
    if matrix.reply_to_msg_id:
        await matrix.get_reply_message()
    l5 = await bot.inline_query(donttag, kkno)
    await l5[0].click(matrix.chat_id)
    await matrix.delete()
@matrix.on(admin_cmd(pattern="حالتي ?(.*)"))
async def iq(matrix):
    await matrix.edit("جاري الفحص")
    async with bot.conversation("@SpamBot") as l5:
        try:
            dontTag = l5.wait_event(
                events.NewMessage(incoming=True, from_users=178220800))
            await l5.send_message("/start")
            dontTag = await dontTag
            await bot.send_read_acknowledge(l5.chat_id)
        except YouBlockedUserError:
            await matrix.edit("**قم بفك حظر @SpamBot للاكمال**")
            return
        await matrix.edit(f"~ {dontTag.message.message}")    
@matrix.on(admin_cmd(pattern="بي دي اف ?(.*)"))
async def _(matrix):
    if not matrix.reply_to_msg_id:
        return await matrix.edit("**الرجاء الرد على أي نص**")
    reply_message = await matrix.get_reply_message()
    chat = "@office2pdf_bot"
    await matrix.edit("**جاري تحويل إلى PDF...**")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(reply_message)
                convert = await conv.send_message("/ready2conv")
                cnfrm = await conv.get_response()
                editfilename = await conv.send_message("نعم")
                enterfilename = await conv.get_response()
                filename = await conv.send_message("matrix")
                started = await conv.get_response()
                pdf = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await matrix.edit("**قم بفك الحظر من البوت : @office2pdf_bot **")
                return
            await matrix.client.send_message(event.chat_id, pdf)
            await matrix.client.delete_messages(                conv.chat_id,                [
                    msg_start.id,
                    response.id,
                    msg.id,
                    started.id,
                    filename.id,
                    editfilename.id,
                    enterfilename.id,
                    cnfrm.id,
                    pdf.id,
                    convert.id,
                ],)
            await matrix.delete()
    except TimeoutError:
        return await matrix.edit("**هناك خطا نعتذر**") 
@matrix.on(admin_cmd(pattern="بوتي$"))
async def iq(iqbot):
    TG_BOT_USERNAME = Config.TG_BOT_USERNAME
    await iqbot.reply(f"**بوت ماتركس العربي الخاص بك : {TG_BOT_USERNAME}**")
@matrix.on(admin_cmd(pattern="ملصقي ?(.*)"))
async def iq(matrix):
    if matrix.fwd_from:
        return
    if not matrix.reply_to_msg_id:
        await edit_delete(matrix, "**الرجاء الرد على الرسالة**")
        return
    reply_message = await matrix.get_reply_message()
    warna = matrix.pattern_match.group(1)
    chat = "@QuotLyBot"
    await edit_or_reply(matrix, "**جاري...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1031952739))
            first = await conv.send_message(f"/start")
            ok = await conv.get_response()
            await asyncio.sleep(2)
            second = await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await matrix.reply("**قم بفك الحظر من البوت : @QuotLyBot **")
            return
        if response.text.startswith("Hi!"):
            await edit_or_reply(
                matrix, "**الرجاء تعطيل إعادة توجيه إعدادات الخصوصية الخاصة بك**")
        else:
            await matrix.delete()
            await bot.forward_messages(matrix.chat_id, response.message)
    await bot.delete_messages(conv.chat_id, [first.id, ok.id, second.id, response.id])
@matrix.on(admin_cmd(pattern="اسم الاغنيه ?(.*)"))
async def iq(matrix):
    if not matrix.reply_to_msg_id:
        return await matrix.edit("**الرجاء الرد على الرسالة**")
    reply_message = await matrix.get_reply_message()
    chat = "@auddbot"
    try:
        async with matrix.client.conversation(chat) as conv:
            try:
                await matrix.edit("**التعرف على الأغاني...**")
                start_msg = await conv.send_message("/start")
                await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await matrix.edit(
                        "**حدث خطأ أثناء تحديد الأغنية. حاول استخدام رسالة صوتية تتراوح مدتها من 5 إلى 10 ثوانٍ.**")
                await matrix.edit("**انتظر لحظة...**")
                result = await conv.get_response()
                await matrix.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await matrix.edit("**قم بفك الحظر من البوت : @auddbot dan coba lagi:")
                return
            namem = f"**إسم الأغنية : {result.text.splitlines()[0]}**\
        \n\n**تفاصيل : {result.text.splitlines()[2]}**"
            await matrix.edit(namem)
            await matrix.client.delete_messages(                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id]            )
    except TimeoutError:
        return await matrix.edit(            "**هناك خطا نعتذر**")
@matrix.on(admin_cmd(pattern="انشاء بريد(?: |$)(.*)"))
async def _(matrix):
    chat = "@TempMailBot"
    geez = await matrix.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(                incoming=True,                from_users=220112646            )            )            
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            matrixbot = ((response).reply_markup.rows[2].buttons[0].url)
            await matrix.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**قم بفتح الحظر عن : @TempMailBot للأستمرار بانشاء البريدات**")
            return
        await matrix.edit(f"بريدك الخاص هوه : ~ `{response.message.message}`\n[انقر هنا للتحقق من رسائل بريدك]({matrixbot})")
@matrix.on(admin_cmd(pattern="سجل الاسماء(ألف)?(?:\s|$)([\s\S]*)"))
async def _(matrix):  # sourcery no-metrics
    input_str = "".join(matrix.text.split(maxsplit=1)[1:])
    reply_message = await matrix.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(matrix, "**♛ ⦙ قم بالـرد على رسالـة لمستخـدم للحصـول على إسمـه/سجل يوزراتـه أو قم بإعطـاء آيـدي المستخـدم/يـوزر المستخـدم ✦**")
    user, rank = await get_user_from_event(matrix, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    iqevent = await edit_or_reply(matrix, "**♛ ⦙ جـاري المعالجـة ↯**")
    async with matrix.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(matrix, "**♛ ⦙ قم بإلغـاء حظـر @Sangmatainfo_bot ثم حـاول !!**")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await matrix.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(matrix, "**♛ ⦙ لا يستطيـع البـوت جلـب النتائـج ⚠️**")
    if "No records found" in responses:
        await edit_delete(matrix, "**♛ ⦙ المستخـدم ليـس لديـه أيّ سجـل ✕**")
    names, usernames = await sanga_seperator(responses)
    cmd = matrix.pattern_match.group(1)
    sandy = None
    check = usernames if cmd == "u" else names
    for i in check:
        if sandy:
            await matrix.reply(i, parse_mode=_format.parse_pre)
        else:
            sandy = True
            await iqevent.edit(i, parse_mode=_format.parse_pre)
@matrix.on(admin_cmd(pattern="تيك توك(?: |$)(.*)"))
async def _(matrix):
    reply_message = await matrix.get_reply_message()
    if not reply_message:
        await edit_or_reply(matrix, "**♛ ⦙  الرد على الرابط.**")
        return
    if not reply_message.text:
        await edit_or_reply(matrix, "**♛ ⦙  الرد على الرابط.**")
        return
    chat = "@fs0bot"
    iqevent = await edit_or_reply(matrix, "**♛ ⦙  جاري تحميل الرابط**")
    async with matrix.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1354606430))
            await matrix.client.forward_messages(chat, reply_message)
            response = await response
            await matrix.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("**♛ ⦙  فك الحظر من البوت : @fs0bot**")
            return
        if response.text.startswith("؟"):
            await iqevent.edit("?")
        else:
            await iqevent.delete()
            await matrix.client.send_message(matrix.chat_id, response.message)
@matrix.on(admin_cmd(pattern="زخرفه_عربي ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@i0zbot"
    catevent = await edit_or_reply(event, "**جـارِ الزغـرفـه 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1229877081)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("** تحـقق من انـك لم تقـم بحظر البوت @i0zbot .. ثم اعـد استخدام الامـر ... ♥️**")
            return
        if response.text.startswith("رجاء قم بالرد على الكلمه التي تريد زخرفتها "):
            await catevent.edit("رجاء قم بالرد على الكلمه التي تريد زخرفتها")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
@matrix.on(admin_cmd(pattern="زخرفه_انكليزي ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@zagtelethonbot"
    catevent = await edit_or_reply(event, "**جـارِ الزغـرفـه 💞🧸...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1943073737)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("** تحـقق من انـك لم تقـم بحظر البوت @zagtelethonbot .. ثم اعـد استخدام الامـر ... ♥️**")
            return
        if response.text.startswith("رجاء قم بالرد على الكلمه التي تريد زخرفتها "):
            await catevent.edit("رجاء قم بالرد على الكلمه التي تريد زخرفتها")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)
@matrix.on(admin_cmd(pattern="انستا (.*)"))
async def iq(matrixinsta):
    chat = "@instasavegrambot"
    link = matrixinsta.pattern_match.group(1)
    if "www.instagram.com" not in link:
        await edit_or_reply(matrixinsta, "يجب كتابة رابط")
    else:
        start = datetime.now()
        iqevent = await edit_or_reply(matrixinsta, "جار التحميل  🔍")
    async with matrixinsta.client.conversation(chat) as knov:
        try:
            msg_start = await knov.send_message("/start")
            response = await knov.get_response()
            msg = await knov.send_message(link)
            video = await knov.get_response()
            details = await knov.get_response()
            await matrixinsta.client.send_read_acknowledge(knov.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("بفتح الحظر  @instasavegrambot")
            return
        await iqevent.delete()
        l5 = await matrixinsta.client.send_file(matrixinsta.chat_id, video)
        end = datetime.now()
        (end - start).seconds
        await l5.edit(f"تم تنزيل", parse_mode="html")
    await matrixinsta.client.delete_messages(knov.chat_id, [msg_start.id, response.id, msg.id, video.id, details.id])
@matrix.on(admin_cmd(pattern="هديه ?(.*)"))
async def iq(matrix):
    kkno = matrix.pattern_match.group(1)
    donttag = "@i4bot"
    if matrix.reply_to_msg_id:
        await matrix.get_reply_message()
    l5 = await bot.inline_query(donttag, kkno)
    await l5[0].click(matrix.chat_id)
    await matrix.delete()
@matrix.on(admin_cmd(pattern="كشف الفايروسات( -i)?$"))    
async def _IQ(matrix):
    input_str = matrix.pattern_match.group(1)
    if not matrix.reply_to_msg_id:
        return await edit_or_reply(matrix, "الرد على أي رسالة مستخدم.")
    reply_message = await matrix.get_reply_message()
    if not reply_message.media:
        return await edit_or_reply(matrix, "الرد على الملف")
    chat = "@VS_Robot"
    IQevent = await edit_or_reply(matrix, " انتضر قليلا")
    async with matrix.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await matrix.client.forward_messages(chat, reply_message)
            response1 = await conv.get_response()
            if response1.text:
                await matrix.client.send_read_acknowledge(conv.chat_id)
                return await IQevent.edit(response1.text, parse_mode=_format.parse_pre)
            await conv.get_response()
            await matrix.client.send_read_acknowledge(conv.chat_id)
            response3 = await conv.get_response()
            response4 = await conv.get_response()
            await matrix.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await IQevent.edit("قم بفتح الحظر من : @VS_Robot")
        if not input_str:
            return await edit_or_reply(IQevent, response4.text)
        await IQevent.delete()
        await matrix.client.send_file(matrix.chat_id, response3.media, reply_to=(await reply_id(matrix)))
@matrix.on(admin_cmd(pattern="تقويم ([\s\S]*)"))    
async def _iq(matrix):
    input_str = matrix.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) != 2:
        return await edit_delete(matrix, "**تصحيح قم بكتابه الأمر هكذا : **`.تقويم السنه الشهر `", 5)

    yyyy = input_sgra[0]
    mm = input_sgra[1]
    try:
        output_result = calendar.month(int(yyyy.strip()), int(mm.strip()))
        await edit_or_reply(matrix, f"```{output_result}```")
    except Exception as e:
        await edit_delete(matrix, f"                                              **خطأ :**\n`{str(e)}`                       ", 5)


@matrix.on(admin_cmd(pattern="سؤال ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@VidogramAIbot"
    iqtevent = await edit_or_reply(event, "**جاري الجواب عن سؤالك لديك 10 اسئلة فقط خلال كل 24 ساعة ChatGPT ..**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(                events.NewMessage(incoming=True, from_users=6107640967)            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await iqtevent.edit("** تحـقق من انـك لم تقـم بحظر البوت @VidogramAIbot .. ثم اعـد استخدام الامـر ... ♥️**")
            return
        if response.text.startswith("قم بوضع سؤالك بجانب الأمر"):
            await iqtevent.edit("قم بوضع سؤالك بجانب الأمر")
        else:
            await iqtevent.delete()
            await event.client.send_message(event.chat_id, response.message)
