from loader import db, dp, bot
from states.admin import SendingGroup
from keyboards.inline.adv import types_group

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="intogroups", state='*')
async def into_groupss(call: types.CallbackQuery, state: FSMContext):
    await SendingGroup.group.set()

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_group)