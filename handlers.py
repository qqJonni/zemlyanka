import long_messages
import keyboard


from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from sqlite import create_profile, edit_profile
from create_bot import bot

media_group = [types.InputMediaPhoto(media=photo) for photo in long_messages.ZEM_PHOTOS]


class MessageStatesGroup(StatesGroup):  # Создаем обработчик состояний
    phone_number = State()
    address = State()
    name = State()


async def help_command(message: types.Message):
    await message.reply(text=long_messages.HELP_COMMANDS)


async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                        text=f'{long_messages.HELLO} /help', parse_mode='HTML', reply_markup=keyboard.get_start_ikb())
    await bot.send_sticker(message.from_user.id,
                        sticker='CAACAgQAAxkBAAEKvvplUnmXAAEKsby2Cp2GpD-KKTmP97cAAlsXAAKm8XEeMnkyUbT3uFAzBA')
    await create_profile(user_id=message.from_user.id)


async def description_command(message: types.Message):
    await message.reply(text=long_messages.DESCRIPTION1)
    await bot.send_photo(chat_id=message.from_user.id, photo='https://vinde.md/wp-content/uploads/2021/04/7-1-100x100.jpg')
    await bot.send_message(chat_id=message.from_user.id, text=long_messages.DESCRIPTION2)
    await bot.send_message(chat_id=message.from_user.id, text=f'{long_messages.DESCRIPTION3} /list')
    await bot.send_message(chat_id=message.from_user.id, text=f'{long_messages.DESCRIPTION4} /dimensions')
    await message.delete()


# async def send_point(message: types.Message):
#     await bot.send_location(chat_id=message.from_user.id, latitude=55.669873, longitude=37.307199)


# async def send_list(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text=long_messages.LIST)


# async def send_dimensions(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id, text=long_messages.DIMENSIONS)


# # ------- Обработчики Inline кнопок -------
# async def push_boxing(callback: types.CallbackQuery):
#     await callback.message.answer(text='Что делаем с вещами?', reply_markup=keyboard.get_rent_ikb())


# async def push_rent(callback: types.CallbackQuery):
#     pass  # Здесь необходимо реализовать логику функции, которая будет возвращать срок оставшейся аренды


# async def push_photo(callback: types.CallbackQuery):
#     await bot.send_media_group(chat_id=callback.message.chat.id, media=media_group)


# async def order_warehouse(callback: types.CallbackQuery):
#     await callback.message.answer(text=long_messages.BRING_MYSELF, parse_mode='HTML')
#     await bot.send_location(chat_id=callback.from_user.id, latitude=55.669873, longitude=37.307199)


# async def take_it_from_me(callback: types.CallbackQuery):
#     await callback.message.answer(text='Напишите свой номер телефона:')
#     await MessageStatesGroup.phone_number.set()


# # ------- Обработчики состояния -------
# async def get_phone_number(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['phone_number'] = message.text
#     await message.reply('Теперь напишите адрес:')
#     await MessageStatesGroup.next()


# async def get_address(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['address'] = message.text
#     await message.reply('А как к вам обращаться?')
#     await MessageStatesGroup.next()


# async def get_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await edit_profile(state, user_id=message.from_user.id)
#     await message.reply('Ваши данные успешно сохранены! Наш менеджер свяжется с вами в течении часа!')
#     await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(description_command, commands=['description'])
    # dp.register_message_handler(send_point, commands=['location'])
    # dp.register_message_handler(send_list, commands=['list'])
    # dp.register_message_handler(send_dimensions, commands=['dimensions'])
    # dp.register_message_handler(push_boxing, keyboard.cd.filter(action='boxing'))
    # dp.register_message_handler(push_rent, keyboard.cd.filter(action='rent'))
    # dp.register_message_handler(push_photo, keyboard.cd.filter(action='photo'))
    # dp.register_message_handler(order_warehouse, keyboard.cd.filter(action='bring_myself'))
    # dp.register_message_handler(take_it_from_me, keyboard.cd.filter(action='take_it_from_me'))
    # dp.register_message_handler(get_phone_number, state=MessageStatesGroup.phone_number)
    # dp.register_message_handler(get_address, state=MessageStatesGroup.address)
    # dp.register_message_handler(get_name, state=MessageStatesGroup.name)
