import long_messages
import handlers

from aiogram import executor, types
from sqlite import db_start
from create_bot import dp


media_group = [types.InputMediaPhoto(media=photo) for photo in long_messages.ZEM_PHOTOS]


async def on_startup(_):  # Запускает базу данных при запуске бота
    await db_start()


handlers.start_command(dp)
handlers.description_command(dp)
handlers.send_point(dp)
handlers.send_list(dp)
handlers.send_dimensions(dp)
handlers.push_boxing(dp)
handlers.push_rent(dp)
handlers.push_photo(dp)
handlers.order_warehouse(dp)
handlers.take_it_from_me(dp)
# handlers.get_phone_number(dp)
# handlers.get_address(dp)
# handlers.get_name(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
