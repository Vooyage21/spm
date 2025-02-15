# ds < https://t.me/kastaid >
# Copyright (C) 2023-present kastaid
#
# This file is a part of < https://github.com/kastaid/ds/ >
# Please read the MIT License in
# < https://github.com/kastaid/ds/blob/main/LICENSE/ >.

from pyrogram import filters
from ds.config import Var
from ds.user import UserClient


@UserClient.on_message(filters.me, group=-100)
async def _watcher(_, m):
    if not Var.IS_STARTUP:
        m.stop_propagation()
