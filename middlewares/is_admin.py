import logging

from loader import db, bot
from keyboards.inline.start import start_user

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from asyncpg.exceptions import UniqueViolationError


class CheckingAdmin(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        text = "<b>BOT -  GURUHGA ADMIN QILINDI ✅</b>\n\n👮<i>🏻‍♂️ Men bu Guruhda ishlashga tayyorman !</i>"

        try:
            if update.my_chat_member.new_chat_member.status:
                is_bot = update.my_chat_member.new_chat_member.user.is_bot
                bot_username = update.my_chat_member.new_chat_member.user.username
                status = update.my_chat_member.new_chat_member.status

                global chat_id

                if status == 'administrator' and is_bot is True:
                    try:
                        chat_id = update.my_chat_member.chat.id
                        await db.add_group(
                            chat_id=chat_id
                        )

                        await bot.send_message(
                            chat_id=chat_id,
                            text=text,
                            reply_markup=start_user(bot_username)
                        )

                    except UniqueViolationError as unique:
                        logging.info(unique)
                        await bot.send_message(
                            chat_id=chat_id,
                            text=text,
                            reply_markup=start_user(bot_username)
                        )

        except AttributeError as attr:
            logging.info(attr)

