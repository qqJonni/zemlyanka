from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=2)
ikb2 = InlineKeyboardMarkup(row_width=2)

# Кнопки начального меню
ib1 = InlineKeyboardButton(text='Заказать бокс', callback_data='boxing')
ib2 = InlineKeyboardButton(text='Срок аренды', callback_data='rent')
ib3 = InlineKeyboardButton(text='Фото Zемлянки', callback_data='photo')

# Кнопки выбора аренды
ib4 = InlineKeyboardButton(text='Привезу сам', callback_data='bring_myself')
ib5 = InlineKeyboardButton(text='Заберите у меня', callback_data='take_it_from_me')


ikb.add(ib1, ib2, ib3)
ikb2.add(ib4, ib5)
