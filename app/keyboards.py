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
    [
        InlineKeyboardButton(text='Покупка подписки', callback_data='#'),
        InlineKeyboardButton(text='Что можно купить за 39$', callback_data='what-can-buy')
    ]
])

what_can_buy = InlineKeyboardMarkup(inline_keyboard=[
    [
     InlineKeyboardButton(text='Купить подписку', callback_data='#')
    ],
    [
        InlineKeyboardButton(text='Как у вас дела с отзывами? ', callback_data='show-reviews'),
        InlineKeyboardButton(text='Сколько денег нужно для старта в крипте?', callback_data='how-much-money'),
        InlineKeyboardButton(text='Подойдет ли это конкретно мне?', callback_data='suit-me')
    ]
], resize_keyboard=True)

show_reviews = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Хочу купить подписку", callback_data='want-buy')
    ],
    [
        InlineKeyboardButton(text="Сколько денег нужно для старта в крипте?", callback_data='how-much-in-ShowRev'),
        InlineKeyboardButton(text="Подойдет ли это конкретно мне?", callback_data='suit-for-me-in-ShowRev')
    ]
], resize_keyboard=True)

how_much = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Хочу купить подписку", callback_data='want-buy')
    ],
    [
        InlineKeyboardButton(text="Как у вас дела с отзывами? ", callback_data='how-with-rev-in-HowMuch'),
        InlineKeyboardButton(text="Подойдет ли это конкретно мне?", callback_data='suit-for-me-in-HowMuch')
    ]
], resize_keyboard=True)

suit_me = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Хочу купить подписку", callback_data='want-buy')
    ],
    [
        InlineKeyboardButton(text="Как у вас дела с отзывами? ", callback_data='how-with-rev-in-SuitMe'),
        InlineKeyboardButton(text="Сколько денег нужно для старта в крипте?", callback_data='how-much-in-SuitMe')
    ]
], resize_keyboard=True)


req_contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)],
    [KeyboardButton(text='Пропустить')]
], resize_keyboard=True)




del_keyboard = ReplyKeyboardRemove()

