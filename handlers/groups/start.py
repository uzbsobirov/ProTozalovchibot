from loader import dp, db, bot
from filters import IsGroup
from keyboards.inline.start import elite_start_group, elite_start
from utils.misc.group import check_is_admin
from data.config import ADMINS

from aiogram import types
from aiogram.dispatcher import FSMContext
@dp.message_handler(IsGroup(), commands=['start'], state='*')
async def start_group(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id

    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            has_acsess='false'
        )
    except:
        pass

    chat_id = message.chat.id
    await state.update_data(
        {'chat_id': chat_id}
    )

    try:
        chat_id = message.chat.id
        chat = await bot.get_chat(chat_id)
        invite_link = await chat.export_invite_link()
        await db.add_id_of_group(chat_id=chat_id, link=invite_link)
    except Exception as error:
        chat_id = message.chat.id
        await db.update_group_id(chat_id=chat_id)
        print(f"{error} -- groups/start.py -> 38")


    bot_is = await check_is_admin(chat_id=chat_id)
    bot_checking = bot_is[0]['status']
    print(f"{bot_is} -- bot_is && {bot_checking} -- bot_checking")

    for _ in range(1, 1000):
        if user_id == ADMINS[0]:
            if bot_checking != 'administrator':
                text = "<b>@ProTozalovchibot - da sizga yordam beraman 👇\n\n" \
                       "🖇 - Reklama antimalarial tozalayman\n🚫 - Spam xabarlarni tozalayman\n" \
                       "🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - Arab botlardan ximoya qilaman\n" \
                       "🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman\n" \
                       "🔞 - So‘kinganlarni faqat o'qish rejimiga tushuraman\n" \
                       "👥 - Majburiy azo qo'shtiraman\n\n<code>/add 10</code> - 👤Majburiy azo qo'shishni ulash uchun\n" \
                       "<code>/off @ProTozalovchibot</code> - 👤Majburiy azo qo'shishni o'chirib qo'yish\n\n" \
                       "❗️Men to‘liq midrashim uchun ADMIN qilib tayinlashingiz kerak</b>"
                await message.answer(text=text, reply_markup=elite_start_group)
                break
            else:
                text = "<b>@ProTozalovchibot - da sizga yordam beraman 👇\n\n" \
                       "🖇 - Reklama antimalarial tozalayman\n🚫 - Spam xabarlarni tozalayman\n" \
                       "🇸🇦 - Arabcha xabarlarni o‘chirib beraman\n🤖 - Arab botlardan ximoya qilaman\n" \
                       "🧹 - Arabcha reklamalardan tozalayman\n🗑 - Kirdi-chiqdilarni tozalayman\n" \
                       "🔞 - So‘kinganlarni faqat o'qish rejimiga tushuraman\n" \
                       "👥 - Majburiy azo qo'shtiraman\n\n<code>/add 10</code> - 👤Majburiy azo qo'shishni ulash uchun\n" \
                       "<code>/off @ProTozalovchibot</code> - 👤Majburiy azo qo'shishni o'chirib qo'yish\n\n" \
                       "✅ Bot guruhda oʻz faoliyatini boshladi</b>"
                await message.answer(text=text, reply_markup=elite_start)
                break

    # await state.finish()
