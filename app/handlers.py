from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup

import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def start(message):
    await message.answer('Hello', reply_markup=kb.main)

