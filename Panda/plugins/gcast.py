# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
# Recode by Ilham Mansiez

import asyncio

from telethon.errors.rpcerrorlist import FloodWaitError

import Panda
from . import ilhammansiz_cmd
plugin_category = "plugins"



@ilhammansiz_cmd(
    pattern="gcast(?: |$)(.*)",
    command=("gcast", plugin_category),
    info={
        "header": "Promosi kesemua grup yang dimasuki ",
        "usage": "{tr}gcast text/media",
    },
)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Saya Text Untuk Di Broadcast**")
    kk = await edit_or_reply(event, "`• 📢 Global Broadcast Di Prosess Cok...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in Panda.Gblacklist:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **Grup, Broadcast Gagal Terkirim =** `{er}`**Grup**╰✠╼━━━━━━❖━━━━━━━✠╯**"
    )





@ilhammansiz_cmd(
    pattern="gucast(?: |$)(.*)",
    command=("gucast", plugin_category),
    info={
        "header": "Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)",
        "usage": "{tr}gucast text/media",
    },
)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting processing...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in Panda.DEVLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **chat, Gagal Mengirim Pesan Ke = `{er}`**╰✠╼━━━━━━❖━━━━━━━✠╯"
    )
