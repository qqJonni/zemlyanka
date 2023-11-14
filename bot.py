import os

import long_messages
import keyboard

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
from aiogram import executor, types, Bot, Dispatcher

from sqlite import db_start, create_profile, edit_profile


load_dotenv(find_dotenv())
storage = MemoryStorage()
bot = Bot(os.environ.get('TELEGRAM_TOKEN'))
dp = Dispatcher(bot, storage=storage)
media_group = [types.InputMediaPhoto(media=photo) for photo in long_messages.ZEM_PHOTOS]


async def on_startup(_):  # Запускает базу данных при запуске бота
    await db_start()


class MessageStatesGroup(StatesGroup):  # Создаем обработчик состояний
    phone_number = State()
    address = State()
    name = State()


# ------- Обработка стартовых команд -------
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=long_messages.HELP_COMMANDS)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{long_messages.HELLO} /help', parse_mode='HTML', reply_markup=keyboard.get_start_ikb())
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgQAAxkBAAEKvvplUnmXAAEKsby2Cp2GpD-KKTmP97cAAlsXAAKm8XEeMnkyUbT3uFAzBA')
    await create_profile(user_id=message.from_user.id)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=long_messages.DESCRIPTION1)
    await bot.send_photo(chat_id=message.from_user.id, photo='https://vinde.md/wp-content/uploads/2021/04/7-1-100x100.jpg')
    await bot.send_message(chat_id=message.from_user.id, text=long_messages.DESCRIPTION2)
    await bot.send_message(chat_id=message.from_user.id, text=f'{long_messages.DESCRIPTION3} /list')
    await bot.send_message(chat_id=message.from_user.id, text=f'{long_messages.DESCRIPTION4} /dimensions')
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=55.669873, longitude=37.307199)


@dp.message_handler(commands=['list'])
async def send_list(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=long_messages.LIST)


@dp.message_handler(commands=['dimensions'])
async def send_dimensions(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=long_messages.DIMENSIONS)


# ------- Обработчики Inline кнопок -------
@dp.callback_query_handler(keyboard.cd.filter(action='boxing'))
async def push_boxing(callback: types.CallbackQuery):
    await callback.message.answer(text='Что делаем с вещами?', reply_markup=keyboard.get_rent_ikb())


@dp.callback_query_handler(keyboard.cd.filter(action='rent'))
async def push_rent(callback: types.CallbackQuery):
    pass  # Здесь необходимо реализовать логику функции, которая будет возвращать срок оставшейся аренды


@dp.callback_query_handler(keyboard.cd.filter(action='photo'))
async def push_photo(callback: types.CallbackQuery):
    await bot.send_media_group(chat_id=callback.message.chat.id, media=media_group)


@dp.callback_query_handler(keyboard.cd.filter(action='bring_myself'))
async def order_warehouse(callback: types.CallbackQuery):
    await callback.message.answer(text=long_messages.BRING_MYSELF, parse_mode='HTML')
    await bot.send_location(chat_id=callback.from_user.id, latitude=55.669873, longitude=37.307199)


@dp.callback_query_handler(keyboard.cd.filter(action='take_it_from_me'))
async def take_it_from_me(callback: types.CallbackQuery):
    await callback.message.answer(text='Напишите свой номер телефона:')
    await MessageStatesGroup.phone_number.set()


# ------- Обработчики состояния -------
@dp.message_handler(state=MessageStatesGroup.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await message.reply('Теперь напишите адрес:')
    await MessageStatesGroup.next()


@dp.message_handler(state=MessageStatesGroup.address)
async def get_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.reply('А как к вам обращаться?')
    await MessageStatesGroup.next()


@dp.message_handler(state=MessageStatesGroup.name)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await edit_profile(state, user_id=message.from_user.id)
    await message.reply('Ваши данные успешно сохранены! Наш менеджер свяжется с вами в течении часа!')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
