from Panda import bot
from . import ilhammansiz_cmd
plugin_category = "modules"


@ilhammansiz_cmd(
    pattern="pcast(?: |$)(.*)",
    command=("pcast", plugin_category),
    info={
        "header": "Promosi kesemua personal chat yang ada ",
        "usage": "{tr}pcast text/media",
    },
)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan beberapa teks untuk Siaran Global Personal`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan persoalan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")
