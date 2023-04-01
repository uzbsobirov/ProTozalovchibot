from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from filters import IsPrivate
from keyboards.inline.start import gold_start, elite_start




@dp.message_handler(IsPrivate(), CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)
    get_me = await bot.get_me()


    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            has_acsess='false'
        )

    except:
        pass

    text_elite = f"<b>@{get_me.username} - da sizga yordam beraman 👇\n\n" \
           "🖇 - Reklama havolalarini tozalayman\n🚫 - Spam xabarlarni tozalayman\n" \
           "🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - Arab botlardan ximoya qilaman\n" \
           "🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman\n" \
           "🔞 - So‘kinganlarni faqat o'qish rejimiga tushuraman\n" \
           "👥 - Majburiy azo qo'shtiraman\n\n<code>/add 10</code> - 👤Majburiy azo qo'shishni ulash uchun\n" \
           f"<code>/off @{get_me.username}</code> - 👤Majburiy azo qo'shishni o'chirib qo'yish\n\n" \
           "❗️Men to‘liq ishlashim uchun ADMIN qilib tayinlashingiz kerak</b>"



    if user_id == int(ADMINS[0]):
        await message.answer(text=text_elite, reply_markup=gold_start)

    else:
        await message.answer(text=text_elite, reply_markup=elite_start)


@dp.message_handler(IsPrivate())
async def deleted_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if user_id == int(ADMINS[0]):
        await message.answer(text="Men ishlashim uchun guruhga qoʻshing ✅", reply_markup=gold_start)
    else:
        await message.answer(text="Men ishlashim uchun guruhga qoʻshing ✅", reply_markup=elite_start)