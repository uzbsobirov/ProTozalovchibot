from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

type_sending = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Guruhlarga", callback_data='intogroups'),
            InlineKeyboardButton(text="👤 Userlarga", callback_data='intousers')
        ]
    ]
)


types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖼 Surat", callback_data='withpicture'),
            InlineKeyboardButton(text="📹 Video", callback_data='withvideo')
        ],
        [
            InlineKeyboardButton(text="📝 Text", callback_data='withtext')
        ],
        [
            InlineKeyboardButton(text="◀️ Orqaga", callback_data='stat_back')
        ]
    ]
)