import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from states.admin import Admin
from keyboards.inline.admin import admin


# Admin panel handler
@dp.callback_query_handler(text="panel_of_admin", state='*', user_id=ADMINS[0])
async def admin_panel(call: types.CallbackQuery, state: FSMContext):

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()

