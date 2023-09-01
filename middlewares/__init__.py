from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .is_admin import CheckingAdmin


if __name__ == "middlewares":
    dp.middleware.setup(CheckingAdmin())
