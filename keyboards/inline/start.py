from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

gold_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url='https://t.me/protozalovchibot?startgroup=new'
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/ProTozalovchibot?startgroup=new')
        ],
        [
            InlineKeyboardButton(
                text="⌨️ Admin panel", callback_data='panel_of_admin'
            )
        ]
    ]
)

elite_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url='https://t.me/protozalovchibot?startgroup=new'
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/ProTozalovchibot?startgroup=new')
        ]
    ]
)

elite_start_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url='https://t.me/protozalovchibot?startgroup=new'
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/ProTozalovchibot?startgroup=new')
        ]
    ]
)