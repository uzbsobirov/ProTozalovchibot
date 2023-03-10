from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

# This class for bot where is work in the private
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE