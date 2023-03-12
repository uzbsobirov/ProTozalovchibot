from loader import dp
from states.admin import Admin
from keyboards.inline.start import gold_start, elite_start
from data.config import admin_ids
from keyboards.inline.admin import admin

from aiogram import types
from aiogram.dispatcher import FSMContext


# Bu handler Admin paneldan Asosiy menuga chiqish uchun
@dp.callback_query_handler(text="back_to_menu", state=Admin.main_admin)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>👮🏻‍♂GURUH - da sizga yordam beraman 👇\n\n🖇 - Reklama havolalarini tozalayman\n" \
           "🚫 - Spam xabarlarni tozalayman\n🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - " \
           "Arab botlardan ximoya qilaman\n🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman" \
           "\n🔞 - So‘kinganlarni 5 minut faqat o'qish rejimiga tushuraman\n\n❗️Men to‘liq ishlashim uchun ADMIN " \
           "qilib tayinlashingiz kerak</b>"

    if user_id == int(admin_ids()):
        await call.message.edit_text(text=text, reply_markup=gold_start)
    else:
        await call.message.edit_text(text=text, reply_markup=elite_start)

    await state.finish()

# Bu handler Statistika bolimidan Admin panel menuga qaytish uchun
@dp.callback_query_handler(text="stat_back", state=Admin.stat)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()