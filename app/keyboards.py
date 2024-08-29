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

read_meme_part1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ЧИТАТЬ СТАТЬЮ", url="https://t.me/KKrypty/1920")]
])

read_meme_part2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ЧИТАТЬ СТАТЬЮ", url="https://teletype.in/@neekketh/ulitimate_memecoins_guide_pt2")]
])

warp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="ЧИТАТЬ СТАТЬЮ", url="https://teletype.in/@tovarishrijiy/warpcast")]
])

warp_view = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="СМОТРИ ВИДЕО", url="https://www.youtube.com/watch?v=D9Km1Vy3o5A")]
])
number_taken = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Далее", callback_data='next-article-4')]
])

video_warp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="СМОТРИ ВИДЕО", url="https://www.youtube.com/watch?v=D9Km1Vy3o5A")]
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
        InlineKeyboardButton(text='Сколько денег нужно для старта в крипте?', callback_data='how-much-money')
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


req_contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)],
    [KeyboardButton(text='Пропустить')]
], resize_keyboard=True)




del_keyboard = ReplyKeyboardRemove()