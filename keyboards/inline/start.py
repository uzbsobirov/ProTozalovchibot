from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

url = "https://t.me/ProTozalovchibot?startgroup=on&admin=change_info+delete_messages+restrict_members+pin_messages+manage_video_chats+promote_members+invite_users"

gold_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Guruhga Qo'shish", url=url
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
                text="➕ Guruhga Qo'shish", url=url
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
                text="➕ Guruhga Qo'shish", url=url
            )
        ]
    ]
)