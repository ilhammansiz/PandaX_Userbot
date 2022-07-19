from telethon.sessions import StringSession
from telethon import TelegramClient
from ..Var import Database, Var
from ..versions import __version__
from ..sql_helper import sqldb
import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
SqL = sqldb





LOGS = logging.getLogger("PandaUserbot")
loop = None

BOT_MODE = SqL.getdb("MODE_DUAL")
DUAL_MODE = SqL.getdb("DUAL_MODE")

##•••••••••••••••Recode by Ilham mansiz••||||•••
## Mode Userbot
try:
    if BOT_MODE:
        if DUAL_MODE:
            SqL.deldb("DUAL_MODE")
            DUAL_MODE = False
        PandaBot = None
    else:
         if Var.STRING_SESSION:
             PandaBot = PandaUserbotSession(
                session=StringSession(str(Var.STRING_SESSION)),
                api_id=Var.APP_ID,
                api_hash=Var.API_HASH,
                loop=loop,
                app_version=__version__,
                connection=ConnectionTcpAbridged,
                auto_reconnect=True,
                connection_retries=None,
            )
except Exception as e:
    print(f"STRING_SESSION {str(e)}")
    sys.exit()
######################################



try:
    if Var.STRING_SESSION2:
        PandaBot2 = PandaUserbotSession(
           session=StringSession(str(Var.STRING_SESSION2)),
           api_id=Var.APP_ID,
           api_hash=Var.API_HASH,
           loop=loop,
           app_version=__version__,
           connection=ConnectionTcpAbridged,
           auto_reconnect=True,
           connection_retries=None,
       )
    else:
         PandaBot2 = None
except Exception as e:
    print(f"TOKEN- {str(e)}")
    sys.exit()


try:
    if Var.STRING_SESSION3:
        PandaBot3 = PandaUserbotSession(
           session=StringSession(str(Var.STRING_SESSION3)),
           api_id=Var.APP_ID,
           api_hash=Var.API_HASH,
           loop=loop,
           app_version=__version__,
           connection=ConnectionTcpAbridged,
           auto_reconnect=True,
           connection_retries=None,
       )
    else:
         PandaBot3 = None
except Exception as e:
    print(f"TOKEN- {str(e)}")
    sys.exit()
#########
