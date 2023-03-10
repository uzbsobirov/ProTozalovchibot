from aiogram.dispatcher import FSMContext

from loader import dp, bot
from filters import IsGroup

from aiogram import types

@dp.message_handler(IsGroup(), state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name # Full name
    user_mention = message.from_user.get_mention(name=full_name, as_html=True) # User mention <a href=''></a>


    for entity in message.entities:
        if entity.type in ['url', 'mention', 'text_link']:
            await message.delete()
            text = f"❗️{user_mention} iltimos reklama tarqatmang!"
            await message.answer(text=text)

    # List of arabian letter
    lst = ['ب', 'د', 'أنا', 'ه', 'ز', 'هي تكون', 'ش', 'ن', 'ز', 'تكون', 'ج', 'س', 'ا', 'م', 'ذ', 'ذ', 'ل', 'أ']
    for item in lst:
        if item in message.text:
            await message.delete()
            break


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
        await message.answer(text=text)