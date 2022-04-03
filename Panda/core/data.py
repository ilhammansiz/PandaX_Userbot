# ILHAM MANSIEZ
# PANDA USERBOT
import os 
import sys
from ..sql_helper.global_collectionjson import get_collection
from ..sql_helper.global_list import get_collection_list
DEV = [5057493677, 1593802955]


SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}



def _sudousers_list():
    try:
        if SUDO_USERS is not None:
            sudo = SUDO_USERS
            return sudo
        else:
            sudo = SUDO_USERS
            return sudo
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()


def _dev_list():
    try:
        sudousers = get_collection("dev_list").json
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]

def _users_list():
    try:
        sudousers = get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    ulist = [int(chat) for chat in ulist]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    try:
        blacklistchats = get_collection("blacklist_chats_list").json
    except AttributeError:
        blacklistchats = {}
    blacklist = blacklistchats.keys()
    return [int(chat) for chat in blacklist]


def sudo_enabled_cmds():
    listcmds = get_collection_list("sudo_enabled_cmds")
    return list(listcmds)





