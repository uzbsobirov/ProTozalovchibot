from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data='stat'),
            InlineKeyboardButton(text="🗞 Xabar yuborish", callback_data='send_message')
        ],
        [
            InlineKeyboardButton(text="👥 Guruhlar", callback_data='groups')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_to_menu')
        ]
    ]
)