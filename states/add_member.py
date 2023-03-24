from aiogram.dispatcher.filters.state import State, StatesGroup

class AddMember(StatesGroup):
    number = State()