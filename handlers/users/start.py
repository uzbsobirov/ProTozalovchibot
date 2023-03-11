from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from data.config import admin_ids
from loader import dp, db, bot
from filters import IsPrivate
from keyboards.inline.start import start_private




@dp.message_handler(IsPrivate(), CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)


    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id
        )

        # About message to ADMIN
        msg = f"{user_mention} [<code>{user_id}</code>] bazaga qo'shildi."
        await bot.send_message(chat_id=admin_ids(), text=msg)

    except:
        await bot.send_message(chat_id=admin_ids(), text=f"{user_mention} [<code>{user_id}</code>] "
                                                         f"bazaga oldin qo'shilgan")

    text = "<b>👮🏻‍♂GURUH - da sizga yordam beraman 👇\n\n🖇 - Reklama havolalarini tozalayman\n" \
           "🚫 - Spam xabarlarni tozalayman\n🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - " \
           "Arab botlardan ximoya qilaman\n🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman" \
           "\n🔞 - So‘kinganlarni 5 minut faqat o'qish rejimiga tushuraman\n\n❗️Men to‘liq ishlashim uchun ADMIN " \
           "qilib tayinlashingiz kerak</b>"

    await message.answer(text=text, reply_markup=start_private)

