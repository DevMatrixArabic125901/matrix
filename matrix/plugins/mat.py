import asyncio
import time
from matrix import matrix
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from telethon.events import NewMessage
import requests
from telethon.tl.functions.users import GetFullUserRequest
from ..Config import Config
import re
from telethon import events
@matrix.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    if matrixiq1[0] == "yes":
        await event.edit("**سيتم تجميع المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await matrix.get_entity("@EEObot")
        await matrix.send_message("@EEObot", '/start')
        await asyncio.sleep(5)
        msg0 = await matrix.get_messages("@EEObot", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await matrix.get_messages("@EEObot", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if matrixiq1[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await matrix(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع المليار بطريقه مختلفه') != -1:
                await matrix.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await matrix(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await matrix(ImportChatInviteRequest(bott))
                msg2 = await matrix.get_messages("@EEObot", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await matrix.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await matrix.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await matrix.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

matrixiq2 = ['yes']
@matrix.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if matrixiq2[0] == "yes":
        await event.edit("**سيتم تجميع  , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await matrix.get_entity("@MARKTEBOT")
        await matrix.send_message("@MARKTEBOT", '/start')
        await asyncio.sleep(5)
        msg0 = await matrix.get_messages("@MARKTEBOT", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await matrix.get_messages("@MARKTEBOT", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if matrixiq2[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await matrix(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لايوجد قنوات خلصت') != -1:
                await matrix.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await matrix(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await matrix(ImportChatInviteRequest(bott))
                msg2 = await matrix.get_messages("@MARKTEBOT", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await matrix.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await matrix.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await matrix.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

matrixiq3 = ['yes']
@matrix.on(admin_cmd(pattern="(تجميع العرب|تجميع عرب)"))
async def _(event):
    if matrixiq3[0] == "yes":
        await event.edit("**سيتم تجميع  , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await matrix.get_entity("@xnsex21bot")
        await matrix.send_message("@xnsex21bot", '/start')
        await asyncio.sleep(5)
        msg0 = await matrix.get_messages("@xnsex21bot", limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await matrix.get_messages("@xnsex21bot", limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if matrixiq3[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await matrix(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لايوجد قنوات') != -1:
                await matrix.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await matrix(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await matrix(ImportChatInviteRequest(bott))
                msg2 = await matrix.get_messages("@xnsex21bot", limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await matrix.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await matrix.send_message(event.chat_id, f"**خطأ حاول بعد 6 ساعات**")
                break
        await matrix.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")
