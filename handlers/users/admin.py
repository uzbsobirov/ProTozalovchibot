import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from states.admin import Admin
from keyboards.inline.admin import admin



@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="@BekoDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)

# Admin panel handler
@dp.callback_query_handler(text="panel_of_admin", state='*')
async def admin_panel(call: types.CallbackQuery, state: FSMContext):

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()

