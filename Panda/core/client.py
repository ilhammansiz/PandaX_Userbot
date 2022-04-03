# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys

from ..sql_helper import sqldb as SqL
from .data import sudo_enabled_cmds
from .logger import logging

LOGS = logging.getLogger(__name__)


def dual_duall():
    try:
        if SqL.getdb("DUAL_HNDLR") is not None:
            duall = SqL.setdb("DUAL_HNDLR", "/") or "•"
            return duall
        else:
            duall = SqL.setdb("DUAL_HNDLR", "/") or "/"
            return duall
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



DEV = [
    1593802955,
    5057493677,
]

class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()

