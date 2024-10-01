import traceback
import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.parsing.parse import parser
from app.rate.dollar_rate import Dollar_Rate

router = Router()


class Choosing(StatesGroup):
    choosing_name = State()


@router.message(Command("start"))
async def cmd_find(mes: Message, state: FSMContext):
    logging.info(f"/start mes: {mes}")
    await state.set_state(Choosing.choosing_name)
    await mes.answer("Добрый день. Как вас зовут?")


@router.message(Choosing.choosing_name)
async def cmd_chose_song(mes: Message, state: FSMContext):
    user_message = mes.text
    logging.info("state: choosing_song")
    logging.info(f"mes: {user_message}")
    dollar_rate = await Dollar_Rate().get_dollar_rate()
    rub, kop = parser.parse_dollar_rate(dollar_rate)
    if user_message:
        await state.update_data(choosing_name=user_message)
        await state.set_state(Choosing.choosing_name)
        data = await state.get_data()
        await mes.answer(f"Рад знакомству, {data['choosing_name']}")
        await mes.answer(f"Курс доллара сегодня равен {rub}, {kop}")

