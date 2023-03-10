from loader import dp
from filters import IsPrivate

from aiogram import types

@dp.message_handler(IsPrivate())
async def echoo(message: types.Message):
    print(message.text)