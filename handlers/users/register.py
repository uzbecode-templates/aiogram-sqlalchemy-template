from aiogram import Dispatcher
from .start import start_handler

def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
