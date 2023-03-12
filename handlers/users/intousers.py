from loader import db, dp, bot
from states.admin import SendingUser
from keyboards.inline.adv import types_private

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="intousers", state='*')
async def into_groupss(call: types.CallbackQuery, state: FSMContext):
    await SendingUser.user.set()

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_private)