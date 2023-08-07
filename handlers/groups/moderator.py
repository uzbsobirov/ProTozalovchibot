import logging
import datetime
from aiogram.dispatcher import FSMContext
from aiogram import types

from loader import dp, db, bot
from filters import IsGroup
from utils.misc.subscription import check
from keyboards.inline.start import elite_start
from keyboards.inline.start import elite_start_group
from states.group_adv import CheckAcsess


@dp.message_handler(IsGroup(), state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name # Full name
    user_id = message.from_user.id # User id
    username = message.from_user.username
    user_mention = message.from_user.get_mention(name=full_name, as_html=True) # User mention <a href=''></a>
    chat_id = message.chat.id # Group id
    check_is_not_bot = message['from']['is_bot']

    # Add user id and how many member added to chat
    try:
        await db.add_id_to_addmember(user_id=user_id, is_added=0)
    except:
        pass

    try:
        chat = await bot.get_chat(chat_id)
        invite_link = await chat.export_invite_link()
        await db.add_id_of_group(chat_id=chat_id, link=invite_link)
    except Exception as error:
        chat = await bot.get_chat(chat_id)
        invite_link = await chat.export_invite_link()
        await db.update_group_id(chat_id=chat_id)
        logging.info(f"{error} -- groups/moderator.py -> 36")

    checking = await check(user_id=user_id, chat_id=chat_id)  # We must check if user is admin in the group


    try:
        await db.add_user(
            full_name=full_name,
            username=username,
            user_id=user_id,
            has_acsess='false'
        )
    except:
        pass

    # Majburiy odam qoshish


    if checking is True:
        try:
            text = message.text
            splited = text.split(' ')
            args = message.get_args()
            if '/add' in text and len(splited) == 2:
                selection = await db.select_many_member()
                if len(selection) == 0:
                    await db.add_members_to_adminpanel(members=int(args), chat_id=chat_id, power='add')
                else:
                    await db.update_add_members(members=int(args), chat_id=chat_id)
                    await db.update_power(power='add', chat_id=chat_id)
                await message.answer(text=f"Majburiy a'zo {args} ga o'zgardi✅\n\nGuruh azolari guruhda yozish "
                                          f"uchun {args} ta odam qo'shishlari shart")
            elif len(splited) == 2 and '/off @protozalovchibot' in text.lower():
                await db.update_power(power='off', chat_id=chat_id)
                await message.answer(text="Majburiy azolik o'chirildi✅", reply_markup=elite_start_group)

        except Exception as err:
            logging.info(f"{err} -- groups/moderator.py -> 73")
            pass

    # <-------------------------->

    select_is_added = await db.select_add_member(user_id=user_id)
    number_is_added = select_is_added[0][0]
    select_members = await db.select_many_member()
    try:
        if chat_id == select_members[0][1]:
            if select_members[0][2] == 'add':
                if check_is_not_bot != True:
                    if checking is not True:
                        try:
                            if number_is_added < select_members[0][0]:

                                ed = select_members[0][0] - number_is_added
                                await message.delete()
                                text = f"<b>📛 {user_mention} - Guruhda yozish uchun avval {ed} ta odam qo'shing!</b>"
                                await message.answer(text=text, reply_markup=elite_start)
                        except Exception as err:
                            print(err)
                            pass
    except Exception as er:
        logging.info(f"{er} -- groups/moderator.py -> 96")


    try:
        await CheckAcsess.check.set()
        is_channel = message['from']['username']
        is_channel_double = message['from']['first_name']
        channel_username = message['sender_chat']['username']
        channel_name = message['sender_chat']['title']
        chennel_mention = f"<a href='https://t.me/{channel_username}'>{channel_name}</a>"

        if is_channel == 'Channel_Bot' or is_channel_double == 'Channel':
            await message.delete()
            text = f"{chennel_mention} kanal nomidan yozmang!"
            deleted_text = await message.answer(text=text, reply_markup=elite_start_group, disable_web_page_preview=True)
            # await asyncio.sleep(10)
            # await deleted_text.delete()

        await state.finish()
    except:
        pass



    if check_is_not_bot != True:
        if checking is not True:
            for entity in message.entities:
                if entity.type in ['url', 'mention', 'text_link']:
                    await message.delete()
                    text = f"❗️{user_mention} iltimos reklama tarqatmang!"
                    deleted_text = await message.answer(text=text, reply_markup=elite_start_group)
                    # await asyncio.sleep(10)
                    # await deleted_text.delete()

    # List of arabian letter
    list_of_arab_words = ['ب', 'د', 'أنا', 'ص', 'ح', 'ه', 'ز', 'هي تكون', 'ش', 'ن', 'ز', 'تكون', 'ج', 'س', 'ا', 'م', 'ذ', 'ذ', 'ل', 'أ']
    if checking is not True:
        for item in list_of_arab_words:
            if item in message.text:
                await message.delete()
                await message.chat.kick(user_id=user_id)
                break



    list_of_insulting_words = await db.select_all_badwrods()
    msg = message.text
    if check_is_not_bot != True:
        if checking is not True:
            for word in list_of_insulting_words:
                if msg in word[0]:
                    try:
                        await message.delete()
                        text = f"❗️{user_mention} iltimos xaqoratli so'z ishlatmang"
                        bad_text = await message.answer(text=text, reply_markup=elite_start_group)
                        # await asyncio.sleep(10)
                        # await bad_text.delete()
                        restriction_time = 5
                        until_date = datetime.datetime.now() + datetime.timedelta(minutes=restriction_time)
                        await message.chat.restrict(user_id=user_id,
                                                    can_send_messages=False, until_date=until_date)
                    except:
                        pass


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS, state='*')
async def new_member(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    # If New User join to group, we should delete message of user
    try:
        await message.delete()
    except:
        pass

    user_id = message.from_user.id
    length_members = len(message.new_chat_members)

    try:
        await db.add_id_to_addmember(user_id=user_id, is_added=0)
    except:
        pass

    new_chat_members = message.new_chat_members

    for new_chat_member in new_chat_members:
        full_name = new_chat_member.full_name
        new_user_id = new_chat_member.id
        user_mention = f"<a href='tg://user?id={new_user_id}'>{full_name}</a>"
        text = f"<b>Xush kelibsiz {user_mention}</b>"
        try:
            await message.answer(text=text)
        except:
            pass

        try:
            chat = await bot.get_chat(chat_id)
            invite_link = await chat.export_invite_link()
            await db.add_id_of_group(chat_id=chat_id, link=invite_link)
        except Exception as error:
            chat = await bot.get_chat(chat_id)
            invite_link = await chat.export_invite_link()
            await db.update_group_id(chat_id=chat_id)
            logging.info(f"{error} -- groups/moderator.py -> 36")


    select_is_add = await db.select_add_member(user_id=user_id)
    count_add = select_is_add[0][0]
    count_add += length_members
    await db.update_add_member(user_id=user_id, is_added=count_add)




@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER, state='*')
async def banned_member(message: types.Message, state: FSMContext):

    # If New User left to group, we should delete message of user
    try:
        await message.delete()
    except:
        pass

@dp.message_handler(IsGroup(), content_types=types.ContentType.PHOTO, state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name # Full name
    user_mention = message.from_user.get_mention(name=full_name, as_html=True) # User mention <a href=''></a>
    check_is_not_bot = message['from']['is_bot']
    user_id = message.from_user.id
    chat_id = message.chat.id  # Group id
    checking = await check(user_id=user_id, chat_id=chat_id)

    if check_is_not_bot != True:
        if checking is not True:
            types_of_message = ['url', 'mention', 'text_link']
            entity = message['caption_entities'][0]['type']
            if entity in types_of_message:
                await message.delete()
                text = f"❗️{user_mention} iltimos reklama tarqatmang!"
                deleted_text = await message.answer(text=text, reply_markup=elite_start_group)
                # await asyncio.sleep(10)
                # await deleted_text.delete()

@dp.message_handler(IsGroup(), content_types=types.ContentType.VIDEO, state='*')
async def deleteads(message: types.Message, state: FSMContext):
    full_name = message.from_user.full_name  # Full name
    user_mention = message.from_user.get_mention(name=full_name, as_html=True)  # User mention <a href=''></a>
    user_id = message.from_user.id
    chat_id = message.chat.id  # Group id
    checking = await check(user_id=user_id, chat_id=chat_id)
    check_is_not_bot = message['from']['is_bot']

    if check_is_not_bot != True:
        if checking is not True:
            types_of_message = ['url', 'mention', 'text_link']
            entity = message['caption_entities'][0]['type']
            if entity in types_of_message:
                await message.delete()
                text = f"❗️{user_mention} iltimos reklama tarqatmang!"
                deleted_text = await message.answer(text=text, reply_markup=elite_start_group)
                # await asyncio.sleep(10)
                # await deleted_text.delete()

