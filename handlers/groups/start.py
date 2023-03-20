from loader import dp, db, bot
from filters import IsGroup
from keyboards.inline.start import elite_start_group
from utils.misc.group import check_is_admin

from aiogram import types
from aiogram.dispatcher import FSMContext
@dp.message_handler(IsGroup(), commands=['start'], state='*')
async def start_group(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            has_acsess='false'
        )
    except:
        pass

    chat_id = message.chat.id
    await state.update_data(
        {'chat_id': chat_id}
    )

    try:
        chat_id = message.chat.id
        chat = await bot.get_chat(chat_id)
        invite_link = await chat.export_invite_link()
        await db.add_id_of_group(chat_id=chat_id, link=invite_link)
    except Exception as error:
        chat_id = message.chat.id
        chat = await bot.get_chat(chat_id)
        await db.update_group_id(chat_id=chat_id)
        print(error)


    bot_is = await check_is_admin(chat_id=chat_id)
    bot_checking = bot_is[0]['status']

    for _ in range(1, 1000):
        if bot_checking != 'administrator':
            text = "<b>Bot ishlashi uchun guruhingizga ADMIN qilishingiz kerak ❗️ </b>"
            await message.answer(text=text, reply_markup=elite_start_group)
            break
        else:
            await message.answer(text="Bot guruhda oʻz faoliyatini boshladi ✅")
            break

    # await state.finish()
