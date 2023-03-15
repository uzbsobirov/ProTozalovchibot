from typing import Union
from aiogram import Bot


async def check(chat_id: Union[str, int]):
    bot = Bot.get_current()
    member = await bot.get_chat_member_count(chat_id=chat_id)
    return member

async def check_is_admin(chat_id: Union[str, int]):
    bot = Bot.get_current()
    member = await bot.get_chat_administrators(chat_id=chat_id)
    return member

