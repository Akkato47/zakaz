import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.main_menu_keyboard import menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def on_start_add_user(message: types.Message, state: FSMContext):
    try:
        await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id
        )
        await state.set_state('def')
    except asyncpg.exceptions.UniqueViolationError:
        await state.set_state('def')
    await message.answer(text='Выберите дейтсвие', reply_markup=menu)

