from loader import dp, db
from states.add_member import AddMember
from keyboards.inline.backs import back_stat
from filters.group import IsGroup

from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(IsGroup(), state='*')
async def  add_member_majburiy(message: types.Message, state: FSMContext):
    text = message.text
    splited = text.split(' ')
    number = splited[1]
    #
    if '/add' in text and len(text) == 2:
        selection = await db.select_many_member()
        if len(selection) == 0:
            print('keldi1')
            await db.add_members_to_adminpanel(members=int(number))
        else:
            print('keldi')
            await db.update_add_members(members=int(number))
        await message.answer(text=f"Majburiy a'zo {number} ga o'zgardi✅", reply_markup=back_stat)

    # select_members = await db.select_many_member()
    # number_of_member = select_members[0][0]
    #
    # text = f"<b>Hozirgi majburiy odam qo'shish soni, O'zgartirish uchun raqam yuboring</b>\n\n👉🏻 {number_of_member}"
    # await message.edit_text(text=text)
    # await AddMember.number.set()

# @dp.message_handler(state=AddMember.number)
# async def state_number(message: types.Message, state: FSMContext):
#     try:
#         number = int(message.text)
#         #
#         selection = await db.select_many_member()
#         if len(selection) == 0:
#             await db.add_members_to_adminpanel(members=number)
#         else:
#             await db.update_add_members(members=number)
#         await message.answer(text=f"Majburiy a'zo {number} ga o'zgardi✅", reply_markup=back_stat)
#         # await state.finish()
#
#     except Exception as error:
#         print(error)
#         await message.answer(text="Iltimos, faqat raqam kiriting...")
#         await AddMember.number.set()