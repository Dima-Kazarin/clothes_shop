import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

TOKEN = '7813399487:AAHqgfS1RHnqVSBTjg7oKgM2AUZsNVb3p0k'


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
