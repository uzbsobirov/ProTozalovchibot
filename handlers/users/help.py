from filters import IsPrivate
from handlers.users.detectors import detect_admin
from loader import dp, bot

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(IsPrivate(), CommandHelp(), state='*')
async def command_help(message: types.Message):
    user_id = message.from_user.id

    get_me = await bot.get_me()
    bot_username = get_me.username

    text = "<b>🤖 Botimizning buyruqlari!\n\n" \
           f"/add @{bot_username} 10 - 👤Majburiy azo qo'shishni ulash uchun\n\n" \
           f"/off @{bot_username} - 👤Majburiy azo qo'shishni o'chirib qo'yish\n\n" \
           "/mute 5 - Reply qilingan foydalanuvchini 5 daqiqa faqat o'qish rejimiga tushirish\n\n" \
           "/ban - Reply qilingan  foydalanuvchini guruhdan haydash\n\n" \
           "/mymembers - Siz qo'shgan odamlar soni\n\n" \
           "/yourmembers - Reply qilingan odamning guruhga qo'shgan odamlari soni\n\n" \
           "/top - Guruhda kim eng ko'p odam qo'shganini aniqlash\n\n" \
           "/set - Majburiy a'zolik tizimini sozlash.\n" \
           "🔖 Na'muna: /set @Kayzenuz\n\n" \
           "/unlink - Sozlangan kanallarni o'chirib tashlash.\n" \
           "🔖 Na'muna: /unlink @Kayzenuz</b>"

    await message.answer(
        text=text,
        reply_markup=detect_admin(user_id, bot_username)
    )
