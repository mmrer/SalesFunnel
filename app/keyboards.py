#from aiogram.filters import callback_data
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardRemove)

#import emoji

settings = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text="Проверить")]
],
            resize_keyboard=True,
            one_time_keyboard=True)


next_art_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next-article-2')]
], resize_keyboard=True)

next_art_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next-article-3')]
], resize_keyboard=True)

next_art_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Далее", callback_data='next-article-4')]
])

next_art_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Далее", callback_data='next-article-5')]
])

next_art_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Далее", callback_data='next-article-6')]
])

next_art_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next-article-7')]
])

next_art_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next-article-8')]
])

choice_question = InlineKeyboardMarkup(inline_keyboard=[
    [
     InlineKeyboardButton(text='1', callback_data='next-quest-1'),
     InlineKeyboardButton(text='2', callback_data='next-quest-2'),
     InlineKeyboardButton(text='3', callback_data='next-quest-3')
    ]

], resize_keyboard=True)

req_contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)],
    [KeyboardButton(text='Пропустить')]
], resize_keyboard=True)




del_keyboard = ReplyKeyboardRemove()

