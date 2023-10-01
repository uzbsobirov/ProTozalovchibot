from filters import IsAdmin
from filters.group import IsGroup
from keyboards.inline.start import add_to_group
from loader import dp, bot

from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.misc.subscription import check


@dp.message_handler(IsGroup(), IsAdmin(), state='*')
async def delete_ads(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    get_mention = message.from_user.get_mention(full_name)
    is_bot = message['from']['is_bot']
    chat_id = message.chat.id
    get_bot = await bot.get_me()
    bot_username = get_bot.username

    is_admin = await check(user_id=user_id, chat_id=chat_id)

    # Guruhda reklama yuborgan odamning xabarini o'chirish uchun
    text = f"❗️{get_mention} iltimos reklama tarqatmang!"

    entities = ['mention', 'text_link', 'url']
    if is_bot is False:
        if message.entities:
            for entity in message.entities:
                if entity.type in entities:
                    await message.delete()
                    await message.answer(text=text, reply_markup=add_to_group(bot_username))

    # > > >





