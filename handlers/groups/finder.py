from loader import dp, db, bot
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


@dp.message_handler(IsGroup(), Command('mymembers', prefixes='/'), state='*')
async def get_my_members(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chat_id = message.chat.id
    print(message)
    selection = await db.select_one_user_data(user_id=user_id, chat_id=chat_id)
    print(selection)