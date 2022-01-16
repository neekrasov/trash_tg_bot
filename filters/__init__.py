from aiogram import Dispatcher

from .private import *


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsChannels)
    dp.filters_factory.bind(IsAdmin)
