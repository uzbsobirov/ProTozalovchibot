from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

url = 'https://t.me/ProTozalovchibot?startgroup=new'

gold_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url=url
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/kayzenuz')
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
                text="➕ Guruhga Qo'shish", url=url
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/kayzenuz')
        ]
    ]
)

elite_start_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url=url
            )
        ],
        [
            InlineKeyboardButton(text="Boshqa botlar", url='https://t.me/kayzenuz')
        ]
    ]
)