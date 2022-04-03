from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import ilhammansiz_cmd

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="sa$",
    command=("sa", plugin_category),
    info={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}sa",
    },
)
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Mohon Balas Ke Pesan Pengguna Panda.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    await steal.edit(
        "```🐼 Panda Memerintahku Mengambil Informasi Riwayat Pergantian Nama Orang Ini 🐼```"
    )
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```🐼 Panda Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit(
                    "```Saya Tidak Menemukan Informasi Pergantian Nama, Panda Orang Ini Belum Pernah Mengganti Namanya ```"
                )
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Saya Sedang Sakit Panda Maaf`")
