from aiogram.dispatcher.filters.state import State, StatesGroup

class Picture(StatesGroup):
    file_id = State()
    text = State()
    choose_yes_no = State()
    choose_yes = State()