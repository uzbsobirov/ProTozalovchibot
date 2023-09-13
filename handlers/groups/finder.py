import logging

from loader import dp, db, bot
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


@dp.message_handler(IsGroup(), Command('mymembers', prefixes='/'), state='*')
async def get_my_members(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    get_mention = message.from_user.get_mention(name=full_name)
    chat_id = message.chat.id
    try:
        selection = await db.select_one_user_data(user_id=user_id, chat_id=chat_id)
        members = selection[0][2]
        text = f"{get_mention} siz {members} ta odam qo'shgansiz!"
        await message.reply(text)
    except IndexError as ind:
        logging.info(ind)
        text = f"{get_mention} siz xali odam qo'shmagansiz"
        await message.reply(text)


@dp.message_handler(IsGroup(), Command('yourmembers', prefixes='/'), state='*')
async def get_my_members(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    try:
        user_id = message.reply_to_message.from_user.id
        full_name = message.reply_to_message.from_user.full_name
        get_mention = message.from_user.get_mention(name=full_name)
        selection = await db.select_one_user_data(user_id=user_id, chat_id=chat_id)
        members = selection[0][2]
        text = f"{get_mention} {members} ta odam qo'shgansiz!"
        await message.answer(text)

    except IndexError as ind:
        logging.info(ind)
        text = f"{get_mention} xali odam qo'shmagan"
        await message.answer(text)

    except AttributeError as attr:
        logging.info(attr)
        await message.answer(
            text="<b>Bu kamanda bitta foydalanuvchiga reply qilgan xolda ishlatishingiz lozim❗️</b>"
        )