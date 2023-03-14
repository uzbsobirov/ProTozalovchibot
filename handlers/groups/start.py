from loader import dp, db
from filters import IsGroup
from keyboards.inline.start import elite_start
from utils.misc.group import check_is_admin

from aiogram import types
from aiogram.dispatcher import FSMContext
@dp.message_handler(IsGroup(), commands=['start'], state='*')
async def start_group(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    chat_id = message.chat.id
    try:
        await db.add_id_of_group(chat_id=chat_id)
    except Exception as error:
        print(error)
        pass

    bot_is = await check_is_admin(chat_id=chat_id)
    bot_checking = bot_is[0]['status']

    for _ in range(1, 1000):
        if bot_checking != 'administrator':
            text = "<b>Bot ishlashi uchun guruhingizga ADMIN qilishingiz kerak ❗️ </b>"
            await message.answer(text=text, reply_markup=elite_start)
            break
        else:
            await message.answer(text="Bot guruhda oʻz faoliyatini boshladi ✅")
            break

    await state.finish()
