import datetime
from aiogram.dispatcher import FSMContext
from aiogram import types

from loader import dp, db
from filters import IsGroup
from utils.misc.subscription import check
from data.config import ADMINS
from keyboards.inline.start import elite_start



@dp.message_handler(IsGroup(), state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name # Full name
    user_id = message.from_user.id # User id
    user_mention = message.from_user.get_mention(name=full_name, as_html=True) # User mention <a href=''></a>
    chat_id = message.chat.id # Group id

    checking = await check(user_id=user_id, chat_id=chat_id) # We must check if user is admin in the group

    if checking is not True:
        for entity in message.entities:
            if entity.type in ['url', 'mention', 'text_link']:
                await message.delete()
                text = f"❗️{user_mention} iltimos reklama tarqatmang!"
                await message.answer(text=text, reply_markup=elite_start)

    # List of arabian letter
    list_of_arab_words = ['ب', 'د', 'أنا', 'ص', 'ح', 'ه', 'ز', 'هي تكون', 'ش', 'ن', 'ز', 'تكون', 'ج', 'س', 'ا'
                                                                                        , 'م', 'ذ', 'ذ', 'ل', 'أ']
    for item in list_of_arab_words:
        if item in message.text:
            await message.delete()
            await message.chat.kick(user_id=user_id)
            break



    list_of_insulting_words = await db.select_all_badwrods()
    msg = message.text
    if user_id != ADMINS[0]:
        for word in list_of_insulting_words:
            if msg in word[1]:
                await message.delete()
                text = f"❗️{user_mention} iltimos xaqoratli so'z ishlatmang"
                await message.answer(text=text, reply_markup=elite_start)
                restriction_time = 5
                until_date = datetime.datetime.now() + datetime.timedelta(minutes=restriction_time)
                await message.chat.restrict(user_id=user_id,
                                               can_send_messages=False, until_date=until_date)


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS, state='*')
async def new_member(message: types.Message, state: FSMContext):
    # If New User join to group, we should delete message of user
    await message.delete()


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER, state='*')
async def banned_member(message: types.Message, state: FSMContext):
    # If New User left to group, we should delete message of user
    await message.delete()

@dp.message_handler(IsGroup(), content_types=types.ContentType.PHOTO, state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name # Full name
    user_mention = message.from_user.get_mention(name=full_name, as_html=True) # User mention <a href=''></a>

    types_of_message = ['url', 'mention', 'text_link']
    entity = message['caption_entities'][0]['type']
    if entity in types_of_message:
        await message.delete()
        text = f"❗️{user_mention} iltimos reklama tarqatmang!"
        await message.answer(text=text, reply_markup=elite_start)