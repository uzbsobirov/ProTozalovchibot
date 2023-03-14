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

deleted_bad_word = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                    text="🔞 So'zni o'chirish", callback_data='delete_bad_word'
                )
        ],
        [
            InlineKeyboardButton(
                    text="◀️ Orqaga", callback_data='bad_words_back_back'
                )
        ]
    ]
)