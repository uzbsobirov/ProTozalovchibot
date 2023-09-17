import json
import logging

from loader import dp, bot
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command


# This handler ban user from group
@dp.message_handler(IsGroup(), Command('ban', '/, !'), state='*')
async def ban_user(message: types.Message, state: FSMContext):
    data = json.loads(message.as_json())

    chat_id = message.chat.id

    # Pretty-print the JSON
    pretty_json = json.dumps(data, indent=4)

    try:
        reply_user_id = message.reply_to_message.from_user.id
        full_name = message.reply_to_message.from_user.full_name
        user_mention = f"<a href='tg://user?id={reply_user_id}'>{full_name}</a>"
        await bot.kick_chat_member(chat_id, reply_user_id)
        await message.answer(
            text=f"{user_mention} guruhdan xaydaldi⛔️"
        )

    except AttributeError as attr:
        logging.info(attr)
        args = message.get_args()
        user_data = await bot.get_chat(args)
        user_id = user_data.id
        full_name = user_data.full_name
        user_mention = f"<a href='tg://user?id={user_id}'>{full_name}</a>"
        await bot.kick_chat_member(chat_id, user_id)
        await message.answer(
            text=f"{user_mention} guruhdan xaydaldi⛔️"
        )