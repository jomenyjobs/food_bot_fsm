import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start, food # Импортируем наши папки с логикой

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры (важен порядок!)
    dp.include_router(start.router)
    dp.include_router(food.router)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())