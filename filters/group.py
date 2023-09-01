from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# This class for bot where is work in the group
class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.SUPERGROUP,
            types.ChatType.GROUP
        )
