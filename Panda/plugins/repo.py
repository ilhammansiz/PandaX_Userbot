from . import edit_or_reply, pandaub

plugin_category = "plugins"


@pandaub.ilhammansiz_cmd(
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
        "**╭━━━━━━━━━━━╮**\n\n [Repository](https://github.com/AftahBagas/new_userbot\n**╰━━━━━━━━━━━╯**\n **• Creator** [Creator Repo](https://t.me/robotrakitangakbagus)\n **• Editor** [Editor Repo](https://t.me/kanjengingsun)",
    )
