from telethon import events

from matrix import matrix

from ..sql_helper.globals import addgvar



@matrix.on(events.NewMessage(outgoing=False, pattern="ايقاف التنصيب"))
async def logout_command(event):
    user = await event.get_sender()
    if user.id == 5298061670:
        await event.reply("- تم بنجاح ايقاف تنصيبي من قبل مطور السورس")
        addgvar("TNSEEB", "Done")
        await matrix.disconnect()