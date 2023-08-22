import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import MatrixUserBotClient

__version__ = "5.0.0"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "matrix"

try:
    matrix = MatrixUserBotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"كود تيرمكس  - {str(e)}")
    sys.exit()


matrix.tgbot = tgbot = MatrixUserBotClient(
    session="Sessionszbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)
