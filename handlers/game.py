from aiogram import Router, F, types

router = Router()

# Ловим данные от Mini App (когда игра закончилась)
@router.message(F.web_app_data)
async def process_game_result(message: types.Message):
    result = message.web_app_data.data
    
    if result == 'win':
        text = "🏆 <b>ПОБЕДА!</b> Ты уничтожил мой алгоритм!"
    elif result == 'loss':
        text = "💀 <b>ПОРАЖЕНИЕ...</b> Искусственный интеллект оказался хитрее."
    elif result == 'draw':
        text = "🤝 <b>НИЧЬЯ.</b> Битва титанов."
    else:
        text = "Данные получены."

    await message.answer(text, parse_mode="HTML")
