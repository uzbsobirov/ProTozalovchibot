from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from handlers.users.detectors import detect_admin
from loader import dp, db, bot
from filters import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    get_me = await bot.get_me()
    bot_username = get_me.username

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

    text = f"<b>@{bot_username} - orqali sizga yordam beraman 👇\n\n" \
           "🖇 - Reklama havolalarini tozalayman\n" \
           "🚫 - Spam xabarlarni tozalayman\n" \
           "🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n" \
           "🤖 - Arab botlardan ximoya qilaman\n" \
           "🧹 - Arabcha reklamalardan tozalayman\n" \
           "🗑 - Kirdi-chiqdilarni tozalayman\n" \
           "🔞 - So‘kinganlarni faqat o'qish rejimiga tushuraman\n" \
           "👥 - Majburiy azo qo'shtiraman\n" \
           "📣 - Guruhdagi odamlarni kanalga obuna bo'lmagunicha yozdirmayman\n" \
           "📊 - Guruhda kim nechta odam qo'shganini hisoblayman\n\n" \
           f"/help - Qo'shimcha buyruqlarni bilish uchun ☑️\n\n" \
           "❗️Men guruhda to‘liq ishlashim uchun ADMIN qilib tayinlashingiz kerak</b>"

    await message.answer(
        text=text,
        reply_markup=detect_admin(user_id, bot_username=bot_username)
    )
