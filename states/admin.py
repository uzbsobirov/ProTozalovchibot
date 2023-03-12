from aiogram.dispatcher.filters.state import State, StatesGroup

class Admin(StatesGroup):
    main_admin = State()
    stat = State()
    sending = State()

class SendingGroup(StatesGroup):
    group = State()

class SendingUser(StatesGroup):
    user = State()