from . import edit_or_reply, ilhammansiz_cmd

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="p$",
    command=("p", plugin_category),
    info={
        "header": "memberi salam",
        "usage": "{tr}p",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ASSALAMUALAIKUM WR.WB")


@ilhammansiz_cmd(
    pattern="l$",
    command=("l", plugin_category),
    info={
        "header": "menjawab salam",
        "usage": "{tr}l",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "WALAIKUMSALAM WR.WB")
