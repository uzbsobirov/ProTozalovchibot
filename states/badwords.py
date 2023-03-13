from aiogram.dispatcher.filters.state import State, StatesGroup

class BadWords(StatesGroup):
    word = State()
