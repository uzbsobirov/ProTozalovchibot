import logging

from aiogram.utils.exceptions import NotFound
from asyncpg import UniqueViolationError

from filters.group import IsGroup
from keyboards.inline.start import add_to_group
from loader import dp, db, bot

from aiogram import types
from aiogram.dispatcher import FSMContext


# Guruhga yangi qo'shilgan ni o'chirish uchun
@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS, state='*')
async def new_member_join(message: types.Message, state: FSMContext):
    new_chat_members = message.new_chat_members
    user_id = message.from_user.id
    chat_id = message.chat.id
    get_chat_link = await bot.get_chat(chat_id)
    chat_link = get_chat_link.invite_link
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    # Guruhga qo'shildi xabarini o'chirish uchun
    try:
        await message.delete()
    except:
        pass

    try:
        await db.add_user_data(
            user_id=user_id,
            add_members=0,
            chat_id=chat_id,
            chat_link=chat_link
        )

    except UniqueViolationError as unique:
        logging.info(unique)

    for new_member in new_chat_members:
        full_name = new_member.full_name
        new_user_id = new_member.id
        user_mention = f"<a href='tg://user?id={new_user_id}'>{full_name}</a>"
        if bot_username != new_member.username:
            text = f"<b>Guruhga xush kelibsiz {user_mention}</b>"
            await message.answer(
                text=text,
                reply_markup=add_to_group(bot_username)
            )

    selection = await db.select_one_user(user_id=user_id)
    members_count = selection[0][2]
    select_chat_id = selection[0][3]
    if select_chat_id == chat_id:
        new_members_count = members_count + len(new_chat_members)
        await db.update_user_members(user_id=user_id, add_members=new_members_count, chat_link=chat_link)


# Guruhdan chiqib ketgannni o'chirish uchun
@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER, state='*')
async def new_member_join(message: types.Message, state: FSMContext):
    # Guruhdan chiqib ketdi xabarini o'chirish uchun
    try:
        await message.delete()
    except:
        pass
