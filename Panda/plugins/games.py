from . import ilhammansiz_cmd

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="xoagame$",
    command=("xoagame", plugin_category),
    info={
        "header": "Game busuk",
        "usage": "{tr}xoagame",
    },
)
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
