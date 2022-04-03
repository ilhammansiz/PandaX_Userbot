from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from Panda import bot
from . import ilhammansiz_cmd
plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="frog(?: |$)(.*)",
    command=("frog", plugin_category),
    info={
        "header": "Mengirim sticker kodok megangtulisan",
        "usage": "{tr}frog <pesan>",
    },
)
async def honkasays(event):
    await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Beri Aku Bebeberapa Teks, Contoh .frog test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit(
            "`Boss! Saya tidak bisa menggunakan hal-hal sebaris di sini...`"
        )
    except ChatSendStickersForbiddenError:
        await event.edit("🐼 Maaf Panda, saya tidak bisa mengirim stiker ke sini !!")
