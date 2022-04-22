# С помощью этого кода можно запретить боту отвечать на сообщения которые не являются командой
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import BOT_TOKEN


bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Здаров')


@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
    await message.answer(message.text)


# @dp.message_handler(lambda message: 'такси' in message.text)
# async def taxi(message : types.Message):
# await message.answer('такси')

@dp.message_handler(lambda message: 'нло' in message.text)
async def ufo(message: types.Message):
    await message.answer('нло')
# Эти два декоратора улавливают слова в сообщении и возвращают булевое значение (True or False).
# Например в первом декорторе. Если мы напишем заказать такси он вернет True и выполнит то, что вы в него заложили
# @dp.message_handler(Text(equals='отмена', ignore_case=True))
# Тут тоже самое Берется функция "Text" вылавливает там "отмена" и игнорирует регистр, т.е. может быть написано "ОтМеНа"


@dp.message_handler(lambda message: message.text.startswith('такси'))
async def ufo(message: types.Message):
    await message.answer(message.text[6:])
# Этот декоратор находит слово такси и выдет все что после него написал пользователь.
# Из примера выше если написать "такси 250", то он вернет "250", т.к. такси плюс пробел это будет 6 знаков


@dp.message_handler()
async def emty(message: types.Message):
    await message.answer('Нет такой команды')
    await message.delete()


executor.start_polling(dp, skip_updates=True)
