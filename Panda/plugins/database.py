# Heroku manager for your pandauserbot

# Ilham mansiz

import asyncio
import math
import os
from validators.url import url
from Panda.core.logger import logging

import heroku3
import requests
import urllib3

from Panda import SqL
from . import BOTLOG_CHATID, ilhammansiz_cmd
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "plugins"
LOGS = logging.getLogger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

gvarstatus = SqL.getdb
addgvar = SqL.setdb
delgvar = SqL.deldb

@ilhammansiz_cmd(
    pattern="(set|get|del) var (.*)",
    command=("var", plugin_category),
    info={
        "header": "To manage heroku vars.",
        "flags": {
            "set": "To set new var in heroku or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "usage": [
            "{tr}set var <var name> <var value>",
            "{tr}get var <var name>",
            "{tr}del var <var name>",
        ],
        "examples": [
            "{tr}get var ALIVE_NAME",
        ],
    },
)
async def variable(var):  # sourcery no-metrics
    """
    Manage most of ConfigVars setting, set new var, get current var, or delete var...
    """
    if (Config.HEROKU_API_KEY is None) or (Config.HEROKU_APP_NAME is None):
        return await edit_delete(
            var,
            "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",
        )
    app = Heroku.app(Config.HEROKU_APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        panda = await edit_or_reply(var, "`Getting information...`")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await panda.edit(
                    "**ConfigVars**:" f"\n\n`{variable}` = `{heroku_var[variable]}`\n"
                )
            await panda.edit(
                "**ConfigVars**:" f"\n\n__Error:\n-> __`{variable}`__ don't exists__"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                await edit_or_reply(
                    panda,
                    "`[HEROKU]` ConfigVars:\n\n"
                    "================================"
                    f"\n```{result}```\n"
                    "================================",
                )
            os.remove("configs.json")
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        panda = await edit_or_reply(var, "`Setting information...`")
        if not variable:
            return await panda.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await panda.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await panda.edit(f"`{variable}` **successfully changed to  ->  **`{value}`")
        else:
            await panda.edit(
                f"`{variable}`**  successfully added with value`  ->  **{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        panda = await edit_or_reply(
            var, "`Getting information to deleting variable...`"
        )
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await panda.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await panda.edit(f"`{variable}`**  does not exist**")

        await panda.edit(f"`{variable}`  **successfully deleted**")
        del heroku_var[variable]


@ilhammansiz_cmd(
    pattern="usage$",
    command=("usage", plugin_category),
    info={
        "header": "To Check dyno usage of userbot and also to know how much left.",
        "usage": "{tr}usage",
    },
)
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",
        )
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
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
    return await dyno.edit(
        "**Dyno Usage**:\n\n"
        f" -> `🐼 Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n"
        f"     🐼  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> `🐼 Dyno hours quota remaining this month`:\n"
        f"     🐼  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


@ilhammansiz_cmd(
    pattern="(herokulogs|logs)$",
    command=("logs", plugin_category),
    info={
        "header": "To get recent 100 lines logs from heroku.",
        "usage": ["{tr}herokulogs", "{tr}logs"],
    },
)
async def _(dyno):
    "To get recent 100 lines logs from heroku"
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(
            dyno,
            "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except:
        return await edit_or_reply(dyno,
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    v = await dyno.edit("Getting Logs....")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await v.edit("Got the logs wait a sec")
    await dyno.client.send_file(
        dyno.chat_id,
        "logs.txt",
        reply_to=dyno.id,
        caption="Panda-Userbot Logs.",
    )

    await asyncio.sleep(5)
    await v.delete()
    return os.remove("logs.txt")



def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)



valuess = """
    `ALIVE_PIC`
    `CUSTOM_ALIVE_TEXT`
    `HELP_EMOJI`
    `HELP_TEXT_INLINE`
    `ALIVE_NAME`
    `PM_TEXT`
    `PM_BLOCK`
    `NO_OF_ROWS_IN_HELP`
    `NO_OF_COLUMNS_IN_HELP`
    `PANDA_HELP_LOGO`
"""

vlist = [
    "ALIVE_PIC",
    "CUSTOM_ALIVE_TEXT",
    "HELP_EMOJI",
    "HELP_TEXT_INLINE",
    "ALIVE_NAME",
    "PM_TEXT",
    "PM_BLOCK",
    "NO_OF_ROWS_IN_HELP",
    "NO_OF_COLUMNS_IN_HELP",
]

oldvars = {
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}


@ilhammansiz_cmd(
    pattern="(set|get|del)db(?: |$)([\s\S]*)",
    command=("db", plugin_category),
    info={
        "header": "Set vars in database or Check or Delete",
        "description": "Set , Fetch or Delete values or vars directly in database without restart or heroku vars.\n\nYou can set multiple pics by giving space after links in alive, pm permit.",
        "flags": {
            "set": "To set new var in database or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "var name": f"{valuess}",
        "usage": [
            "{tr}setdb <var name> <var value>",
            "{tr}getdb <var name>",
            "{tr}deldb <var name>",
        ],
        "examples": [
            "{tr}setdb ALIVE_PIC <pic link>",
            "{tr}setdb ALIVE_PIC <pic link 1> <pic link 2>",
            "{tr}getdb ALIVE_PIC",
            "{tr}deldb ALIVE_PIC",
        ],
    },
)
async def panda(event):  # sourcery no-metrics
    "To manage vars in database"
    cmd = event.pattern_match.group(1)
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "set":
            if not vinfo:
                return await edit_delete(
                    event, f"Berhasil Mengubah {vname}"
                )
            check = vinfo.split(" ")
            for i in check:
                if "PIC" in vname and not url(i):
                    return await edit_delete(event, "**Give me a correct link...**")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#SET_DATAVAR\
                    \n**{vname}** is updated newly in database as below",
                )
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(
                event, f"📑 Value of **{vname}** is changed to :- `{vinfo}`", time=20
            )
        if cmd == "get":
            var_data = gvarstatus(vname)
            await edit_delete(
                event, f"📑 Value of **{vname}** is  `{var_data}`", time=20
            )
        elif cmd == "del":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#DEL_DATAVAR\
                    \n**{vname}** is deleted from database",
                )
            await edit_delete(
                event,
                f"📑 Value of **{vname}** is now deleted & set to default.",
                time=20,
            )
    else:
        await edit_delete(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )
