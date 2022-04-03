from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


from ..core.managers import edit_or_reply
from . import ilhammansiz_cmd
plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="recognize ?(.*)",
    command=("recognize", plugin_category),
    info={
        "header": "To recognize a image",
        "description": "Get information about an image using AWS Rekognition. Find out information including detected labels, faces. text and moderation tags",
        "usage": "{tr}recognize",
    },
)
async def _(event):
    "To recognize a image."
    if not event.reply_to_msg_id:
        return await edit_or_reply(event, "Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_or_reply(event, "reply to media file")
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        return await event.edit("Reply to actual users message.")
    panda = await edit_or_reply(event, "recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await panda.edit("unblock @Rekognition_Bot and try again")
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            msg = response.message.message
            await panda.edit(msg)
        else:
            await panda.edit("sorry, I couldnt find it")
        await event.client.send_read_acknowledge(conv.chat_id)
