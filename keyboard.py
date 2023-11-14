from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cd = CallbackData('ikb', 'action')  # This is a pattern from official documentation


# Функция срабатывает при нажатии /start
def get_start_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Заказать бокс', callback_data=cd.new('boxing'))],
        [InlineKeyboardButton('Срок аренды', callback_data=cd.new('rent'))],
        [InlineKeyboardButton('Фото Zемлянки', callback_data=cd.new('photo'))],
    ])
    return ikb


# Функция реагирует на нажатие кнопки 'Заказать бокс'
def get_rent_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Привезу сам', callback_data=cd.new('bring_myself'))],
        [InlineKeyboardButton('Заберите у меня', callback_data=cd.new('take_it_from_me'))],
    ])
    return ikb
