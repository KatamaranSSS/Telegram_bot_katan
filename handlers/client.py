from aiogram import types, Dispatcher
from bot_app.create_bot import bot
from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text

# noinspection PyBroadException


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Test_katan_bot')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Пушкина 25')  # , reply_markup=ReplyKeyboardRemove())


async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, Text(equals='режим работы', ignore_case=True))
    dp.register_message_handler(pizza_place_command, Text(equals='расположение', ignore_case=True))
    dp.register_message_handler(pizza_menu_command, Text(equals='меню', ignore_case=True))
