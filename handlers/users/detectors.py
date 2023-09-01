from data.config import ADMINS
from keyboards.inline.start import start_admin, start_user


def detect_admin(user_id, bot_username):
    for admin in ADMINS:
        if int(admin) == int(user_id):
            return start_admin(bot_username)

    return start_user(bot_username)


async def start_message(bot, admin_list, text):
    for admin in admin_list:
        await bot.send_message(
            chat_id=admin,
            text=text
        )