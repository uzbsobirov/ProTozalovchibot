from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_admin(bot_username):
    url = 'https://t.me/{}?startgroup=new'.format(bot_username)

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="➕ Botni guruhga qo'shish", url=url))
    markup.add(InlineKeyboardButton(text="Foydali botlar", url='t.me/kayzenuz'))
    markup.add(InlineKeyboardButton(text="Admin panel", callback_data='admin_panel'))

    return markup


def start_user(bot_username):
    url = 'https://t.me/{}?startgroup=new'.format(bot_username)

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="➕ Botni guruhga qo'shish", url=url))
    markup.add(InlineKeyboardButton(text="Foydali botlar", url='t.me/kayzenuz'))

    return markup


def add_to_group(bot_username):
    url = 'https://t.me/{}?startgroup=new'.format(bot_username)

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(text="➕ Botni guruhga qo'shish", url=url)
    )

    return markup
