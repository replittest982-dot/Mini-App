import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiohttp import web

# Импортируем конфиг и хендлеры
from config import BOT_TOKEN
from handlers import start, game

# --- WEB SERVER (Для сайта) ---
async def web_handler(request):
    return web.FileResponse('./www/index.html')

def setup_web_app():
    app = web.Application()
    app.router.add_get('/', web_handler)
    return app

# --- ЗАПУСК БОТА ---
async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    if not BOT_TOKEN:
        print("❌ ОШИБКА: Нет BOT_TOKEN!")
        return

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем И start, И game
    dp.include_router(start.router)
    dp.include_router(game.router)

    # Запускаем сервер сайта (Порт 8000)
    runner = web.AppRunner(setup_web_app())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    await site.start()
    
    print("🌐 Сервер игры работает на порту 8000")
    print("🤖 Бот запущен...")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stop")
