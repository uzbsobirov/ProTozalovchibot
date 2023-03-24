from loader import dp, db
from states.admin import Admin, SendingGroup, SendingUser
from states.badwords import BadWords, DeleteBadWords
from keyboards.inline.start import gold_start, elite_start
from data.config import ADMINS
from keyboards.inline.admin import admin
from keyboards.inline.adv import type_sending, types_private, types_group
from keyboards.inline.badwords import *
from states.add_member import AddMember

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

    if user_id == int(ADMINS[0]):
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



# Bu handler xabar yuborish bolimidan Admin panel menuga qaytish uchun
@dp.callback_query_handler(text="stat_back", state=Admin.sending)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()




@dp.callback_query_handler(text="stat_back", state=SendingUser.user)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Keraklisini tanlang👇</b>"
    await call.message.edit_text(text=text, reply_markup=type_sending)
    await Admin.sending.set()



@dp.callback_query_handler(text="back_group", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Keraklisini tanlang👇</b>"
    await call.message.edit_text(text=text, reply_markup=type_sending)
    await Admin.sending.set()

@dp.callback_query_handler(text="bad_words_back", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    result = ""
    list_of_bad_words = await db.select_all_badwrods()
    for b_word in list_of_bad_words:
        result += f"{b_word[0]}, "
    text = f"<b>Xaqoratli so'z qo'shish uchun yozing</b>\n\nBazadagi so'zlar: {result}"
    await call.message.edit_text(text=text, reply_markup=deleted_bad_word)
    await BadWords.word.set()

@dp.callback_query_handler(text="bad_words_back_back", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()

@dp.callback_query_handler(text="back_private_adv", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_private)
    await SendingUser.user.set()

@dp.callback_query_handler(text="back_group_adv", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Kerakli reklama turini tanlang</b>"
    await call.message.edit_text(text=text, reply_markup=types_group)
    await SendingGroup.group.set()

@dp.callback_query_handler(text="bad_words_back_loading", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    result = ""
    list_of_bad_words = await db.select_all_badwrods()
    for b_word in list_of_bad_words:
        result += f"{b_word[0]}, "
    text = f"<b>Xaqoratli so'z qo'shish uchun yozing</b>\n\nBazadagi so'zlar: {result}"
    await call.message.edit_text(text=text, reply_markup=deleted_bad_word)
    await DeleteBadWords.word.set()

@dp.callback_query_handler(text="bad_words_back_succes", state='*')
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    result = ""
    list_of_bad_words = await db.select_all_badwrods()
    for b_word in list_of_bad_words:
        result += f"{b_word[0]}, "
    text = f"<b>Xaqoratli so'z qo'shish uchun yozing</b>\n\nBazadagi so'zlar: {result}"
    await call.message.edit_text(text=text, reply_markup=deleted_bad_word)
    await BadWords.word.set()

@dp.callback_query_handler(text="stat_back", state=AddMember.number)
async def back_to_main(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    text = "<b>Admin panelga xush kelibsiz👣</b>"
    await call.message.edit_text(text=text, reply_markup=admin)
    await Admin.main_admin.set()