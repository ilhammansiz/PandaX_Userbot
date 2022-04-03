import asyncio
from time import sleep

from telethon import events

from Panda import PandaBot
from . import register
plugin_category = "modules"


@register(
    pattern="sayang$",
    command=("sayang", plugin_category),
    help={
        "header": "Sayang aku sayang kamu",
        "usage": "{tr}sayang",
    },
)
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("I LOVEE YOUUU 💕")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💗💕")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG KAMU 💝💖💘")
        await e.edit("💝💘💓💗")
        await e.edit("💞💕💗💘")
        await e.edit("💘💞💕💗")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SELAMANYA 💕")
        await e.edit("💘💘💘💘")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("SAYANG")
        await e.edit("KAMU")
        await e.edit("I LOVE YOUUUU")
        await e.edit("MY BABY")
        await e.edit("💕💞💘💝")
        await e.edit("💘💕💞💝")
        await e.edit("GA DITERIMA🥺🥺💞")


@register(
    pattern="dino$",
    command=("dino", plugin_category),
    help={
        "header": "Dikejar dino",
        "usage": "{tr}dino",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIN DINNN.....`")
    sleep(2)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(2)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`🏃  ADUH MATI AKU 😭     🦖`")
    await typew.edit("`🏃 LARI TERUSSSS     🦖`")
    await typew.edit("`🏃   KEPELESET 🧎🧎  🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`HARUS BERJUANG 👍`")
    sleep(1)
    await typew.edit("`🧎🦖`")
    sleep(2)
    await typew.edit("`-NUNGGUIN YA DAH HABIS BATERAINYA☹️-`")


@register(
    pattern="gabut$",
    command=("gabut", plugin_category),
    help={
        "header": "Gabut aku",
        "usage": "{tr}gabut",
    },
)
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
        await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
        await e.edit("`RAMBUUUT WARNAAA WARNII`")
        await e.edit("`BAGAI GULALI`")
        await e.edit("`IMUUUTTTTT LUCUUU`")
        await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
        await e.edit("`GW GABUUTTTT`")
        await e.edit("`EMMMM BACOTNYA`")
        await e.edit("`GABUTTTT WOI GABUT`")
        await e.edit("🙈🙈🙈🙈")
        await e.edit("🙉🙉🙉🙉")
        await e.edit("🙈🙈🙈🙈")
        await e.edit("🙉🙉🙉🙉")
        await e.edit("`CILUUUKKK BAAAAA`")
        await e.edit("🙉🙉🙉🙉")
        sleep(2)
        await e.edit("🐢  TAK PERNAH KUSADARI 🧎")
        sleep(1)
        await e.edit("🐢        AKU SEGILA INI             🚶")
        sleep(2)
        await e.edit("🐢     AKU HIDUP UNTUKMU                🚶")
        sleep(2)
        await e.edit("🐢   AKU MATI TANPAMU                🚶")
        sleep(2)
        await e.edit("🐢        ooooooo           🚶")
        sleep(5)
        await e.edit("🐢                  🚶")
        sleep(5)
        await e.edit("🐢         OOOOOOOOOOO        🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢     bodo        🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢    dahla        🚶")
        await e.edit("🐢     males     🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢  apa kau       🚶")
        await e.edit("🐢   capek   🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶      dorrrrr           🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶          matiiiiiii            🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶              astagfirullah            🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶               matiiiiiii yang dilakukan oleh             🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶             astagfirullah                  🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🚶                                 🐢")
        await e.edit("`AHHH MANTAP`")
        await e.edit("🙉")
        await e.edit("🙈")
        await e.edit("🙉")
        await e.edit("🙈")
        await e.edit("🙉")
        await e.edit("😂")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢      BEGITU BANYAK HAL         🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢       YANG KU ALAMI      🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢     YANG KUTEMUI      🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢   SAAT BERSAMAMU KURASA SESIH    🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢  KURASA PAHIT  🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶  AIR MATA BOT   🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶      INI MENYANDARKANKU AKU ADALAH BOT   🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶           DAHLA                   🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🐢                       🚶")
        await e.edit("🐢                      🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢        🥺        🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢       🥺       🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢     🥺      🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶    🥺       🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("🐢                       🚶")
        await e.edit("🐢           🥺           🚶")
        await e.edit("🐢                     🚶")
        await e.edit("🐢                    🚶")
        await e.edit("🐢                   🚶")
        await e.edit("🐢                  🚶")
        await e.edit("🐢                 🚶")
        await e.edit("🐢                🚶")
        await e.edit("🐢               🚶")
        await e.edit("🐢              🚶")
        await e.edit("🐢             🚶")
        await e.edit("🐢            🚶")
        await e.edit("🐢           🚶")
        await e.edit("🐢          🚶")
        await e.edit("🐢         🚶")
        await e.edit("🐢        🚶")
        await e.edit("🐢       🚶")
        await e.edit("🐢      🚶")
        await e.edit("🐢     🚶")
        await e.edit("🐢    🚶")
        await e.edit("🐢   🚶")
        await e.edit("🐢  🚶")
        await e.edit("🐢 🚶")
        await e.edit("🐢🚶")
        await e.edit("🚶🐢")
        await e.edit("🚶 🐢")
        await e.edit("🚶  🐢")
        await e.edit("🚶   🐢")
        await e.edit("🚶    🐢")
        await e.edit("🚶     🐢")
        await e.edit("🚶      🐢")
        await e.edit("🚶       🐢")
        await e.edit("🚶        🐢")
        await e.edit("🚶         🐢")
        await e.edit("🚶          🐢")
        await e.edit("🚶           🐢")
        await e.edit("🚶            🐢")
        await e.edit("🚶             🐢")
        await e.edit("🚶              🐢")
        await e.edit("🚶               🐢")
        await e.edit("🚶                🐢")
        await e.edit("🚶                 🐢")
        await e.edit("🚶                  🐢")
        await e.edit("🚶                   🐢")
        await e.edit("🚶                    🐢")
        await e.edit("🚶                     🐢")
        await e.edit("🚶                      🐢")
        await e.edit("🚶                       🐢")
        await e.edit("🚶                        🐢")
        await e.edit("🚶                         🐢")
        await e.edit("🚶                          🐢")
        await e.edit("🚶                           🐢")
        await e.edit("🚶                            🐢")
        await e.edit("🚶                             🐢")
        await e.edit("🚶                              🐢")
        await e.edit("🚶                               🐢")
        await e.edit("🚶                                🐢")
        await e.edit("`GABUT`")


@register(
    pattern="terkadang$",
    command=("terkadang", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}terkadang",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@register(
    pattern="mf$",
    command=("mf", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}mf",
    },
)
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@PandaBot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            f"`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You 💞`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(
    pattern="gombal$",
    command=("gombal", plugin_category),
    help={
        "header": "Gombalin",
        "usage": "{tr}gombal",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai, I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💕💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💗💞`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💝💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💟💖`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💘💓`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@register(
    pattern="mantan$",
    command=("mantan", plugin_category),
    help={
        "header": "teringat mantan",
        "usage": "{tr}mantan",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`HAI MANTAN 🙂`")
    sleep(1)
    await typew.edit("`BERUBAH KARENA DIA`")
    sleep(1)
    await typew.edit("`ALASAN BANYAK`")
    sleep(1)
    await typew.edit("`SOK SIBUK`")
    sleep(1)
    await typew.edit("`JAWAB SINGKAT AMAT PAS BELUM PUTUS`")
    sleep(1)
    await typew.edit("`KAU PERGI DENGANNYA`")
    sleep(1)
    await typew.edit("`SUNGGUH TEGA`")
    sleep(1)
    await typew.edit("`AKU LIAT KAU BERDUAAN 🙃`")
    sleep(1)
    await typew.edit("`KAN KEINGET LAGI MASA SAKITNYA `")
    sleep(1)
    await typew.edit("`CUMA MANTAN AJAPUN 😂`")
    sleep(3)
    await typew.edit("`😁`")
    sleep(2)
    await typew.edit("`MANTAN KEKASIH GELAP`")
    sleep(2)
    await typew.edit("`😂`")


# Create by myself @localheart


@register(
    pattern="sedih$",
    command=("sedih", plugin_category),
    help={
        "header": "sedih kaki kali",
        "usage": "{tr}sedih",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`AKU SEDIH LOH `")
    sleep(1)
    await typew.edit("`KAU SEDIH GAK?`")
    sleep(1)
    await typew.edit("`🥺🥺🥺`")
    sleep(1)
    await typew.edit("`🥺🥺`")
    sleep(1)
    await typew.edit("`😭🙃`")
    sleep(1)
    await typew.edit("`😭😭😭😭`")
    sleep(1)
    await typew.edit("`SUNGGUH TEGA`")
    sleep(1)
    await typew.edit("`AKU LIAT KAU BERDUAAN😭`")
    sleep(1)
    await typew.edit("`🙂🙃😭`")
    sleep(1)
    await typew.edit("`🥺😭🥺😭🥺😭🥺`")


# Create by myself @localheart


@register(
    pattern="salam$",
    command=("salam", plugin_category),
    help={
        "header": "salam",
        "usage": "{tr}salam",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bismillah semoga diterima salamnya`")
    sleep(1)
    await typew.edit("`Assalammuallaikum😊😊`")


# Create by myself @localheart


@register(
    pattern="jawab$",
    command=("jawab", plugin_category),
    help={
        "header": "jawab salam",
        "usage": "{tr}jawab",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Eh lupa jawab salam maaf atuh`")
    sleep(1)
    await typew.edit("`Walaikumsalam😊`")


# Create by myself @localheart


@register(
    pattern="pantun$",
    command=("pantun", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}pantun",
    },
)
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        sleep(1)
        await e.edit("I LOVEE YOUUU 💕")
        sleep(2)
        await e.edit("IKAN HIU")
        sleep(2)
        await e.edit("MAKAN ULAR")
        sleep(2)
        await e.edit("EH SALAH APA YA LUPA TADI")
        sleep(2)
        await e.edit("EH GOBLOK")
        sleep(2)
        await e.edit("LU GOBLOK")
        sleep(1)
        await e.edit("BUAT PARA CEWEK ILOVE U😍")
        sleep(2)
        await e.edit("JANGAN PERNAH BILANG ADA YANG MENYAKITIMU")
        sleep(2)
        await e.edit("NANTI ORANG ITU AKAN HILANG")
        sleep(2)
        await e.edit("MAU GA JADI PACARKU")
        sleep(1)
        await e.edit("TETAP DISINI")
        sleep(2)
        await e.edit("TENAMANI AKU")
        sleep(1)
        await e.edit("SEPANJANG HIDUPKUUU")
        sleep(2)
        await e.edit("PERCAYALAH KUAKAN SELINGKUH 💕")
        sleep(1)
        await e.edit("MENDUAKANMU")
        sleep(2)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("KAMU")
        sleep(1)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("YOK GASKANNNN")
        sleep(2)
        await e.edit("I LOVE YOUUUU")
        sleep(1)
        await e.edit("MY BABY")
        sleep(1)
        await e.edit("💕💞💘💝")
        sleep(1)
        await e.edit("💘💕💞💝")
        sleep(1)
        await e.edit("MUACH MUACH😍😁💞")


# Create by myself @localheart


@register(
    pattern="galau$",
    command=("galau", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}galau",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(5)
    await typew.edit("`🎸 JRENG JRENG JRENG `")
    sleep(3)
    await typew.edit("`KUMOHON KAU MENGERTI COBALAH KAU TAMBAHKAN HATI`")
    sleep(2)
    await typew.edit("`🎸 MUNGKIN DISAAT INI CINTA KITA SEDANG DIUJI `")
    sleep(2)
    await typew.edit("`TABAHKANLAH HATIMU OLEH SIKSA ORANG TUAMU `")
    sleep(2)
    await typew.edit("`🎸 KUYAKIN KITA MAMPU BILA KITA SALING MENUNGGU `")
    sleep(2)
    await typew.edit("`KU KAN SELALU SENANG MENUNGGU (WALAU HANYA KEKASIH GELAP MU`")
    sleep(2)
    await typew.edit("`🎸 SAD YA SEBAGAI SIMPANAN `")
    sleep(2)
    await typew.edit("`DAHLA MALES 🙂`")


# Create by myself @localheart


@register(
    pattern="sad$",
    command=("sad", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}sad",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` MARI KITA NANGIS-NANGIS BUAT YANG LAGI PATAH HATI/BROKENHOME `")
    sleep(2)
    await typew.edit("`1`")
    sleep(2)
    await typew.edit("` 2 `")
    sleep(2)
    await typew.edit("` 3 `")
    sleep(2)
    await typew.edit("` 🥺 `")
    sleep(2)
    await typew.edit("`😭`")
    sleep(2)
    await typew.edit("`🥺`")
    sleep(2)
    await typew.edit("`😭`")


# Create by myself @localheart


@register(
    pattern="razia$",
    command=("razia", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}razia",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` 🏍️ `")
    sleep(1)
    await typew.edit("`ADA POLISI`")
    sleep(1)
    await typew.edit("` 🚓 `")
    sleep(1)
    await typew.edit("` WIU WIU`")
    sleep(1)
    await typew.edit("` 🚓 `")
    sleep(2)
    await typew.edit("`🚑`")
    sleep(1)
    await typew.edit("`🚓`")
    sleep(1)
    await typew.edit("`🚥 Yah Ketangkap`")


# Create by myself @localheart


@register(
    pattern="wkwk$",
    command=("wkwk", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}wkwk",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` 😂 `")
    sleep(1)
    await typew.edit("`🤣`")
    sleep(1)
    await typew.edit("` 😁 `")
    sleep(1)
    await typew.edit("` 😅`")
    sleep(1)
    await typew.edit("`😄`")
    sleep(2)
    await typew.edit("`😀`")
    sleep(1)
    await typew.edit("`😆`")
    sleep(1)
    await typew.edit("`😓`")


# Create by myself @localheart


@register(
    pattern="melamar$",
    command=("melamar", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}melamar",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` AKU ADALAH KAMU  `")
    sleep(1)
    await typew.edit("`AKU INGIN MENJADI TEMAN HIDUP UNTUKMU`")
    sleep(2)
    await typew.edit("` MAU GAK KALAU GAK MAU AKU TARIK LAGI KATA NYA `")
    sleep(2)
    await typew.edit("`KALAU MAU MAH TROBOS AJA`")
    sleep(3)
    await typew.edit("`😄`")
    sleep(2)
    await typew.edit("`BISMILAH`")
    sleep(3)
    await typew.edit("`KUCINTAI DIRIMU SEKARANG DENGAN SAH`")
    sleep(1)
    await typew.edit("`DILAN 1990`")


# Create by myself @localheart


@register(
    pattern="buaya$",
    command=("buaya", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}buaya",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`KAMU MAU LIHAT BUAYA `")
    sleep(1)
    await typew.edit("`INISIAL R 🐊`")
    sleep(1)
    await typew.edit("` INISIAL V 🦎 `")
    sleep(1)
    await typew.edit("`INISIAL I 👌`")
    sleep(1)
    await typew.edit("`INISIAL D 🐊🦎`")
    sleep(2)
    await typew.edit("`C 🐊 DARAT`")
    sleep(1)
    await typew.edit("`U🦎 LAUT`")
    sleep(1)
    await typew.edit("`ITULAH BUAYA BUAYA HATI HATI YA 😁`")


# Create by myself @localheart


@register(
    pattern="yang$",
    command=("yang", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}yang",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` Sayang udah makan? `")
    sleep(1)
    await typew.edit("`Apa Kabar mu`")
    sleep(1)
    await typew.edit("` Kuharap  `")
    sleep(1)
    await typew.edit("` kau`")
    sleep(1)
    await typew.edit("`Baik-baik saja`")
    sleep(2)
    await typew.edit("`Aku sayang kamu`")
    sleep(1)
    await typew.edit("`Tapi kamu nya tidak`")
    sleep(1)
    await typew.edit("`Semoga engkau baik baik saja meski tak kumiliki.`")


# Create by myself @localheart


@register(
    pattern="raziamasker$",
    command=("eaziamasker", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}raziamasker",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`ADA SATPOL PP LARI.....`")
    sleep(1)
    await typew.edit("`WOI SATPOL PP MASKER KALIAN !!`")
    sleep(1)
    await typew.edit("`🏃                        🚓`")
    await typew.edit("`🏃                       🚓`")
    await typew.edit("`🏃                      🚓`")
    await typew.edit("`🏃                     🚓`")
    await typew.edit("`🏃   `LARII`          🚓`")
    await typew.edit("`🏃                   🚓`")
    await typew.edit("`🏃                  🚓`")
    await typew.edit("`🏃                 🚓`")
    await typew.edit("`🏃                🚓`")
    await typew.edit("`🏃               🚓`")
    await typew.edit("`🏃              🚓`")
    await typew.edit("`🏃             🚓`")
    await typew.edit("`🏃            🚓`")
    await typew.edit("`🏃           🚓`")
    await typew.edit("`🏃LUMAYAN CAPEK😪   🚓`")
    await typew.edit("`🏃  LANJUT LARI         🚓`")
    await typew.edit("`🏃            🚓`")
    await typew.edit("`🏃             🚓`")
    await typew.edit("`🏃              🚓`")
    await typew.edit("`🏃               🚓`")
    await typew.edit("`🏃     SALTO DULU          🚓`")
    await typew.edit("`🏃                 🚓`")
    await typew.edit("`🏃                  🚓`")
    await typew.edit("`🏃                   🚓`")
    await typew.edit("`🏃                    🚓`")
    await typew.edit("`🏃                     🚓`")
    await typew.edit("`🏃  Huh-Huh           🚓`")
    await typew.edit("`🏃                   🚓`")
    await typew.edit("`🏃                  🚓`")
    await typew.edit("`🏃                 🚓`")
    await typew.edit("`🏃                🚓`")
    await typew.edit("`🏃               🚓`")
    await typew.edit("`🏃              🚓`")
    await typew.edit("`🏃             🚓`")
    await typew.edit("`🏃            🚓`")
    await typew.edit("`🏃           🚓`")
    await typew.edit("`🏃          🚓`")
    await typew.edit("`🏃         🚓`")
    await typew.edit("`CAPE BANGET !!!`")
    sleep(1)
    await typew.edit("`🏃       🚓`")
    await typew.edit("`🏃      🚓`")
    await typew.edit("`🏃     🚓`")
    await typew.edit("`🏃    🚓`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`🧎🚓🚓 KETANGKAP KAUKAN MANA MASKERNYA`")
    sleep(2)
    await typew.edit("`🤦TINGGAL DIRUMAH PAK`")


# Create by myself @localheart


@register(
    pattern="jalan$",
    command=("jalan", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}jalan",
    },
)
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("BOSEN GAK ADA KEGIATAN")
        sleep(1)
        await e.edit("DIRUMAH MULU")
        sleep(1)
        await e.edit("SEKOLAH DILIBURKAN")
        sleep(1)
        await e.edit("TEMEN GADA")
        sleep(1)
        await e.edit("`MENDING JALAN JALAN`")
        sleep(1)
        await e.edit("SAMBIL NGABUBURIT SEMOGA GADA RAZIA YA:)")
        sleep(1)
        await e.edit("...........................🚐")
        await e.edit("..........................🚐.")
        await e.edit("..............🛺.........🚐..")
        await e.edit("..............🛺........🚐...")
        await e.edit("..............🛺.......🚐....")
        await e.edit("..............🛺......🚐.....")
        await e.edit("..............🛺.....🚐......")
        await e.edit("..............🛺....🚐.......")
        await e.edit("..............🛺...🚐........")
        await e.edit("..............🛺.🚐..........")
        await e.edit("..............🛺🚐...........")
        await e.edit("............🚐🛺.............")
        await e.edit("..........🚐...🛺............")
        await e.edit(".........🚐.....🛺...........")
        await e.edit("........🚐.......🛺..........")
        await e.edit(".......🚐..........🛺........")
        await e.edit("......🚐.............🛺......")
        await e.edit(".....🚐...............🛺.....")
        await e.edit("....🚐..................🛺...")
        await e.edit("..🚐.....................🛺..")
        await e.edit(".🚐........................🛺")
        await e.edit("🚐...........................")
        await e.edit("...........................🚐")
        await e.edit("........🏠🏡🏘️............🚐.")
        await e.edit("........🏘️🏡🏠...........🚐..")
        await e.edit("........🏘️🏡🏠..........🚐...")
        await e.edit("........🏘️🏡🏠.........🚐....")
        await e.edit("........🏘️🏘️🏘️........🚐.....")
        await e.edit("........🏡🏠🏡.......🚐......")
        await e.edit("........🏘️🏡🏠......🚐.......")
        await e.edit("........🏘️🏡🏠.....🚐........")
        await e.edit("........🏘️🏡🏠....🚐.........")
        await e.edit("........🏘️🏡🏠...🚐..........")
        await e.edit("........🏘️🏡🏠..🚐...........")
        await e.edit("........🏘️🏡🏠.🚐............")
        await e.edit("........🏘️🏡🏠🚐.............")
        await e.edit("........🏘️🏡🚐🏠.............")
        await e.edit("........🏘️🚐🏡🏠.............")
        await e.edit("........🚐🏠🏡🏘️.............")
        await e.edit(".......🚐.🏠🏡🏡.............")
        await e.edit("......🚐..🏘️🏡🏠.............")
        await e.edit(".....🚐...🏘️🏡🏠.............")
        await e.edit("....🚐....🏘️🏠🏡.............")
        await e.edit("...🚐.....🏠🏡🏘️.............")
        await e.edit("..🚐......🏘️🏡🏠.............")
        await e.edit(".🚐.......🏘️🏡🏠.............")
        await e.edit("🚐........🏠🏡🏘️.............")
        await e.edit("...........................🚐")
        await e.edit("............🕌............🚐.")
        await e.edit("............🕌...........🚐..")
        await e.edit("............🕌..........🚐...")
        await e.edit("............🕌.........🚐....")
        await e.edit("............🕌........🚐.....")
        await e.edit("............🕌.......🚐......")
        await e.edit("............🕌......🚐.......")
        await e.edit("............🕌.....🚐........")
        await e.edit("............🕌....🚐.........")
        await e.edit("............🕌...🚐..........")
        await e.edit("............🕌..🚐...........")
        await e.edit("............🕌.🚐............")
        await e.edit("............🕌🚐.............")
        await e.edit("............🚐🕌.............")
        await e.edit("...........🚐.🕌.............")
        await e.edit("..........🚐..🕌.............")
        await e.edit(".........🚐...🕌.............")
        await e.edit("........🚐....🕌ᴬᴸᴸᴬᴴᵁ ᴬᴷᴮᴬᴿ²ˣ.")
        await e.edit("ᵂᴬᴴ ᴬᴰᶻᴬᴺ🚐....🕌.............")
        await e.edit("ˢᴴᴼᴸᴬᵀ ᴬᴴ🚐....🕌.............")
        await e.edit(".........🚐...🕌............")
        await e.edit("...........🚐.🕌............")
        await e.edit("............🚐🕌............")
        sleep(1)
        await e.edit("CERITANYA LAGI SHOLAT")
        sleep(1)
        await e.edit("KARNA SI DARA MAU MENAMBAH PAHALA")
        sleep(1)
        await e.edit("DIA PUN SHALAT")
        sleep(1)
        await e.edit("KATA SI DARA")
        sleep(1)
        await e.edit("SHOLAT LAH SEBELUM KAU DI SHOLATKAN")
        sleep(1)
        await e.edit("Lagi shalat🚐🕌.............")
        await e.edit("Lagi shalat..........🚐.🕌.............")
        await e.edit("...............🚐..🕌.............")
        await e.edit("..............🚐...🕌.............")
        await e.edit(".............🚐....🕌.............")
        await e.edit("............🚐.....🕌.............")
        await e.edit("...........🚐......🕌.............")
        await e.edit("..........🚐.......🕌.............")
        await e.edit("🏘️.......🚐........🕌.............")
        await e.edit("🏘️......🚐.........🕌.............")
        await e.edit("🏘️.....🚐..........🕌.............")
        await e.edit("🏘️....🚐...........🕌.............")
        await e.edit("🏘️...🚐............🕌.............")
        await e.edit("🏘️..🚐.............🕌.............")
        await e.edit("🏘️.🚐..............🕌.............")
        await e.edit("🏘️🚐...............🕌.............")
        await e.edit("..............................🚐🏘️")
        await e.edit(".............................🚐.🏘️")
        sleep(1)
        await e.edit(
            "...........DIPERJALANAN ADA JUALAN ES CENDOL................🚐..🏘️"
        )
        sleep(1)
        await e.edit(".............BELI ES CENDOL AH ..............🚐...🏘️")
        sleep(1)
        await e.edit("..........................🚐....🏘️")
        await e.edit(".........................🚐.....🏘️")
        await e.edit("........................🚐......🏘️")
        await e.edit(".......................🚐.......🏘️")
        await e.edit(".....................🚐.........🏘️")
        await e.edit("....................🚐..........🏘️")
        await e.edit("...................🚐...........🏘️")
        await e.edit("..................🚐............🏘️")
        await e.edit(".................🚐.............🏘️")
        await e.edit("................🚐..............🏘️")
        await e.edit("...............🚐...............🏘️")
        await e.edit("..............🚐................🏘️")
        await e.edit(".............🚐.................🏘️")
        await e.edit("............🚐..................🏘️")
        await e.edit("...........🚐...................🏘️")
        await e.edit("..........🚐....................🏘️")
        await e.edit(".........🚐.....................🏘️")
        await e.edit("........🚐......................🏘️")
        await e.edit(".......🚐.......................🏘️")
        await e.edit("......🚐........................🏘️")
        await e.edit(".....🚐.........................🏘️")
        await e.edit("....🚐..........................🏘️")
        await e.edit("...🚐...........................🏘️")
        await e.edit("..🚐............................🏘️")
        await e.edit(".🚐.............................🏘️")
        await e.edit("🚐..............................🏘️")
        await e.edit("SEBELUM SAMPAI RUMAH EH MALAH KECELAKAAN")


# Create by myself @localheart


@register(
    pattern="fuck$",
    command=("fuck", plugin_category),
    help={
        "header": "Fun animation try yourself to know more",
        "usage": "{tr}fuck",
    },
)
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await typew.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )
