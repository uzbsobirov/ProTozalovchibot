from aiogram.dispatcher import FSMContext

from filters import IsGroup
from loader import dp, bot

from aiogram import types


@dp.message_handler(IsGroup(), commands='help', state='*')
async def command_help(message: types.Message, state: FSMContext):
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    text = "<b>Bu buyruq GURUHda ishlamaydi❗️\n\n" \
           f"Buyruqni ishlatish uchun botga kiring👉: @{bot_username}</b>"

    await bot.send_message(
        chat_id=message.chat.id,
        text=text
    )
    print(text)
