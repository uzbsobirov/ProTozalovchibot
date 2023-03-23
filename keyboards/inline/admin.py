from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data='stat'),
            InlineKeyboardButton(text="🗞 Xabar yuborish", callback_data='send_message')
        ],
        [
            InlineKeyboardButton(text="🚷 Xoqaratli so'zlar", callback_data='bad_words'),
            InlineKeyboardButton(text="🔫 Majburiy odam qo'shish", callback_data='add_member')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='back_to_menu')
        ]
    ]
)