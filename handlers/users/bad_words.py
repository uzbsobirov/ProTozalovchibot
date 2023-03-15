from loader import dp, db, bot
from keyboards.inline.badwords import *
from states.badwords import BadWords, DeleteBadWords

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="bad_words", state='*')
async def badd_words(call: types.CallbackQuery, state: FSMContext):

    result = ""
    list_of_bad_words = await db.select_all_badwrods()
    for b_word in list_of_bad_words:
        result += f"{b_word[0]}, "
    await call.message.edit_text(text=f"Xaqoratli so'z qo'shish uchun yozing\n\nBazadagi so'zlar: <b>{result}</b>",
                                                reply_markup=deleted_bad_word)
    await BadWords.word.set()

@dp.message_handler(state=BadWords.word)
async def baddd_words(message: types.Message, state: FSMContext):
    bad_word = message.text
    try:
        await db.add_word_to_bad_word(badword=bad_word.lower())
        await message.answer(text="So'z bazaga qo'shildi✅\n\nYana kiritishni xoxlasangiz so'z yuboring",
                                                            reply_markup=bad_words_back)
    except:
        await message.answer(text="Bu so'z bazada bor ekan, boshqattan urinib ko'ring", reply_markup=bad_words_back)


@dp.callback_query_handler(text="delete_bad_word", state='*')
async def delete_bad_word(call: types.CallbackQuery, state: FSMContext):

    result = ""
    list_of_bad_words = await db.select_all_badwrods()
    for b_word in list_of_bad_words:
        result += f"<code>{b_word[0]}</code>, "
    await call.message.edit_text(text="Qaysi so'zni o'chirmoqchi bo'lsangiz o'sha so'zni yuboring\n\n"
                                      f"Bazadagi so'zlar: {result}", reply_markup=bad_words_back_loading)
    await DeleteBadWords.word.set()

@dp.message_handler(state=DeleteBadWords.word)
async def delete_state(message: types.Message, state: FSMContext):
    deleted_word = message.text

    select_bad_words = await db.select_all_badwrods()
    for one_word in select_bad_words:
        if deleted_word.lower() == one_word[0].lower():
            await db.delete_bad_word(badword=deleted_word)
            await message.answer(text=f"<b><i>{deleted_word}</i></b> -- so'zi bazadan o'chirildi", reply_markup=bad_words_back_succes)
            await DeleteBadWords.word.set()
            break


        # else:
        #     await message.answer(text="Bunday so'z bazadan topilmadi")




