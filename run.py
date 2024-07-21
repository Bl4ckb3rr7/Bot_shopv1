import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router as user_router
from app.admin import admin as admin_router
from app.database.models import async_main

async  def main(): # Это ассинхронная функция .которая запускает всего бота
    load_dotenv() # Утелита для скрытия токена для бота

    await async_main()

    bot = Bot(token = os.getenv('TOKEN')) # Тут создается экземпляр бота, передавая ему токен
    dp = Dispatcher()   # Создание диспетчера, который занимается обработкой всех входящих обновлений

    dp.include_routers(user_router, admin_router) # Роутеры по которым обрабатываются сообщения от телеграма
    await dp.start_polling(bot) # Поиск обновлений приходящих от телеграма для диспетчера


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')