import logging

# Оповещения о том что бот запущен
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp)
