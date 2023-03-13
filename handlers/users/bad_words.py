from loader import dp, db, bot
from keyboards.inline.badwords import bad_words_back
from states.badwords import BadWords

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="bad_words", state='*')
async def badd_words(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="Xaqoratli so'z qo'shish uchun yozing")
    await BadWords.word.set()

@dp.message_handler(state=BadWords.word)
async def baddd_words(message: types.Message, state: FSMContext):
    bad_word = message.text
    try:
        await db.add_word_to_bad_word(badword=bad_word)
        await message.answer(text="So'z bazaga qo'shildi✅\n\nYana kiritishni xoxlasangiz so'z yuboring",
                                                            reply_markup=bad_words_back)
    except:
        await message.answer(text="Bu so'z bazada bor ekan, boshqattan urinib ko'ring", reply_markup=bad_words_back)