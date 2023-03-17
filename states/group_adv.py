from aiogram.dispatcher.filters.state import State, StatesGroup

class GPicture(StatesGroup):
    file_id = State()
    text = State()
    choose_yes_no = State()
    choose_yes = State()

class GText(StatesGroup):
    text = State()
    choose_yes_no = State()
    choose_yes = State()

class GVideo(StatesGroup):
    file_id = State()
    text = State()
    choose_yes_no = State()
    choose_yes = State()

class CheckAcsess(StatesGroup):
    check = State()