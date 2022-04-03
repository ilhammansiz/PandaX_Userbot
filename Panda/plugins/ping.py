import asyncio
from datetime import datetime

from . import mention, ilhammansiz_cmd
from ..core.managers import edit_or_reply

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        pandaevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🚶`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🏃`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await pandaevent.edit(f"𝗣𝗶𝗻𝗴\n`{ms} ms`")
    else:
        pandaevent = await edit_or_reply(event, "🐼")
        await pandaevent.edit("⚡")
        await pandaevent.edit("👍")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await pandaevent.edit(
            f"┏━《 **𝗣 𝗔 𝗡 𝗗 𝗔** 》━\n"
            f"┣➠  __Ping:__ `{ms} ms`\n"
            f"┗➠ 𝗢𝘄𝗻𝗲𝗿𝘀: {mention} "
        )
