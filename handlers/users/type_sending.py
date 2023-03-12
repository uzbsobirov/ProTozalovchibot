from loader import dp
from states.admin import Admin
from keyboards.inline.adv import type_sending

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="send_message", state='*')
async def send_messsage(call: types.CallbackQuery, state: FSMContext):
    await Admin.sending.set()

    text = "<b>Keraklisini tanlang👇</b>"
    await call.message.edit_text(text=text, reply_markup=type_sending)