from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import db


# This class for bot where is work in the group
class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.SUPERGROUP,
            types.ChatType.GROUP
        )


class InData(BoundFilter):
    async def check(self, message: types.Message):
        chat_id = message.chat.id
        select_required = await db.select_required_groups()
        for item in select_required:
            if chat_id == item[1]:
                return True
        return False
