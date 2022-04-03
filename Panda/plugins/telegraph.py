import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file


from ..Config import Config
from ..core.managers import edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, ilhammansiz_cmd

plugin_category = "plugins"


telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@ilhammansiz_cmd(
    pattern="(t(ele)?g(raph)?) ?(m|t|media|text)(?: |$)(.*)",
    command=("telegraph", plugin_category),
    info={
        "header": "Membuat telegraph link.",
        "description": "balas ke media untuk tg t balas ke media untuk tg m",
        "options": {
            "m or media": "Balas ke sticker/image/video/gif.",
            "t or text": "Membuat text menjadi link telegraph.",
        },
        "usage": [
            "{tr}tg m",
            "{tr}tg t <title(optional)>",
            "{tr}telegraph media",
            "{tr}telegraph text <title(optional)>",
        ],
    },
)  # sourcery no-metrics
async def _(event):
    "To get telegraph link."
    pandaevent = await edit_or_reply(event, "`processing........`")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"Created New Telegraph account {auth_url} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**",
        )
    optional_title = event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await pandaevent.edit(
            "`Reply to a message to get a permanent telegra.ph link.`",
        )

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()
    if input_str in ["media", "m"]:
        downloaded_file_name = await event.client.download_media(
            r_message, Config.TEMP_DIR
        )
        await pandaevent.edit(f"`Downloaded to {downloaded_file_name}`")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await pandaevent.edit(f"**Error : **\n`{str(exc)}`")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await pandaevent.edit(
                f"**link : **[telegraph](https://telegra.ph{media_urls[0]})\
                    \n**Time Taken : **`{ms} seconds.`",
                link_preview=True,
            )
    elif input_str in ["text", "t"]:
        user_object = await event.client.get_entity(r_message.sender_id)
        title_of_page = user_object.first_name  # + " " + user_object.last_name
        # apparently, all Users do not have last_name field
        if optional_title:
            title_of_page = optional_title
        page_content = r_message.message
        if r_message.media:
            if page_content != "":
                title_of_page = page_content
            downloaded_file_name = await event.client.download_media(
                r_message, Config.TEMP_DIR
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            for m in m_list:
                page_content += m.decode("UTF-8") + "\n"
            os.remove(downloaded_file_name)
        page_content = page_content.replace("\n", "<br>")
        response = telegraph.create_page(title_of_page, html_content=page_content)
        end = datetime.now()
        ms = (end - start).seconds
        panda = f"https://telegra.ph/{response['path']}"
        await pandaevent.edit(
            f"**link : ** [telegraph]({panda})\
                 \n**Time Taken : **`{ms} seconds.`",
            link_preview=True,
        )
