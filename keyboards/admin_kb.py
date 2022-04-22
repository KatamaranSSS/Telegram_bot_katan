from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки клавиатуры админа
button_load = KeyboardButton('Загрузить')
button_delete = KeyboardButton('Удалить')
button_menu = KeyboardButton('Меню')
button_cancel = KeyboardButton('Отмена загрузки')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
            .insert(button_delete).add(button_menu).add(button_cancel)
