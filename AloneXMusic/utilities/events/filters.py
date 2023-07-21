# Powered By @ALONE_WAS_BOT

from typing import Union, List
from pyrogram import filters
from AloneXMusic.utilities.config import COMMAND_PREFIXES


# ╔══╗╔══╗╔═╦╗╔╦╗╔══╗  ╔═╦═╗╔╦╗╔══╗╔══╗╔═╗
# ║══╣║╔╗║║║║║║╔╝╚║║╝  ║║║║║║║║║══╣╚║║╝║╔╝
# ╠══║║╠╣║║║║║║╚╗╔║║╗  ║║║║║║║║╠══║╔║║╗║╚╗
# ╚══╝╚╝╚╝╚╩═╝╚╩╝╚══╝  ╚╩═╩╝╚═╝╚══╝╚══╝╚═╝

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
