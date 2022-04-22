from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from bot_app.config import BOT_TOKEN

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

answ = dict()

# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)  # Тут указывается сколько кнопок будет в одном ряду
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4',
                                                                                          url='https://google.com'),
     InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))
# На метод row метод сверху не распростроняется


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки:', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),
                                             InlineKeyboardButton(text='Dislike', callback_data='like_-1'))


@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('За видео', reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосвали')
    else:
        await callback.answer('Вы уже проголосвали', show_alert=True)
    # await callback.message.answer('Нажата инлайн кнопка')#это функция отправления сообщения в чат
    # await callback.answer('Нажата инлайн кнопка', show_alert=True)#это у нас отвечает за сплывающее окно,
    # нужно остаить пустым что бы ничего не показывалось,
    # show_alert показывает всплывающее окно на котором надо нажать окей, туда помещается 200 символов
executor.start_polling(dp, skip_updates=True)
