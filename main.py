import asyncio
import logging
import sys
import os

from app.handlers import router
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.database.models import async_main

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv("TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()





async def main() -> None:
    await async_main()
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
