
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from . import edit_delete, edit_or_reply, ilhammansiz_cmd, HEROKU_APP_NAME, HEROKU_API_KEY, Config
from ..core.data import _sudousers_list
from .. import SqL
Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = _sudousers_list()


@ilhammansiz_cmd(
    pattern="sudo$",
    command=("sudo", plugin_category),
    info={
        "header": "To enable sudo of your Catuserbot.",
        "description": "Initially all sudo commands are disabled, you need to enable ",
        "usage": "{tr}sudo",
    },
)
async def sudo(event):
    sudo = "True" if SUDO_USERS else "False"
    users = sudousers
    listsudo = users.replace(" ", "\n» ")
    if sudo == "True":
        await edit_or_reply(
            event,
            f"🔮 **Sudo:** `Enabled`\n\n📚 ** List Sudo Users:**\n» {listsudo}\n\n**SUDO_COMMAND_HAND_LER:** `{Config.SUDO_COMMAND_HAND_LER}`",
        )
    else:
        await edit_delete(event, "🔮 **Sudo:** `Disabled`")


@ilhammansiz_cmd(
    pattern="addsudo(?: |$)(.*)",
    command=("addsudo", plugin_category),
    info={
        "header": "To add user as your sudo.",
        "usage": "{tr}addsudo <username/reply/mention>",
    },
)
async def add(event):
    suu = event.text[9:]
    if f"{cmd}add " in event.text:
        return
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "SUDO_USERS"
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            xxnx,
            "Balas ke pengguna atau berikan user id untuk menambahkannya ke daftar pengguna sudo anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            xxnx, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan pengguna sudo**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu:
        target = suu
    elif reply:
        target = await get_user(event)
    suudo = f"{sudousers} {target}"
    newsudo = suudo.replace("{", "")
    newsudo = newsudo.replace("}", "")
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{target}` **ke Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = newsudo
    SqL.setdb(f"{var}", f"{newsudo}")

@ilhammansiz_cmd(
    pattern="delsudo(?: |$)(.*)",
    command=("delsudo", plugin_category),
    info={
        "header": "To remove user from your sudo.",
        "usage": "{tr}delsudo <username/reply/mention>",
    },
)
async def _(event):
    suu = event.text[8:]
    xxx = await edit_or_reply(event, "`Processing...`")
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await edit_delete(
            xxx,
            "Balas ke pengguna atau berikan user id untuk menghapusnya dari daftar pengguna sudo Anda.",
            45,
        )
    if suu and not suu.isnumeric():
        return await edit_delete(
            xxx, "Berikan User ID atau reply ke pesan penggunanya.", 45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus pengguna sudo**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu != "" and suu.isnumeric():
        target = suu
    elif reply:
        target = await get_user(event)
    gett = str(target)
    if gett in sudousers:
        newsudo = sudousers.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{target}` **dari Pengguna Sudo.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "SUDO_USERS"
        heroku_Config[var] = newsudo
    else:
        await edit_delete(
            xxx, "**Pengguna ini tidak ada dalam Daftar Pengguna Sudo anda.**", 45
        )


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    return replied_user.user.id
