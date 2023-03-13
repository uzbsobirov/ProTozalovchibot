from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bad_words_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="◀️ Orqaga", callback_data='bad_words_back'
                )
        ]
    ]
)