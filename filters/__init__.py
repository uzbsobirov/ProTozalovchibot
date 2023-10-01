from aiogram import Dispatcher

from loader import dp
from .group import IsGroup
from .private import IsPrivate
from .isadmin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)
