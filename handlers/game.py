from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import WEBAPP_URL

router = Router()

# Команда /game
@router.message(Command("game"))
async def cmd_game(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Играть (Крестики-Нолики)", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer(
        "<b>Искусственный интеллект готов к битве!</b>\n"
        "Нажми кнопку ниже, чтобы запустить игру 👇",
        reply_markup=markup,
        parse_mode="HTML"
    )

# Обработка результата игры (победа/поражение)
@router.message(F.web_app_data)
async def process_game_result(message: types.Message):
    result = message.web_app_data.data
    
    if result == 'win':
        text = "🏆 <b>ПОБЕДА!</b> Ты обыграл ИИ!"
    elif result == 'loss':
        text = "💀 <b>ПОРАЖЕНИЕ...</b> Искусственный интеллект оказался умнее."
    elif result == 'draw':
        text = "🤝 <b>НИЧЬЯ.</b> Достойная игра."
    else:
        text = f"Данные из приложения: {result}"

    await message.answer(text, parse_mode="HTML")
