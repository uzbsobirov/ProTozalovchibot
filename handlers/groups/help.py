from filters import IsGroup
from handlers.users.detectors import detect_admin
from loader import dp, bot

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(IsGroup(), CommandHelp(), state='*')
async def command_help(message: types.Message):
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    text = "<b>Bu buyruq GURUHda ishlamaydi❗️\n\n" \
           f"Buyruqni ishlatish uchun botga kiring👉: @{bot_username}</b>"

    await message.answer(text=text)
