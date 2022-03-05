from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import main_menu

menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Выдать задание',
                             callback_data=main_menu.new(name='in_quest'))
    ]
])
