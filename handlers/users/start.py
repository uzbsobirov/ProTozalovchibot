from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from filters import IsPrivate
from keyboards.inline.start import gold_start, elite_start




@dp.message_handler(IsPrivate(), CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.delete()
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)


    # Add the User to the DB
    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            has_acsess='false'
        )

        # About message to ADMIN
        msg = f"{user_mention} [<code>{user_id}</code>] bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)



    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"{user_mention} [<code>{user_id}</code>] "
                                                     f"bazaga oldin qo'shilgan")




    text_elite = "<b>👮🏻‍♂GURUH - da sizga yordam beraman 👇\n\n🖇 - Reklama havolalarini tozalayman\n" \
           "🚫 - Spam xabarlarni tozalayman\n🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - " \
           "Arab botlardan ximoya qilaman\n🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman" \
           "\n🔞 - So‘kinganlarni 5 minut faqat o'qish rejimiga tushuraman\n\n❗️Men to‘liq ishlashim uchun ADMIN " \
           "qilib tayinlashingiz kerak</b>"

    text_gold = "<b>Admin panelga xush kelibsiz</b>"


    if user_id == int(ADMINS[0]):
        await message.answer(text=text_gold, reply_markup=gold_start)

    else:
        await message.answer(text=text_elite, reply_markup=elite_start)


@dp.message_handler(IsPrivate())
async def deleted_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    await message.delete()
    if user_id == int(ADMINS[0]):
        await message.answer(text="Men ishlashim uchun guruhga qoʻshing ✅", reply_markup=gold_start)
    else:
        await message.answer(text="Men ishlashim uchun guruhga qoʻshing ✅", reply_markup=elite_start)