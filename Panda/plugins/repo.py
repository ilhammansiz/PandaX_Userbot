from . import edit_or_reply, ilhammansiz_cmd

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="repo$",
    command=("repo", plugin_category),
    info={
        "header": "menunjukkan repo",
        "usage": "{tr}repo",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(
        event,
        "**╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [Repositories](https://github.com/ilhammansiz/PandaX_Userbot)\n\n [Creator](t.me/diemmmmmmmmmm)\n\n [Grup Support](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n",
    )
