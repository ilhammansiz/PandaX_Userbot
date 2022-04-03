import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

from Panda import pandaub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event, ilhammansiz_cmd

plugin_category = "plugins"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@ilhammansiz_cmd(
    pattern="gban(?: |$)(.*)",
    command=("gban", plugin_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def pandagban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    pandae = await edit_or_reply(event, "`gbanning.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, pandae)
    if not user:
        return
    if user.id == pandaub.uid:
        return await edit_delete(pandae, "`why would I ban myself`")
    if gban_sql.is_gbanned(user.id):
        await pandae.edit(
            f"`the `[user](tg://user?id={user.id})` is already in gbanned list any way checking again`"
        )
    else:
        gban_sql.pandagban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(pandae, "`you are not admin of atleast one group` ")
    await pandae.edit(
        f"`Sedang menghabisi pengguna meresahkan `[user](tg://user?id={user.id}) `Dari {len(san)} groups grup didunia`"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {event.chat.title}(`{event.chat_id}`)\n`For banning here`",
            )
    end = datetime.now()
    pandataken = (end - start).seconds
    if reason:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {pandataken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {count} groups in {pandataken} seconds`!!"
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Banned in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Banned in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@ilhammansiz_cmd(
    pattern="ungban(?: |$)(.*)",
    command=("ungban", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "description": "will unban and also remove from your gbanned list.",
        "usage": "{tr}ungban <username/reply/userid>",
    },
)
async def pandagban(event):
    "To unban the person from every group where you are admin."
    pandae = await edit_or_reply(event, "`ungbanning.....`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, pandae)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.pandaungban(user.id)
    else:
        return await edit_delete(
            pandae, f"the [user](tg://user?id={user.id}) `is not in your gbanned list`"
        )
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`you are not even admin of atleast one group `")
    await pandae.edit(
        f"initiating ungban of the [user](tg://user?id={user.id}) in `{len(san)}` groups"
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat : **{event.chat.title}(`{event.chat_id}`)\n`For unbaning here`",
            )
    end = datetime.now()
    pandataken = (end - start).seconds
    if reason:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}`) was ungbanned in {count} groups in {pandataken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was ungbanned in {count} groups in {pandataken} seconds`!!"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Unbanned in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )


@ilhammansiz_cmd(
    pattern="listgban$",
    command=("listgban", plugin_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "usage": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "Current Gbanned Users\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) Reason None\n"
                )
    else:
        GBANNED_LIST = "no Gbanned Users (yet)"
    await edit_or_reply(event, GBANNED_LIST)


@ilhammansiz_cmd(
    pattern="gmute(?: |$)(.*)",
    command=("gmute", plugin_category),
    info={
        "header": "To mute a person in all groups where you are admin.",
        "description": "It doesnt change user permissions but will delete all messages sent by him in the groups where you are admin including in private messages.",
        "usage": "{tr}gmute username/reply> <reason (optional)>",
    },
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == pandaub.uid:
            return await edit_or_reply(event, "`Sorry, I can't gmute myself`")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} ` is already gmuted`",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n`{str(e)}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`\n**Reason :** `{reason}`",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully gmuted`",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#GMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@ilhammansiz_cmd(
    pattern="ungmute(?: |$)(.*)",
    command=("ungmute", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("`Unexpected issues or ugly errors may occur!`")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == pandaub.uid:
            return await edit_or_reply(event, "`Sorry, I can't gmute myself`")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")

    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"{_format.mentionuser(user.first_name ,user.id)} `is not gmuted`"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**Error**\n`{str(e)}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`\n**Reason :** `{reason}`",
            )
        else:
            await edit_or_reply(
                event,
                f"{_format.mentionuser(user.first_name ,user.id)} `is Successfully ungmuted`",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**Reason :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#UNGMUTE\n"
                f"**User :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@ilhammansiz_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


@ilhammansiz_cmd(
    pattern="gkick(?: |$)(.*)",
    command=("gkick", plugin_category),
    info={
        "header": "kicks the person in all groups where you are admin.",
        "usage": "{tr}gkick <username/reply/userid> <reason (optional)>",
    },
)
async def pandagkick(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin"
    pandae = await edit_or_reply(event, "`gkicking.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == pandaub.uid:
        return await edit_delete(cate, "`why would I kick myself`")
    san = []
    san = await admin_groups(event)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`you are not admin of atleast one group` ")
    await pandae.edit(
        f"`initiating gkick of the `[user](tg://user?id={user.id}) `in {len(san)} groups`"
    )
    for i in range(sandy):
        try:
            await event.client.kick_participant(san[i], user.id)
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {event.chat.title}(`{event.chat_id}`)\n`For kicking there`",
            )
    end = datetime.now()
    pandataken = (end - start).seconds
    if reason:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {pandataken} seconds`!!\n**Reason :** `{reason}`"
        )
    else:
        await pandae.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {count} groups in {pandataken} seconds`!!"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Reason :** `{reason}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GKICK\
                \nGlobal Kick\
                \n**User : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Kicked in {count} groups__\
                \n**Time taken : **`{pandataken} seconds`",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)
