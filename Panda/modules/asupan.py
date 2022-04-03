# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# from pocong userbot

import random
from telethon.tl.types import InputMessagesFilterVideo
plugin_category = "modules"
from . import ilhammansiz_cmd

@ilhammansiz_cmd(
    pattern="asupan(?: |$)(.*)",
    command=("asupan", plugin_category),
    info={
        "header": "Video Asupan buat yg sangeann",
        "usage": [
            "{tr}asupan",
        ],
    },
)
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Asupan_Pocong", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"nih asupan biar ga lemess 🥵",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")
