import logging

from loader import dp, db, bot
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


# This handler find my members how much I add
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


# This handler find how much replied user add member to group
@dp.message_handler(IsGroup(), Command('yourmembers', prefixes='/'), state='*')
async def get_my_members(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    try:
        user_id = message.reply_to_message.from_user.id
        full_name = message.reply_to_message.from_user.full_name
        get_mention = message.from_user.get_mention(name=full_name)
        selection = await db.select_one_user_data(user_id=user_id, chat_id=chat_id)
        members = selection[0][2]
        text = f"{get_mention} {members} ta odam qo'shgan!"
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


# This handler detect top users who add more
# @dp.message_handler(IsGroup(), Command('top', prefixes='/'), state='*')
# async def detect_top_add_user(message: types.Message, state: FSMContext):
#     select_all_user_data = await db.select_all_users_data()
#     top_lst = []
#
#     text = "Guruhda eng odam qo'shganlar 10taligi 👇"
#     def sort_out(lst):
#         for item in select_all_user_data:
#             user_id = item[1]
#             add_members = item[2]
#             chat_id = item[3]
#             # top_lst.append(
#             #     {
#             #         'user_id': user_id,
#             #         'add_members': add_members,
#             #         'chat_id': chat_id
#             #     }
#             #
#             # )
#             return lst['add_memebrs']
#     print(sort_out(select_all_user_data))
#     # print(top_lst.sort(key=sort_out))