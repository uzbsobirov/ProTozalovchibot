from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_private = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url='https://t.me/ProTozalovchibot?startgroup=new'
            )
        ],
        [
            InlineKeyboardButton(
                text="⌨️ Admin panel", callback_data='panel_of_admin'
            )
        ]
    ]
)

group_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url='https://t.me/ProTozalovchibot?startgroup=new'
            )
        ]
    ]
)