from loader import dp
from filters import IsGroup
from keyboards.inline.start import start

from aiogram import types
from aiogram.dispatcher import FSMContext
@dp.message_handler(IsGroup(), commands=['start'], state='*')
async def start_group(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)

    text = "<b>👮🏻‍♂GURUH - da sizga yordam beraman 👇\n\n🖇 - Reklama havolalarini tozalayman\n" \
           "🚫 - Spam xabarlarni tozalayman\n🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - " \
           "Arab botlardan ximoya qilaman\n🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman" \
           "\n🔞 - So‘kinganlarni 5 minut faqat o'qish rejimiga tushuraman\n\n❗️Men to‘liq ishlashim uchun ADMIN " \
           "qilib tayinlashingiz kerak</b>"

    await message.answer(text=text, reply_markup=start)
    await state.finish()
