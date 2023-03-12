import asyncio
from loader import db, dp, bot
from states.adv import Picture
from keyboards.inline.adv import yes_no, buttons

from aiogram import types
from aiogram.dispatcher import FSMContext


# This handler for adv with photo
@dp.callback_query_handler(text="withpictureprivate", state='*')
async def odinochit(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama rasmini yuboring, faqat rasmni!")
    await Picture.file_id.set()

@dp.message_handler(state=Picture.file_id, content_types=types.ContentType.PHOTO)
async def file_id_image(message: types.Message, state: FSMContext):
    image_file_id = message.photo[-1].file_id
    await state.update_data(
        {'image_file_id': image_file_id}
    )

    await message.answer(text="Yaxshi endi reklama textini yuboring")
    await Picture.text.set()

@dp.message_handler(state=Picture.text)
async def image_tekst(message: types.Message, state: FSMContext):
    image_text = message.text
    await state.update_data(
        {'image_text': image_text}
    )

    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no)
    await Picture.choose_yes_no.set()

@dp.callback_query_handler(state=Picture.choose_yes_no)
async def choose_yes_no_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    image_file_id = data.get('image_file_id')
    image_text = data.get('image_text')


    await call.message.delete()
    if call.data == 'choose_yoq':
        users = await db.select_all_users()
        for user in users:
            user_id = user[3]
            try:
                await bot.send_photo(chat_id=user_id, photo=image_file_id, caption=image_text)
                await asyncio.sleep(1)
            except Exception as error:
                print(error)
                continue

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await Picture.choose_yes.set()

@dp.message_handler(state=Picture.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    image_file_id = data.get('image_file_id')
    image_text = data.get('image_text')

    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        try:
            await bot.send_photo(chat_id=user_id, photo=image_file_id, caption=image_text,
                                                    reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
        except Exception as error:
            print(error)
            continue