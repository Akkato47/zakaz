from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InputFile

from keyboards.inline import next_keyboard
from keyboards.inline.callback_data import next_menu, main_menu
from loader import dp
from utils.misc.get_random_quest import get_random


@dp.callback_query_handler(main_menu.filter(name='in_quest'), state='def')
async def send_quest_user(call: CallbackQuery, state: FSMContext):
    send_quest_user.n, send_quest_user.a = get_random()
    await call.answer()
    photo = InputFile(f'data/pic/{send_quest_user.n + 1}_req.jpg')
    await dp.bot.send_photo(chat_id=call.from_user.id, photo=photo, reply_markup=next_keyboard)


@dp.callback_query_handler(next_menu.filter(name='go_next'), state='def')
async def go_next_quest(call: CallbackQuery, state: FSMContext):
    send_quest_user.n, send_quest_user.a = get_random()
    await call.answer()
    photo = InputFile(f'data/pic/{send_quest_user.n + 1}_req.jpg')
    await dp.bot.send_photo(chat_id=call.from_user.id, photo=photo, reply_markup=next_keyboard)


@dp.message_handler(state='def')
async def check_answer(message: types.Message, state: FSMContext):
    if message.text == str(send_quest_user.a):
        await message.answer('Правильно', reply_markup=next_keyboard)
    elif message.text != str(send_quest_user.a):
        photo = InputFile(f'data/pic/{send_quest_user.n + 1}.jpg')
        await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo)
        await message.answer('Неправильно. Вот решение', reply_markup=next_keyboard)
