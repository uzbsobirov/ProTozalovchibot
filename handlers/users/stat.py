from loader import dp, db
from keyboards.inline.backs import back_stat
from utils.misc.group import check
from states.admin import Admin

from aiogram import types
from aiogram.dispatcher import FSMContext

from datetime import datetime, date

# This handler for statics of bot
@dp.callback_query_handler(text="stat", state='*')
async def static(call: types.CallbackQuery, state: FSMContext):
    await Admin.stat.set()
    todays_date = date.today() # Todays date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    count = await db.count_users() # All users
    all_groups = await db.select_all_group() # Len of all groups

    all_users = 0
    for chat_id in all_groups:
        checking = await check(chat_id=chat_id[1])
        all_users += checking

    text = f"<b>📆 Bugunki sana: {todays_date}\n🕰 Hozirgi vaqt: {current_time}\n\n" \
    f"📊 Bot obunachilari: {count}\n👥 Guruhlar soni: {len(all_groups)}\n🫂 Guruh obunachilar: {all_users}" \
    f"\n👤Barcha obunachilar: {all_users+count}\n\n⚡️@ProTozalovchibot</b>"
    await call.message.edit_text(text=text, reply_markup=back_stat)
