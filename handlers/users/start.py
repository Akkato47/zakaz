import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.main_menu_keyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def on_start_add_user(message: types.Message, state: FSMContext):
    await state.set_state('def')
    await message.answer(text='Выберите дейтсвие', reply_markup=menu)

