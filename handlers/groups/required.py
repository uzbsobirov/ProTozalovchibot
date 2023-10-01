import logging

from asyncpg import UniqueViolationError

from filters import IsAdmin
from keyboards.inline.required import check_user
from keyboards.inline.start import add_to_group
from loader import dp, bot, db
from filters.group import IsGroup, InData
from keyboards.inline.instruction import instruction

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


# This handler to force users add members
@dp.message_handler(IsGroup(), InData(), IsAdmin(), Command('add', '/, !'), state='*')
async def ban_user(message: types.Message, state: FSMContext):
    data = message.text.split(' ')
    if len(data) == 1:
        text = "/add son - majburiy odam qo'shish funksiyasi" \
               "\nNamuna: /add 10" \
               "\n/unadd - majburiy odam qo'shishni o'chirish"
        await message.answer(text=text)

    else:
        method = data[0]
        amount = data[1]
        if amount.isdigit():
            chat_id = message.chat.id
            get_me = await bot.get_chat(chat_id)
            chat_link = get_me.invite_link
            group_name = get_me.full_name
            try:
                await db.add_group_required(
                    chat_id=chat_id,
                    chat_link=chat_link,
                    method=method,
                    amount=int(amount)
                )

                text = f"<b>{group_name}</b> guruhida majburiy odam qo'shish tizimi ishga tushdi" \
                       f"\n\nEndi guruhga yozishingiz uchun <code>{amount}</code> ta odam qo'shishingiz shart❗️"
                await message.answer(
                    text=text,
                    reply_markup=instruction
                )

            except UniqueViolationError as unique:
                logging.info(unique)
                text = f"<b>{group_name}</b> guruhida majburiy odam qo'shish tizimi ishga tushdi" \
                       f"\n\nEndi guruhga yozishingiz uchun <code>{amount}</code> ta odam qo'shishingiz shart❗️"
                await message.answer(
                    text=text,
                    reply_markup=instruction
                )
                await db.update_required_members(
                    amount=int(amount),
                    chat_id=chat_id
                )
        else:
            await message.answer(
                text="<b>❌ Xato urinish</b>\nNamuna: /add 10" \
                     "\n/unadd - majburiy odam qo'shishni o'chirish"
            )


# release users from add members
@dp.message_handler(IsGroup(), InData(), IsAdmin(), Command('off', '/, !'), state='*')
async def ban_user(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    get_bot = await bot.get_me()
    bot_username = get_bot.username
    await db.delete_required_group(chat_id=chat_id)

    text = "<b>Majburiy a'zo qo'shish o'chirildi✅\n\nEndi guruhga odam qo'shish shart emas</b>"
    await message.answer(text, reply_markup=add_to_group(bot_username))


@dp.message_handler(IsGroup(), InData(), IsAdmin(), content_types=types.ContentType.ANY, state='*')
async def is_added(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    user_mention = message.from_user.get_mention(full_name)

    try:
        select_user = await db.select_one_user(user_id=user_id)
        amount_members = select_user[0][2]

        select_group = await db.select_one_group(chat_id=chat_id)
        amount = select_group[0][4]

        if amount > amount_members:
            await message.delete()
            text = f"{user_mention} - Guruhda yozish uchun {amount} ta odam qo'shishingiz kerak" \
                   f"\n\n👉 /off odam qo'shishni o'chirish"
            await message.answer(text, reply_markup=check_user(user_id))

    except IndexError as index:
        logging.info(index)
        select_group = await db.select_one_group(chat_id=chat_id)
        amount = select_group[0][4]
        print(select_group)
        await message.delete()
        text = f"{user_mention} - Guruhda yozish uchun {amount} ta odam qo'shishingiz kerak" \
               f"\n\n👉 /off odam qo'shishni o'chirish"
        await message.answer(text, reply_markup=check_user(user_id))


@dp.callback_query_handler(text_contains='check_members_', state='*')
async def check_user_amount(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    splited = data.split('_')
    user_id = splited[2]
    chat_id = call.message.chat.id
    try:
        select_user = await db.select_one_user(user_id=int(user_id))
        amount_members = select_user[0][2]

        select_group = await db.select_one_group(chat_id=chat_id)
        amount = select_group[0][4]

        left = amount - amount_members
        if amount > amount_members:
            text = f"Siz guruhga {amount_members} ta odam qo'shgansiz. " \
                   f"Guruhda yozish uchun yana {left} ta odam qo'shishingiz zarur❗️"
            await call.answer(text, show_alert=True)

    except IndexError as index:
        logging.info(index)

        select_group = await db.select_one_group(chat_id=chat_id)
        amount = select_group[0][4]

        text = f"Siz xali guruhga odam qo'shmagansiz. " \
               f"Guruhda yozish uchun {amount} ta odam qo'shishingiz zarur❗️"
        await call.answer(text, show_alert=True)