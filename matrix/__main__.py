from telethon.tl.functions.messages import GetMessagesViewsRequest
import sys, asyncio
import matrix
from matrix import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import matrix
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup, inlinematrix
LOGS = logging.getLogger("MATRIX")
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدء تنصيب ماتركس العربي")
    matrix.loop.run_until_complete(setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل الاونلاين")
    matrix.loop.run_until_complete(inlinematrix())
    LOGS.info("تم تفعيل الاونلاين")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await matrix.get_entity(channel_id)
            async for message in matrix.iter_messages(entity=channel.id, limit=5):
                try:
                    await matrix(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True))
                except Exception as error:
                    print ("🔻")
            return True

        except Exception as error:
            print ("🔻")

    async def start_bot():
      try:
          List = ["MatrixThon","MatrxSupport"]
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              Join = await matrix(JoinChannelRequest(channel=id))
              MarkAsRead = await MarkAsViewed(id)
              print (MarkAsRead, "🔻")
          return True
      except Exception as e:
        print("🔻")
        return False
    
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"<b> اهلا بك لقد نصبت ماتركس العربي بنجاح اذهب الى قناتنا لمعرفة المزيـد </b>\n CH : https://t.me/MatrixThon ")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    
    Checker = await start_bot()
    if Checker == False:
        print("#1")
    else:
        print ("🔻")
    
    return


matrix.loop.run_until_complete(startup_process())
    
if len(sys.argv) not in (1, 3, 4):
    matrix.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        matrix.run_until_disconnected()
    except ConnectionError:
        pass
