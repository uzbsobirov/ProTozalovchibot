from loader import dp
from filters import IsGroup

from aiogram import types

@dp.message_handler(IsGroup())
async def deleteads(message: types.Message):
    full_name = message.from_user.full_name
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)


    for entity in message.entities:
        if entity.type in ['url', 'mention', 'text_link']:
            await message.delete()
            text = f"❗️{user_mention} iltimos reklama tarqatmang!"
            await message.answer(text=text)
# async def echoo(message: types.Message):
#     full_name = message.from_user.full_name
#     user_mention = message.from_user.get_mention(name=full_name, as_html=True)
#
#     lst = ['.uz', '.com', '@', 'https', 'http', 't.me', '.ru', '.net', '.org', '.kz', '.usa']
#     for item in lst:
#         if item in message.text:
#             await message.delete()
#             text = f"❗️{user_mention} iltimos reklama tarqatmang!"
#             await message.answer(text=text)