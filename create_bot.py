import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

storage = MemoryStorage()
bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot, storage=storage)
