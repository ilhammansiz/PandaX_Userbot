from . import _pandautils, edit_or_reply, ilhammansiz_cmd

plugin_category = "plugins"


@ilhammansiz_cmd(
    pattern="suicide$",
    command=("suicide", plugin_category),
    info={
        "header": "Deletes all the files and folder in the current directory.",
        "usage": "{tr}suicide",
    },
)
async def _(event):
    "To delete all files and folders in Panda"
    cmd = "rm -rf .*"
    await _pandautils.runcmd(cmd)
    OUTPUT = (
        f"**SUICIDE BOMB:**\nSuccesfully deleted all folders and files in Panda server"
    )
    event = await edit_or_reply(event, OUTPUT)


@ilhammansiz_cmd(
    pattern="plugins$",
    command=("plugins", plugin_category),
    info={
        "header": "To list all plugins in Panda.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in Panda"
    cmd = "ls Panda/plugins"
    o = (await _pandautils.runcmd(cmd))[0]
    OUTPUT = f"**[Panda](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    await edit_or_reply(event, OUTPUT)


@ilhammansiz_cmd(
    pattern="env$",
    command=("env", plugin_category),
    info={
        "header": "To list all environment values in Panda.",
        "description": "to show all heroku vars/Config values in your Panda",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in Panda"
    cmd = "env"
    o = (await _pandautils.runcmd(cmd))[0]
    OUTPUT = (
        f"**[Panda](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    )
    await edit_or_reply(event, OUTPUT)
