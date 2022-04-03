# Copyright (C) 2021 TeamUltroid <https://github.com/TeamUltroid/Ultroid>
# Recode by @diemmmmmmmmmm
# FROM Panda-Userbot <https://github.com/ilhammansiz/PandaX_Userbot>

# Version sql
#Panda Userbot
# Yang Ngapus anak anjeng capek lah aku port nya :(




from . import *
from pytgcalls.exceptions import NotConnectedError
from requests.exceptions import MissingSchema
from telethon import events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

import requests

def mansiez(**args):
    """ Registers a new message. """
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        vcClient.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator

plugin_category = "music"



@ilhammansiz_cmd(
    command=("play", plugin_category),
    info={
        "header": "Play the song in voice chat.",
        "description": "Play the song in voice chat, or add the song to queue..",
        "usage": "{tr}play <song name/link>",
        "examples": ["{tr}play pujaan hati"],
    },
)
@PandaVc_cmd("play")
async def play_music_(event):
    if "playfrom" in event.text.split()[0]:
        return  # For PlayFrom Conflict
    xx = await eor(event, get_string("com_1"), parse_mode="md")
    chat = event.chat_id
    from_user = html_mention(event)
    reply, song = None, None
    if event.reply_to:
        reply = await event.get_reply_message()
    if len(event.text.split()) > 1:
        input = event.text.split(maxsplit=1)[1]
        tiny_input = input.split()[0]
        if tiny_input.startswith("@"):
            try:
                chat = int("-100" + str(await get_user_id(tiny_input, client=vcClient)))
                song = input.split(maxsplit=1)[1]
            except IndexError:
                pass
            except Exception as e:
                return await eor(event, str(e))
        elif tiny_input.startswith("-"):
            chat = int(
                "-100" + str(await get_user_id(int(tiny_input), client=vcClient))
            )
            try:
                song = input.split(maxsplit=1)[1]
            except BaseException:
                pass
        else:
            song = input
    if not (reply or song):
        return await eor(
            xx, "Please specify a song name or reply to a audio file !", time=5
        )
    await eor(xx, get_string('vcbot_20'), parse_mode="md")
    if reply and reply.media and mediainfo(reply.media).startswith(("audio", "video")):
        song, thumb, song_name, link, duration = await file_download(xx, reply)
    else:
        song, thumb, song_name, link, duration = await download(song)
    ultSongs = Player(chat, event)
    song_name = song_name[:30] + "..."
    if not ultSongs.group_call.is_connected:
        if not (await ultSongs.vc_joiner()):
            return
        await ultSongs.group_call.start_audio(song)
        text = "🎧 <strong>Now playing: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👥 <strong>Chat:</strong> <code>{}</code>\n🙋‍♂ <strong>Requested by: {}</strong>".format(
                link, song_name, duration, chat, from_user
        )
        try:
            await xx.reply(
            text,
            file=thumb,
            link_preview=False,
            parse_mode="html",
            )
            await xx.delete()
        except ChatSendMediaForbiddenError:
            await eor(xx, text, link_preview=False)
        if thumb and os.path.exists(thumb):
            os.remove(thumb)
    else:
        if not (
            reply
            and reply.media
            and mediainfo(reply.media).startswith(("audio", "video"))
        ):
            song = None
        add_to_queue(chat, song, song_name, link, thumb, from_user, duration)
        return await eor(
            xx,
            f"▶ Added 🎵 <a href={link}>{song_name}</a> to queue at #{list(VC_QUEUE[chat].keys())[-1]}.",
            parse_mode="html",
        )


@ilhammansiz_cmd(
    command=("playfrom", plugin_category),
    info={
        "header": "Play music from channel files at current chat...",
        "description": "Play music from channel files at current chat....",
        "usage": "{tr}playfrom <channel username> ; <limit>",
        "examples": ["{tr}playfrom <@userbot> ; <100>"],
    },
)
@PandaVc_cmd("playfrom")
async def play_music_(event):
    msg = await eor(event, get_string("com_1"))
    chat = event.chat_id
    limit = 10
    from_user = html_mention(event)
    if not len(event.text.split()) > 1:
        return await msg.edit(
            "Use in Proper Format\n`.playfrom <channel username> ; <limit>`"
        )
    input = event.text.split(maxsplit=1)[1]
    if ";" in input:
        try:
            limit = input.split(";")
            input = limit[0]
            limit = int(limit[1])
        except (IndexError, ValueError):
            pass
    try:
        fromchat = (await event.client.get_entity(input)).id
    except Exception as er:
        return await eor(msg, str(er))
    await eor(msg, "`• Started Playing from Channel....`")
    send_message = True
    ultSongs = Player(chat, event)
    count = 0
    async for song in event.client.iter_messages(
        fromchat, limit=limit, wait_time=5, filter=types.InputMessagesFilterMusic
    ):
        count += 1
        song, thumb, song_name, link, duration = await file_download(
            msg, song, fast_download=False
        )
        song_name = song_name[:30] + "..."
        if not ultSongs.group_call.is_connected:
            if not (await ultSongs.vc_joiner()):
                return
            await ultSongs.group_call.start_audio(song)
            await msg.reply(
                "🎧 <strong>Now playing: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👥 <strong>Chat:</strong> <code>{}</code>\n🙋‍♂ <strong>Requested by: {}</strong>".format(
                    link, song_name, duration, chat, from_user
                ),
                file=thumb,
                link_preview=False,
                parse_mode="html",
            )
            if thumb and os.path.exists(thumb):
                os.remove(thumb)
        else:
            add_to_queue(chat, song, song_name, link, thumb, from_user, duration)
            if send_message and count == 1:
                await eor(
                    msg,
                    f"▶ Added 🎵 <strong><a href={link}>{song_name}</a></strong> to queue at <strong>#{list(VC_QUEUE[chat].keys())[-1]}.</strong>",
                    parse_mode="html",
                )
                send_message = False

@ilhammansiz_cmd(
    command=("joinvc", plugin_category),
    info={
        "header": "Join the voice chat....",
        "description": "Join the voice chat....",
        "usage": "{tr}joinvc",
        "examples": ["{tr}joinvc"],
    },
)
@PandaVc_cmd("joinvc")
async def join_(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat, event)
    if not ultSongs.group_call.is_connected:
        await ultSongs.vc_joiner()


@ilhammansiz_cmd(
    command=("leavevc", plugin_category),
    info={
        "header": "Leave vc the voice chat....",
        "description": "Leave vc the voice chat....",
        "usage": "{tr}leavevc",
        "examples": ["{tr}leavevc"],
    },
)
@PandaVc_cmd("(leavevc|stopvc)")
async def leaver(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.stop()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await eor(event, "` Berhasil Turun voice chat.`")



@ilhammansiz_cmd(
    command=("rejoin", plugin_category),
    info={
        "header": "Re-join the voice chat, incase of errors.",
        "description": "Re-join the voice chat, incase of errors....",
        "usage": "{tr}rejoin",
        "examples": ["{tr}rejoin"],
    },
)
@PandaVc_cmd("rejoin")
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    try:
        await ultSongs.group_call.reconnect()
    except NotConnectedError:
        return await eor(event, "You haven't connected to a voice chat!")
    await eor(event, "`Re-joining this voice chat.`")


@ilhammansiz_cmd(
    command=("queue", plugin_category),
    info={
        "header": "List the songs in queue..",
        "description": "List the songs in queue.....",
        "usage": "{tr}queue",
        "examples": ["{tr}queue"],
    },
)
@PandaVc_cmd("queue")
async def queue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    q = list_queue(chat)
    if not q:
        return await eor(event, "• Nothing in queue!")
    await eor(event, "• <strong>Queue:</strong>\n\n{}".format(q), parse_mode="html")



@ilhammansiz_cmd(
    command=("radio", plugin_category),
    info={
        "header": "Stream Live Radio m3u8 links..",
        "description": "Stream Live Radio m3u8 links.....",
        "usage": "{tr}radio <link>",
        "examples": ["{tr}radio <link>"],
    },
)
@PandaVc_cmd("radio")
async def radio_mirchi(e):
    xx = await eor(e, get_string("com_1"))
    if not len(e.text.split()) > 1:
        return await eor(xx, "Are You Kidding Me?\nWhat to Play?")
    input = e.text.split()
    if input[1].startswith("-"):
        chat = int(input[1])
        song = e.text.split(maxsplit=2)[2]
    elif input[1].startswith("@"):
        cid = (await vcClient.get_entity(input[1])).id
        chat = int(f"-100{cid}")
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    try:
        requests.get(song)
    except BaseException:
        return await eor(xx, f"`{song}`\n\nNot a playable link.🥱")
    ultSongs = Player(chat, e)
    if not ultSongs.group_call.is_connected:
        if not (await ultSongs.vc_joiner()):
            return
    await ultSongs.group_call.start_audio(song)
    await xx.reply(
        f"• Started Radio 📻\n\n• Station : `{song}`",
        file="https://telegra.ph/file/6134eb4bf284402c9a7f6.mp4",
    )
    await xx.delete()

@ilhammansiz_cmd(
    command=("ytlive", plugin_category),
    info={
        "header": "Stream Live YouTube..",
        "description": "Stream Live YouTube.....",
        "usage": "{tr}ytlive <link>",
        "examples": ["{tr}ytlive <link>"],
    },
)
@PandaVc_cmd("(live|ytlive)")
async def live_stream(e):
    xx = await eor(e, get_string("com_1"))
    if not len(e.text.split()) > 1:
        return await eor(xx, "Are You Kidding Me?\nWhat to Play?")
    input = e.text.split()
    if input[1].startswith("-"):
        chat = int(input[1])
        song = e.text.split(maxsplit=2)[2]
    elif input[1].startswith("@"):
        cid_moosa = (await vcClient.get_entity(input[1])).id
        chat = int("-100" + str(cid_moosa))
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    try:
        requests.get(song)
    except BaseException:
        return await eor(xx, f"`{song}`\n\nNot a playable link.🥱")
    is_live_vid = False
    if re.search("youtu", song):
        is_live_vid = (await bash(f'youtube-dl -j "{song}" | jq ".is_live"'))[0]
    if is_live_vid != "true":
        return await eor(xx, f"Only Live Youtube Urls supported!\n{song}")
    file, thumb, title, link, duration = await download(song)
    ultSongs = Player(chat, e)
    if not ultSongs.group_call.is_connected:
        if not (await ultSongs.vc_joiner()):
            return
    from_user = inline_mention(e.sender)
    await xx.reply(
        "🎸 **Now playing:** [{}]({})\n⏰ **Duration:** `{}`\n👥 **Chat:** `{}`\n🙋‍♂ **Requested by:** {}".format(
            title, link, duration, chat, from_user
        ),
        file=thumb,
        link_preview=False,
    )
    await xx.delete()
    await ultSongs.group_call.start_audio(file)

@ilhammansiz_cmd(
    command=("skip", plugin_category),
    info={
        "header": "Skip the current song and play the next in queue, if any...",
        "description": "Skip the current song and play the next in queue, if any......",
        "usage": "{tr}skip",
        "examples": ["{tr}skip"],
    },
)
@PandaVc_cmd("skip")
async def skipper(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat, event)
    await ultSongs.play_from_queue()

@ilhammansiz_cmd(
    command=("mutevc", plugin_category),
    info={
        "header": "Mute playback....",
        "description": "Mute playback.......",
        "usage": "{tr}mutevc",
        "examples": ["{tr}mutevc"],
    },
)
@PandaVc_cmd("mutevc")
async def mute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.set_is_mute(True)
    await eor(event, "`Muted playback in this chat.`")

@ilhammansiz_cmd(
    command=("unmutevc", plugin_category),
    info={
        "header": "Unmute playback....",
        "description": "Unmute playback.......",
        "usage": "{tr}unmutevc",
        "examples": ["{tr}unmutevc"],
    },
)
@PandaVc_cmd("unmutevc")
async def unmute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.set_is_mute(False)
    await eor(event, "`UnMuted playback in this chat.`")

@ilhammansiz_cmd(
    command=("pausevc", plugin_category),
    info={
        "header": "Pause playback....",
        "description": "Pause playback.......",
        "usage": "{tr}pausevc",
        "examples": ["{tr}pausevc"],
    },
)
@PandaVc_cmd("pausevc")
async def pauser(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.set_pause(True)
    await eor(event, "`Paused playback in this chat.`")

@ilhammansiz_cmd(
    command=("resumevc", plugin_category),
    info={
        "header": "Resume playback....",
        "description": "Resume playback.......",
        "usage": "{tr}resumevc",
        "examples": ["{tr}resumevc"],
    },
)
@PandaVc_cmd("resumevc")
async def resumer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    await ultSongs.group_call.set_pause(False)
    await eor(event, "`Resumed playback in this chat.`")

@ilhammansiz_cmd(
    command=("replay", plugin_category),
    info={
        "header": "Re-play the current song from the beginning.....",
        "description": "Re-play the current song from the beginning........",
        "usage": "{tr}replay",
        "examples": ["{tr}replay"],
    },
)
@PandaVc_cmd("replay")
async def replayer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        if not chat.startswith("@"):
            chat = int(chat)
        try:
            chat = int("-100" + str((await vcClient.get_entity(chat)).id))
        except Exception as e:
            return await eor(event, "**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    ultSongs = Player(chat)
    ultSongs.group_call.restart_playout()
    await eor(event, "`Re-playing the current song.`")

@ilhammansiz_cmd(
    command=("videoplay", plugin_category),
    info={
        "header": "Stream Videos in chat. you can use remotely toolike {tr}videoplay @chat <input/reply>.....",
        "description": "Stream Videos in chat. you can use remotely ........",
        "usage": "{tr}videoplay <song name/url/m3u8 links/reply to video>",
        "examples": ["{tr}videoplay pujaan hati"],
    },
)
@PandaVc_cmd("videoplay")
async def video_c(event):
    xx = await eor(event, get_string("com_1"))
    chat = event.chat_id
    from_user = inline_mention(event.sender)
    reply, song = None, None
    if event.reply_to:
        reply = await event.get_reply_message()
    if len(event.text.split()) > 1:
        input = event.text.split(maxsplit=1)[1]
        tiny_input = input.split()[0]
        if tiny_input.startswith("@"):
            try:
                chat = int("-100" + str(await get_user_id(tiny_input, client=vcClient)))
                song = input.split(maxsplit=1)[1]
            except IndexError:
                pass
            except Exception as e:
                return await eor(event, str(e))
        elif tiny_input.startswith("-"):
            chat = int(
                "-100" + str(await get_user_id(int(tiny_input), client=vcClient))
            )
            try:
                song = input.split(maxsplit=1)[1]
            except BaseException:
                pass
        else:
            song = input
    if not (reply or song):
        return await eor(
            xx, "Please specify a song name or reply to a video file !", time=5
        )
    await eor(xx, "`Downloading and converting...`")
    if reply and reply.media and mediainfo(reply.media).startswith("video"):
        song, thumb, title, link, duration = await file_download(xx, reply)
    else:
        try:
            requests.get(song)
            is_link = True
        except MissingSchema:
            is_link = None
        except BaseException:
            is_link = False
        if is_link is False:
            return await eor(xx, f"`{song}`\n\nNot a playable link.🥱")
        if is_link is None:
            song, thumb, title, link, duration = await vid_download(song)
        elif re.search("youtube", song) or re.search("youtu", song):
            song, thumb, title, link, duration = await vid_download(song)
        else:
            song, thumb, title, link, duration = (
                song,
                "https://telegra.ph/file/22bb2349da20c7524e4db.mp4",
                song,
                song,
                "♾",
            )
    ultSongs = Player(chat, xx, True)
    if not (await ultSongs.vc_joiner()):
        return
    await xx.reply(
        "🎸 **Now playing:** [{}]({})\n⏰ **Duration:** `{}`\n👥 **Chat:** `{}`\n🙋‍♂ **Requested by:** {}".format(
            title, link, duration, chat, from_user
        ),
        file=thumb,
        link_preview=False,
    )
    await asyncio.sleep(1)
    await ultSongs.group_call.start_video(song, with_audio=True)
    await xx.delete()

@ilhammansiz_cmd(
    command=("volume", plugin_category),
    info={
        "header": "Put number between 1 to 100....",
        "description": "Put number between 1 to 100.......",
        "usage": "{tr}volume <number>",
        "examples": ["{tr}volume <70>"],
    },
)
@PandaVc_cmd("volume")
async def volume_setter(event):
    if len(event.text.split()) > 1:
        inp = event.text.split()
        if inp[1].startswith("@"):
            chat = inp[1]
            vol = int(inp[2])
            try:
                chat = int("-100" + str((await vcClient.get_entity(chat)).id))
            except Exception as e:
                return await eor(event, "**ERROR:**\n{}".format(str(e)))
        elif inp[1].startswith("-"):
            chat = int(inp[1])
            vol = int(inp[2])
            try:
                chat = int("-100" + str((await vcClient.get_entity(chat)).id))
            except Exception as e:
                return await eor(event, "**ERROR:**\n{}".format(str(e)))
        elif inp[1].isdigit() and len(inp) == 2:
            vol = int(inp[1])
            chat = event.chat_id
    else:
        return await eor(event, "`Please specify a volume from 1 to 200!`")
    ultSongs = Player(chat)
    if vol:
        await ultSongs.group_call.set_my_volume(int(vol))
        if vol > 200:
            vol = 200
        elif vol < 1:
            vol = 1
        return await eor(event, "• Volume Changed to `{}%` •".format(vol))


@ilhammansiz_cmd(
    command=("ytplaylist", plugin_category),
    info={
        "header": "play whole playlist in voice chat...",
        "description": "play whole playlist in voice chat.......",
        "usage": "{tr}ytplaylist <playlist link>",
        "examples": ["{tr}ytplaylist <playlist link>"],
    },
)
@PandaVc_cmd("ytplaylist")
async def live_stream(e):
    xx = await eor(e, get_string("com_1"))
    if not len(e.text.split()) > 1:
        return await eor(xx, "Are You Kidding Me?\nWhat to Play?")
    input = e.text.split()
    if input[1].startswith("-"):
        chat = int(input[1])
        song = e.text.split(maxsplit=2)[2]
    elif input[1].startswith("@"):
        cid_moosa = (await vcClient.get_entity(input[1])).id
        chat = int("-100" + str(cid_moosa))
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    if not (re.search("youtu", song) and re.search("playlist\\?list", song)):
        return await eor(xx, "Give only youtube playlist")
    try:
        requests.get(song)
    except BaseException:
        return await eor(xx, f"`Only Youtube Playlist please.`")
    await xx.edit("`Keep patience... It'll take some time.`")
    file, thumb, title, link, duration = await dl_playlist(chat, html_mention(e), song)
    ultSongs = Player(chat, e)
    if not ultSongs.group_call.is_connected:
        if not (await ultSongs.vc_joiner()):
            return
        from_user = inline_mention(e.sender)
        await xx.reply(
            "🎸 **Now playing:** [{}]({})\n⏰ **Duration:** `{}`\n👥 **Chat:** `{}`\n🙋‍♂ **Requested by:** {}".format(
                title[:30] + "...", link, duration, chat, from_user
            ),
            file=thumb,
            link_preview=False,
        )
        await xx.delete()
        await ultSongs.group_call.start_audio(file)
    else:
        from_user = html_mention(e)
        add_to_queue(chat, file, title, link, thumb, from_user, duration)
        return await eor(
            xx,
            f"▶ Added 🎵 **[{title}]({link})** to queue at #{list(VC_QUEUE[chat].keys())[-1]}.",
        )
