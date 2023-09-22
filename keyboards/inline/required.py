from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def check_user(user_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="✅ Odam qo'shdim", callback_data=f'check_members_{user_id}'
        )
    )

    return markup
