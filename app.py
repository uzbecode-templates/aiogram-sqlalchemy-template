import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from database.db import init_db
from handlers.users.register import register_all_handlers as user_register_all_handlers
from config import cfg

BOT_TOKEN = cfg.BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop)

async def on_startup(_):
    await init_db()
    print("Database initialized successfully")

    user_register_all_handlers(dp)
    print("Handlers registered successfully")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
