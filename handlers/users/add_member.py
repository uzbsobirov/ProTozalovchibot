from loader import dp, db
from data.config import ADMINS

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="add_member", state='*')
async def  add_member_majburiy(call: types.CallbackQuery, state: FSMContext):
    select_members = await db.select_many_member()

    text = f"<b>Hozirgi majburiy odam qo'shish soni, O'zgartirish uchun raqam yuboring</b>\n\n👉🏻 {select_members}"
    await call.message.edit_text(text=text)