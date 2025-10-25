from aiogram import Dispatcher
from .start import start_handler
from .start import delete_me

def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(delete_me, commands=["delete"])
