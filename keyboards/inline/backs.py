from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# This btn for static
back_stat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='stat_back')
        ]
    ]
)