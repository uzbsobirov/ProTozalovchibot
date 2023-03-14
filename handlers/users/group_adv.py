import asyncio
from loader import db, dp, bot
from states.group_adv import *
from keyboards.inline.adv import yes_no_group, buttons, back_group

from aiogram import types
from aiogram.dispatcher import FSMContext



# <------------Adver with photo and text------------->
@dp.callback_query_handler(text="withpicturegroup", state='*')
async def odinochit(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama rasmini yuboring, faqat rasmni!")
    await GPicture.file_id.set()


@dp.message_handler(state=GPicture.file_id, content_types=types.ContentType.PHOTO)
async def file_id_image(message: types.Message, state: FSMContext):
    image_file_id = message.photo[-1].file_id
    await state.update_data(
        {'group_image_file_id': image_file_id}
    )

    await message.answer(text="Yaxshi endi reklama textini yuboring")
    await GPicture.text.set()


@dp.message_handler(state=GPicture.text)
async def image_tekst(message: types.Message, state: FSMContext):
    image_text = message.text
    await state.update_data(
        {'group_image_text': image_text}
    )

    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no_group)
    await GPicture.choose_yes_no.set()


@dp.callback_query_handler(state=GPicture.choose_yes_no)
async def choose_yes_no_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    image_file_id = data.get('group_image_file_id')
    image_text = data.get('group_image_text')

    await call.message.delete()
    if call.data == 'choose_yoq_group':
        await state.finish()

        success_send = 0
        not_send = 0
        groups = await db.select_all_group()
        for group in groups:
            group_id = group[1]
            try:
                await bot.send_photo(chat_id=group_id, photo=image_file_id, caption=image_text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue

        await call.message.answer(text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli "
                                       f"yuborildi\n\n"
                                       f"❌ Reklama <i>{not_send}</i> ta guruhga yuborilmadi</b>", reply_markup=back_group)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await GPicture.choose_yes.set()


@dp.message_handler(state=GPicture.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    image_file_id = data.get('group_image_file_id')
    image_text = data.get('group_image_text')

    success_send = 0
    not_send = 0
    groups = await db.select_all_group()
    for group in groups:
        group_id = group[1]
        try:
            await bot.send_photo(chat_id=group_id, photo=image_file_id, caption=image_text,
                                 reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue
        await state.finish()

    await message.answer(
        text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli yuborildi\n\n"
             f"❌ Reklama <i>{not_send}</i> ta guruhga bormadi</b>", reply_markup=back_group)


# <------------Adver with text------------->
@dp.callback_query_handler(text="withtextgroup", state='*')
async def withtextprivate(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama textini yuboring")
    await GText.text.set()


@dp.message_handler(state=GText.text)
async def text_texti(message: types.Message, state: FSMContext):
    text_text = message.text

    await state.update_data(
        {'group_text_text': text_text}
    )
    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no_group)
    await GText.choose_yes_no.set()


@dp.callback_query_handler(state=GText.choose_yes_no)
async def choose_yes_no(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get('group_text_text')

    await call.message.delete()

    if call.data == 'choose_yoq_group':
        await state.finish()

        success_send = 0
        not_send = 0

        groups = await db.select_all_group()
        for group in groups:
            group_id = group[1]
            try:
                await bot.send_message(chat_id=int(group_id), text=text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue
        await call.message.answer(
            text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli yuborildi\n\n"
                 f"❌ Reklama <i>{not_send}</i> ta guruhga bormadi</b>", reply_markup=back_group)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await GText.choose_yes.set()


@dp.message_handler(state=GText.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text
    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    text = data.get('group_text_text')

    not_send = 0
    success_send = 0

    groups = await db.select_all_group()
    for group in groups:
        group_id = group[1]
        try:
            await bot.send_message(chat_id=int(group_id), text=text,
                                   reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue

        await state.finish()
    await message.answer(text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli yuborildi\n\n"
                              f"❌ Reklama <i>{not_send}</i> ta guruhga bormadi</b>", reply_markup=back_group)


# <------------Adver with video and text------------->
@dp.callback_query_handler(text="withvideogroup", state='*')
async def odinochit(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Reklama videosini yuboring, faqat videoni!")
    await GVideo.file_id.set()


@dp.message_handler(state=GVideo.file_id, content_types=types.ContentType.VIDEO)
async def file_id_image(message: types.Message, state: FSMContext):
    video_file_id = message.video.file_id
    await state.update_data(
        {'group_video_file_id': video_file_id}
    )

    await message.answer(text="Yaxshi endi reklama textini yuboring")
    await GVideo.text.set()


@dp.message_handler(state=GVideo.text)
async def image_tekst(message: types.Message, state: FSMContext):
    video_text = message.text
    await state.update_data(
        {'group_video_text': video_text}
    )

    await message.answer(text="Tugma qo'shishni xoxlaysizmi?", reply_markup=yes_no_group)
    await GVideo.choose_yes_no.set()


@dp.callback_query_handler(state=GVideo.choose_yes_no)
async def choose_yes_no_data(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    video_file_id = data.get('group_video_file_id')
    video_text = data.get('group_video_text')

    await call.message.delete()
    if call.data == 'choose_yoq_group':
        await state.finish()
        not_send = 0
        success_send = 0

        groups = await db.select_all_group()
        for group in groups:
            group_id = group[1]
            try:
                await bot.send_video(chat_id=group_id, video=video_file_id, caption=video_text)
                await asyncio.sleep(1)
                success_send += 1
            except Exception as error:
                print(error)
                not_send += 1
                continue
        await call.message.answer(
            text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli yuborildi\n\n"
                 f"❌ Reklama <i>{not_send}</i> ta guruhga yuborilmadi</b>", reply_markup=back_group)

    else:
        choose_text = "<b>Tugma qo'shmoqchi bo'lsangiz namunadagidek qilib yuboring👇\n\n" \
                      "<code>Foydali botlar+https://t.me/kayzenuz</code></b>"
        await call.message.answer(text=choose_text)
        await GVideo.choose_yes.set()




@dp.message_handler(state=GVideo.choose_yes)
async def user_choose_ha_image(message: types.Message, state: FSMContext):
    btn_link = message.text

    split_text = btn_link.split('+')
    adv_text = split_text[0]
    adv_url = split_text[1]

    data = await state.get_data()
    video_file_id = data.get('group_video_file_id')
    video_text = data.get('group_video_text')

    not_send = 0
    success_send = 0
    groups = await db.select_all_group()
    for group in groups:
        group_id = group[1]
        try:
            await bot.send_video(chat_id=int(group_id), video=video_file_id, caption=video_text,
                                 reply_markup=buttons(text=adv_text, url=adv_url))
            await asyncio.sleep(1)
            success_send += 1
        except Exception as error:
            print(error)
            not_send += 1
            continue

    await message.answer(
        text=f"<b>✅ Reklama <i>{success_send}</i> ta guruhga muvaffaqqiyatli yuborildi\n\n"
             f"❌ Reklama <i>{not_send}</i> ta guruhga yuborilmadi</b>", reply_markup=back_group)

    await state.finish()