import logging

from loader import dp, bot
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


# This handler ban user from group
@dp.message_handler(IsGroup(), Command('add', '/, !'), state='*')
async def ban_user(message: types.Message, state: FSMContext):
    data = message.text.split(' ')
    if len(data) == 0:
        pass

    else:
        pass