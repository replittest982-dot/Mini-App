import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiohttp import web

# Импорты наших модулей
from config import BOT_TOKEN
from handlers import start, game # Убедись, что start.py тоже есть, или удали его отсюда

# --- WEB SERVER (Для отображения сайта) ---
async def web_handler(request):
    # Отдаем index.html при заходе на сайт
    return web.FileResponse('./www/index.html')

def setup_web_app():
    app = web.Application()
    app.router.add_get('/', web_handler)
    # Если добавишь картинки/css, раскомментируй строку ниже:
    # app.router.add_static('/static/', path='./www/static/', name='static')
    return app

# --- ЗАПУСК ---
async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Проверка токена
    if not BOT_TOKEN:
        print("❌ ОШИБКА: Не указан BOT_TOKEN в переменных окружения!")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    # dp.include_router(start.router) # Если есть стартовый файл
    dp.include_router(game.router)    # Наша игра

    # Запуск веб-сервера (чтобы ссылка https://krestikinoliki... работала)
    runner = web.AppRunner(setup_web_app())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    
    print("🌐 Web Server (Mini App) запущен на порту 8080")
    print("🤖 Бот запущен...")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
