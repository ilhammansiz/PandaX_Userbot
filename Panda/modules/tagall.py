import asyncio
import random
import re

from . import ilhammansiz_cmd

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")
emoji = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🎲 🧩 ♟ 🎯 🎳 🎭💕 💞 💓 💗 💖 ❤️‍🔥 💔 🤎 🤍 🖤 ❤️ 🧡 💛 💚 💙 💜 💘 💝 🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧 🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍨 📞".split(
    " "
)

plugin_category = "modules"

class FlagContainer:
    is_active = False


@ilhammansiz_cmd(
    pattern="mention(?: |$)(.*)",
    command=("mention", plugin_category),
    info={
        "header": "Untuk memention semua anggota grup",
        "usage": [
            "{tr}mention",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    query = event.pattern_match.group(1)
    mentions = f"@all {query}"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100500):
        mentions += f"[\u2063](tg://user?id={x.id} {query})"
    await event.client.send_message(
        chat, mentions, reply_to=event.message.reply_to_msg_id
    )


@ilhammansiz_cmd(
    pattern="emojitag(?: |$)(.*)",
    command=("emojitag", plugin_category),
    info={
        "header": "Untuk Mengetag semua anggota di grup dengan random emoji berbeda.",
        "usage": [
            "{tr}emojitag",
        ],
    },
)
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True
        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()
        tags = list(
            map(
                lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break
            current_pack.append(participant)
            if len(current_pack) == 5:
                tags = list(
                    map(
                        lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                        current_pack,
                    ),
                )
                current_pack = []
                if text:
                    tags.append(text)
                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False


@ilhammansiz_cmd(
    pattern="all(?: |$)(.*)",
    command=("all", plugin_category),
    info={
        "header": "Untuk Mengetag semua anggota di grup",
        "usage": [
            "{tr}all",
        ],
    },
)
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True
        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()
        tags = list(
            map(
                lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        jumlah = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break
            jumlah.append(participant)
            if len(jumlah) == 5:
                tags = list(
                    map(
                        lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                        jumlah,
                    ),
                )
                jumlah = []
                if text:
                    tags.append(text)
                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False

