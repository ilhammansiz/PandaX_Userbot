# from https://github.com/sandy1709/catuserbot
# Recode by ILHAM MANSIEZ
# PANDA USERBOT
# TENTANG AKU DAN DIA



import re
from collections import defaultdict
from datetime import datetime
from typing import Optional, Union

from telethon import Button, events
from telethon.errors import UserIsBlockedError
from telethon.events import CallbackQuery, StopPropagation
from telethon.utils import get_display_name

from Panda import Config
from Panda import PandaBot 

from Panda.core import check_owner, pool
from Panda.core.logger import logging
from Panda.core.session import tgbot
from Panda.helpers import reply_id
from Panda.helpers.utils import _format
from Panda.sql_helper.bot_blacklists import check_is_black_list
from Panda.sql_helper.bot_pms_sql import (
    add_user_to_db,
    get_user_id,
    get_user_logging,
    get_user_reply,
)
from Panda.sql_helper.bot_starters import add_starter_to_db, get_starter_details
from Panda.sql_helper.globals import delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, bot_cmd
from .botdata import ban_user_from_bot
pandaub = PandaBot

LOGS = logging.getLogger(__name__)

plugin_category = "plugins"
botusername = Config.TG_BOT_USERNAME


class FloodConfig:
    BANNED_USERS = set()
    USERS = defaultdict(list)
    MESSAGES = 3
    SECONDS = 6
    ALERT = defaultdict(dict)
    AUTOBAN = 10


async def check_bot_started_users(user, event):
    if user.id == Config.OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"🐼 {_format.mentionuser(user.first_name , user.id)} Start Me.\
                \n**ID: **`{user.id}`\
                \n**Name: **{get_display_name(user)}"
    else:
        start_date = check.date
        notification = f"🐼 {_format.mentionuser(user.first_name , user.id)} Start Me.\
                \n**ID: **`{user.id}`\
                \n**Name: **{get_display_name(user)}"
    try:
        add_starter_to_db(user.id, get_display_name(user), start_date, user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, notification)


@bot_cmd(
    pattern=f"^/start({botusername})?([\s]+)?$",
    incoming=True,
    func=lambda e: e.is_private,
)
async def bot_start(event):
    chat = await event.get_chat()
    user = await pandaub.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    if chat.id != Config.OWNER_ID:
        start_msg = f"Hey 🙋 {_format.mentionuser(chat.first_name , chat.id)},\
                    \nSaya {_format.mentionuser(user.first_name , user.id)}' Assistant_bot.\
                    \nKamu Bisa Setting saya disini dan Daftar menu perintah Saya sebagai Asistantmu.\
                    \n\nPowered by @PandaUserbot"
        buttons = [
            (
                Button.inline("🌀 INFO 🌀", data="menubot"),
                Button.url(
                    "Deploy",
                    "https://t.me/PandaUserbot/13",
                ),
            )
        ]
    else:
        start_msg = f"Hey 🙋 {_format.mentionuser(chat.first_name , chat.id)},\
                    \nSaya {_format.mentionuser(user.first_name , user.id)}' Assistant_bot.\
                    \nKamu Bisa Setting saya disini dan Daftar menu perintah Saya sebagai Asistantmu.\
                    \n\nPowered by @PandaUserbot"
        buttons = [
            (
                Button.inline("🌀 INFO 🌀", data="menubot"),
                Button.url(
                    "Deploy",
                    "https://t.me/PandaUserbot/13",
                ),
            )
        ]
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Kesalahan**\nTerjadi Kesalahan pada bot saat loading.\
                \n`{str(e)}`",
            )
    else:
        await check_bot_started_users(chat, event)


@bot_cmd(incoming=True, func=lambda e: e.is_private)
async def bot_pms(event):  # sourcery no-metrics
    chat = await event.get_chat()
    if check_is_black_list(chat.id):
        return
    if chat.id != Config.OWNER_ID:
        msg = await event.forward_to(Config.OWNER_ID)
        try:
            add_user_to_db(msg.id, get_display_name(chat), chat.id, event.id, 0, 0)
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**Kesalahan**\nWSaat menyimpan detail pesan di database\n`{str(e)}`",
                )
    else:
        if event.text.startswith("/"):
            return
        reply_to = await reply_id(event)
        if reply_to is None:
            return
        users = get_user_id(reply_to)
        if users is None:
            return
        for usr in users:
            user_id = int(usr.chat_id)
            reply_msg = usr.reply_id
            user_name = usr.first_name
            break
        if user_id is not None:
            try:
                if event.media:
                    msg = await event.client.send_file(
                        user_id, event.media, caption=event.text, reply_to=reply_msg
                    )
                else:
                    msg = await event.client.send_message(
                        user_id, event.text, reply_to=reply_msg
                    )
            except UserIsBlockedError:
                return await event.reply("𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝘄𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿. ❌")
            except Exception as e:
                return await event.reply(f"**Kesalahan:**\n`{str(e)}`")
            try:
                add_user_to_db(
                    reply_to, user_name, user_id, reply_msg, event.id, msg.id
                )
            except Exception as e:
                LOGS.error(str(e))
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"**Kesalahan**\nSaat menyimpan detail pesan di database\n`{str(e)}`",
                    )


@bot_cmd(edited=True)
async def bot_pms_edit(event):  # sourcery no-metrics
    chat = await event.get_chat()
    if check_is_black_list(chat.id):
        return
    if chat.id != Config.OWNER_ID:
        users = get_user_reply(event.id)
        if users is None:
            return
        for user in users:
            if user.chat_id == str(chat.id):
                reply_msg = user.message_id
                break
        if reply_msg:
            await event.client.send_message(
                Config.OWNER_ID,
                f"⬆️ **Pesan ini telah diedit oleh pengguna** {_format.mentionuser(get_display_name(chat) , chat.id)} as :",
                reply_to=reply_msg,
            )
            msg = await event.forward_to(Config.OWNER_ID)
            try:
                add_user_to_db(msg.id, get_display_name(chat), chat.id, event.id, 0, 0)
            except Exception as e:
                LOGS.error(str(e))
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"**Kesalahan**\nSaat menyimpan detail pesan di database\n`{str(e)}`",
                    )
    else:
        reply_to = await reply_id(event)
        if reply_to is not None:
            users = get_user_id(reply_to)
            result_id = 0
            for usr in users:
                if event.id == usr.logger_id:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    result_id = usr.result_id
                    break
            if result_id != 0:
                try:
                    await event.client.edit_message(
                        user_id, result_id, event.text, file=event.media
                    )
                except Exception as e:
                    LOGS.error(str(e))


@tgbot.on(events.MessageDeleted)
async def handler(event):
    for msg_id in event.deleted_ids:
        users_1 = get_user_reply(msg_id)
        users_2 = get_user_logging(msg_id)
        if users_2 is not None:
            result_id = 0
            for usr in users_2:
                if msg_id == usr.logger_id:
                    user_id = int(usr.chat_id)
                    result_id = usr.result_id
                    break
            if result_id != 0:
                try:
                    await event.client.delete_messages(user_id, result_id)
                except Exception as e:
                    LOGS.error(str(e))
        if users_1 is not None:
            for user in users_1:
                if user.chat_id != Config.OWNER_ID:
                    reply_msg = user.message_id
                    break
            try:
                users = get_user_id(reply_msg)
                for usr in users:
                    user_id = int(usr.chat_id)
                    user_name = usr.first_name
                    break
                if check_is_black_list(user_id):
                    return
                if reply_msg:
                    await event.client.send_message(
                        Config.OWNER_ID,
                        f"⬆️ **🐼 Hapus pesan ke pengguna 🐼** {_format.mentionuser(user_name , user_id)}.",
                        reply_to=reply_msg,
                    )
            except Exception as e:
                LOGS.error(str(e))


@bot_cmd(
    pattern=f"^/uinfo$",
    from_users=Config.OWNER_ID,
)
async def bot_start(event):
    reply_to = await reply_id(event)
    if not reply_to:
        return await event.reply("Balas ke pengguna ")
    info_msg = await event.client.send_message(
        event.chat_id,
        "`🔎 Mencari  database saya ...`",
        reply_to=reply_to,
    )
    users = get_user_id(reply_to)
    if users is None:
        return await info_msg.edit(
            "**Kesalahan:** \n`Maaf !, Saya tidak dapat menemukan database anda:(`"
        )
    for usr in users:
        user_id = int(usr.chat_id)
        user_name = usr.first_name
        break
    if user_id is None:
        return await info_msg.edit(
            "**Kesalahan:** \n`Maaf !, Tidak dapat menemukan database :(`"
        )
    uinfo = f"This message was sent by 🐼 {_format.mentionuser(user_name , user_id)}\
            \n**Nama Pengguna:** {user_name}\
            \n**User ID:** `{user_id}`"
    await info_msg.edit(uinfo)


async def send_flood_alert(user_) -> None:
    # sourcery no-metrics
    buttons = [
        (
            Button.inline("🚫  BAN", data=f"bot_pm_ban_{user_.id}"),
            Button.inline(
                "➖ Bot Antiflood [OFF]",
                data="toggle_bot-antiflood_off",
            ),
        )
    ]
    found = False
    if FloodConfig.ALERT and (user_.id in FloodConfig.ALERT.keys()):
        found = True
        try:
            FloodConfig.ALERT[user_.id]["count"] += 1
        except KeyError:
            found = False
            FloodConfig.ALERT[user_.id]["count"] = 1
        except Exception as e:
            if BOTLOG:
                await pandaub.tgbot.send_message(
                    BOTLOG_CHATID,
                    f"**Kesalahan:**\nWhile updating flood count\n`{str(e)}`",
                )
        flood_count = FloodConfig.ALERT[user_.id]["count"]
    else:
        flood_count = FloodConfig.ALERT[user_.id]["count"] = 1

    flood_msg = (
        r"🚷 **#Flood_Warning**"
        "\n\n"
        f"  ID: `{user_.id}`\n"
        f"  Name: {get_display_name(user_)}\n"
        f"  🐼 User: {_format.mentionuser(get_display_name(user_), user_.id)}"
        f"\n\n**Is spamming your bot !** ->  [ Flood rate ({flood_count}) ]\n"
        "__Quick Action__: Ignored from bot for a while."
    )

    if found:
        if flood_count >= FloodConfig.AUTOBAN:
            if user_.id in Config.SUDO_USERS:
                sudo_spam = (
                    f"**Sudo Pengguna** {_format.mentionuser(user_.first_name , user_.id)}:\n  ID: {user_.id}\n\n"
                    "Is Flooding your bot !, Check `.help delsudo` to remove the user from Sudo."
                )
                if BOTLOG:
                    await pandaub.tgbot.send_message(BOTLOG_CHATID, sudo_spam)
            else:
                await ban_user_from_bot(
                    user_,
                    f"Automated Ban for Flooding bot [exceeded flood rate of ({FloodConfig.AUTOBAN})]",
                )
                FloodConfig.USERS[user_.id].clear()
                FloodConfig.ALERT[user_.id].clear()
                FloodConfig.BANNED_USERS.remove(user_.id)
            return
        fa_id = FloodConfig.ALERT[user_.id].get("fa_id")
        if not fa_id:
            return
        try:
            msg_ = await pandaub.tgbot.get_messages(BOTLOG_CHATID, fa_id)
            if msg_.text != flood_msg:
                await msg_.edit(flood_msg, buttons=buttons)
        except Exception as fa_id_err:
            LOGS.debug(fa_id_err)
            return
    else:
        if BOTLOG:
            fa_msg = await pandaub.tgbot.send_message(
                BOTLOG_CHATID,
                flood_msg,
                buttons=buttons,
            )
        try:
            chat = await pandaub.tgbot.get_entity(BOTLOG_CHATID)
            await pandaub.tgbot.send_message(
                Config.OWNER_ID,
                f"🚷  **[Bot Flood Peringatan !](https://t.me/c/{chat.id}/{fa_msg.id})**",
            )
        except UserIsBlockedError:
            if BOTLOG:
                await pandaub.tgbot.send_message(
                    BOTLOG_CHATID, "**Unblock your bot !**"
                )
    if FloodConfig.ALERT[user_.id].get("fa_id") is None and fa_msg:
        FloodConfig.ALERT[user_.id]["fa_id"] = fa_msg.id


@PandaBot.tgbot.on(CallbackQuery(data=re.compile(b"bot_pm_ban_([0-9]+)")))
@check_owner
async def bot_pm_ban_cb(c_q: CallbackQuery):
    user_id = int(c_q.pattern_match.group(1))
    try:
        user = await pandaub.get_entity(user_id)
    except Exception as e:
        await c_q.answer(f"Kesalahan:\n{str(e)}")
    else:
        await c_q.answer(f"Banning PENGGUNA -> {user_id} ...", alert=False)
        await ban_user_from_bot(user, "Spamming Bot")
        await c_q.edit(f"✅ **🐼 BANNED BERHASIL DILAKUKAN 🐼**  User ID: {user_id}")


def time_now() -> Union[float, int]:
    return datetime.timestamp(datetime.now())


@pool.run_in_thread
def is_flood(uid: int) -> Optional[bool]:
    """Checks if a user is flooding"""
    FloodConfig.USERS[uid].append(time_now())
    if (
        len(
            list(
                filter(
                    lambda x: time_now() - int(x) < FloodConfig.SECONDS,
                    FloodConfig.USERS[uid],
                )
            )
        )
        > FloodConfig.MESSAGES
    ):
        FloodConfig.USERS[uid] = list(
            filter(
                lambda x: time_now() - int(x) < FloodConfig.SECONDS,
                FloodConfig.USERS[uid],
            )
        )
        return True


@PandaBot.tgbot.on(CallbackQuery(data=re.compile(b"toggle_bot-antiflood_off$")))
@check_owner
async def settings_toggle(c_q: CallbackQuery):
    if gvarstatus("bot_antif") is None:
        return await c_q.answer(f"Bot Antiflood sudah dinonaktifkan.", alert=False)
    delgvar("bot_antif")
    await c_q.answer(f"Bot Antiflood dibatalkan.", alert=False)
    await c_q.edit("BOT_ANTIFLOOD batal sekarang !")


@bot_cmd(incoming=True, func=lambda e: e.is_private)
@bot_cmd(edited=True, func=lambda e: e.is_private)
async def antif_on_msg(event):
    if gvarstatus("bot_antif") is None:
        return
    chat = await event.get_chat()
    if chat.id == Config.OWNER_ID:
        return
    user_id = chat.id
    if check_is_black_list(user_id):
        raise StopPropagation
    elif await is_flood(user_id):
        await send_flood_alert(chat)
        FloodConfig.BANNED_USERS.add(user_id)
        raise StopPropagation
    elif user_id in FloodConfig.BANNED_USERS:
        FloodConfig.BANNED_USERS.remove(user_id)
