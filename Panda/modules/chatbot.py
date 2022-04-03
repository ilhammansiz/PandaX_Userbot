# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from .. import LOGS, bot
from ..sql_helper.tede_chatbot_sql import is_tede, rem_tede, set_tede
from . import edit_or_reply, ilhammansiz_cmd
plugin_category = "modules"

translator = Translator()
LANGUAGE = "id"

url = "https://api-tede.herokuapp.com/api/chatbot?message={message}"


async def ngapain_rep(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return (data.json())["msg"]
        LOGS.info("ERROR: API chatbot sedang down, report ke @tedesupport.")
    except Exception as e:
        LOGS.info(str(e))


async def chat_bot_toggle(event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if not is_tede(chat_id):
            set_tede(chat_id)
            return await edit_or_reply(event, "**ChatBot Berhasil Diaktifkan!**")
        await edit_or_reply(event, "ChatBot Sudah Diaktifkan.")
    elif status == "off":
        if is_tede(chat_id):
            rem_tede(chat_id)
            return await edit_or_reply(event, "**ChatBot Berhasil Dinonaktifkan!**")
        await edit_or_reply(event, "ChatBot Sudah Dinonaktifkan.")
    else:
        await edit_or_reply(event, "**Usage:** `.chatbot` <on/off>")

@ilhammansiz_cmd(
    pattern="chatbot(?: |$)(.*)"",
    command=("chatbot", plugin_category),
    info={
        "header": "** Untuk membalas chat dengan chatbot AI.",
        "usage": ["{tr}chatbot` <on/off>"],
    },
)
async def on_apa_off(event):
    await chat_bot_toggle(event)


@bot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned),
    ),
)
async def tede_chatbot(event):
    sender = await event.get_sender()
    if not is_tede(event.chat_id):
        return
    if not isinstance(sender, User):
        return
    if event.text:
        rep = await ngapain_rep(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)

