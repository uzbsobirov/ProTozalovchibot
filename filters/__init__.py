from aiogram import Dispatcher

from loader import dp
from .group import IsGroup
from .private import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
