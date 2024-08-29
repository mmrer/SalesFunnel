import time

import app.keyboards as kb
import app.database.requests as rq


from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile

router = Router()


#Begin
@router.message(Command("start"))
async def cmd_start(message: types.Message, bot: Bot) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message.chat.type == "private":
        await bot.send_photo(message.chat.id, photo="https://i.ibb.co/CvcYXnT/welcome.jpg", caption="")
        text = "<b>Привет 👋 Это команда Курим Крипту</b>\n\n" \
            "После прохождения бота ты узнаешь :\n\n" \
            "• Как зарабатывать на мем-коинах в крипте и умножить свой капитал в 100 раз.\n\n" \
            "• Как зарабатывать деньги, просто переписываясь в социально сети Warpcast без вложений.\n\n" \
            "• Как уволиться с работы и стать профессианальным инвестором в криптовалюту.\n\n" \
            "• Как сколотить свой первый капитал за 2024-2025 год.\n\n" \
            "Интересно? Тогда погнали!\n\n " \
            "Чтобы активировать бота подпишись на все наши - <a href='https://t.me/TestFolderLinks'>ресурсы</a>"
        await message.answer(text, parse_mode="HTML",
                             disable_web_page_preview=True,
                             reply_markup=kb.settings)


#Check sub
@router.message(F.text == 'Проверить')
async def check_subscription(message: types.Message, bot: Bot):
    chat_id_list = ["-1002216390442", "-1002234927815"]
    status_channel_list = []

    for chat_id in chat_id_list:
        chat_member = await message.bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if chat_member.status in ['administrator', 'creator', 'member']:
            status_channel_list.append("+")
        else:
            status_channel_list.append("-")

    if "-" in status_channel_list:
        text = 'Для продолжения необходимо добавить все наши <a href="https://t.me/TestFolderLinks">ресурсы</a>.'
        await message.answer(text, parse_mode="HTML",
                             disable_web_page_preview=True,
                             reply_markup=kb.settings
                             )
    else:
        await message.answer(text="Добро пожаловать!", reply_markup=kb.del_keyboard)
        await bot.send_photo(message.chat.id, photo="https://i.ibb.co/KyGBmBM/memcoin-1part.jpg", caption="")
        text ="<b>Миллионы на мем-коинах в 2024-2025 году.</b>\n\n" \
                "Инструмент который уже принес нашей команде более 20.000.000 млн рублей\n\n" \
                "<b>Читай эту статью и узнаешь:</b>\n\n" \
                "• Почему на мем-коинах зарабатываются огромные деньги? \n\n" \
                "• Что такое блокчейн Solana и почему к нему столько внимания? \n\n" \
                "• Где тороговать и покупать эти самые мем-коины?\n\n" \
                "• Как безопасно торговать\n\n"
        await message.answer(text, parse_mode="HTML",
                             reply_markup=kb.read_meme_part1)

        time.sleep(30.0)

        await bot.send_photo(message.chat.id, photo="https://i.ibb.co/8m84B2m/memcoin-2part.jpg", caption="")
        text = "<b>Миллионы на мем-коинах в 2024-2025 году Ч.2</b>\n\n" \
                "Ты уже знаешь, почему на мемах зарабатываются огромные деньги.\n\n" \
               "<b>Читай 2 часть статьи и узнаешь:</b>\n\n" \
               "• Как сделать первые 10.000$ со 100$\n\n" \
               '• Кто такие "коллеры" и для чего они нужны\n\n' \
               '• Важность нетворкинга в крипто чатах\n\n' \
               '• Что такое DEX и CEX\n\n'
        await message.answer(text, parse_mode="HTML",
                             reply_markup=kb.read_meme_part2)


        time.sleep(30.0)


        await bot.send_photo(message.chat.id, photo="https://i.ibb.co/bWqxHT8/warpcast.jpg", caption="")
        text = "<b>Нет, денег? Попроси 500 рублей у друга!</b>\n\n" \
                "Не хочешь вкладывать большие деньги в криптовалюту и заработать первый капитал? У нас есть решение для тебя! Потребуется всего 500 рублей, чтобы начать свой путь к успеху здесь и сейчас!\n\n" \
                "<b>Что ты узнаешь в этой статье?</b>\n\n" \
                "• Как зарабатывать с минимальными вложениями? \n\n" \
                "• Что такое SocialFi и Warpcast\n\n" \
                "• Почему это один из трендов нового бычьего рынка?\n\n" \
                "• Как ты мог заработать 100.000$ за лайки и коменты.\n\n"
        await message.answer(text, parse_mode="HTML",
                             reply_markup=kb.warp)

        time.sleep(30.0)


        text = "У нас осталось для тебя еще несколько бесплатных подарков - чтобы их получить отправь свои контакты.\n"
        await message.answer(text, parse_mode="HTML",
                                      reply_markup=kb.req_contact)

#Processing phone
@router.message(F.contact)
async def contact_callback(message: types.Message):
    await rq.set_tgid_and_number(message.from_user.id, int(message.contact.phone_number))
    await message.answer("Номер получен", reply_markup=kb.del_keyboard)
    await message.answer(text="Спасибо, вот твой <a href='#'>подарок</a>!", parse_mode="HTML",
                         reply_markup=kb.number_taken)

#Skip write number
@router.message(F.text == "Пропустить")
async def skip_send_number(message: types.Message, bot: Bot):
    await message.answer(text="Ввод пропущен", reply_markup=kb.del_keyboard)
    await bot.send_photo(message.chat.id, photo="https://i.ibb.co/tm0cwb6/warpcast-reg.jpg", caption="")
    text = "<b>Отлично! Вот твой видео гайд по регистрации Warpcast!</b>\n\n" \
            "Спасибо, что прочитал статью. Теперь ты знаешь, как зарабатывать деньги за общение в соц-сетях. Осталось только зарегестрировать свой первый аккаунт.\n\n "
    await message.answer(text, parse_mode="HTML",
                         reply_markup=kb.video_warp)

    time.sleep(30.0)

    await bot.send_photo(message.chat.id, photo="https://i.ibb.co/BL14GBg/last-pump.jpg", caption="")
    text = "<b>Ну что? Мой дорогой друг</b>, надеюсь ты уже понял, что зарабатывать в крипте можно и явно проще чем ходить на скучную работу 😔\n\n" \
            "Но скорее всего без правильной информации, ты не только не заработаешь, но и <b>потеряешь свои деньги</b>.\n\n" \
            "<b>Но у нас есть решение для тебя!</b>\n\n" \
            "Мы решили скупить доступ во ВСЕ приватные телеграмм сообщества в СНГ для своего комьюнити\n\n" \
            "✍️ | Общая стоимость доступа в приватные каналы составляет <b>1.000.000 рублей/мес</b> \n\n" \
            "<b>Предлагаем тебе приобрести зеркало всех СНГ приваток в одном месте</b> \n" \
            "<b>ВСЕГО ЗА 39$</b>"
    await message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_8)

@router.callback_query(F.data == 'next-article-4')
async def next_article_4(callback: CallbackQuery, bot: Bot):
    await bot.send_photo(callback.chat.id, photo="https://i.ibb.co/tm0cwb6/warpcast-reg.jpg", caption="")
    text = "<b>Отлично! Вот твой видео гайд по регистрации Warpcast!</b>\n\n" \
            "Спасибо, что прочитал статью. Теперь ты знаешь, как зарабатывать деньги за общение в соц-сетях. Осталось только зарегестрировать свой первый аккаунт.\n\n"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.video_warp)

    time.sleep(30.0)

    await bot.send_photo(callback.chat.id, photo="https://i.ibb.co/BL14GBg/last-pump.jpg", caption="")
    text = "<b>Ну что? Мой дорогой друг</b>, надеюсь ты уже понял, что зарабатывать в крипте можно и явно проще чем ходить на скучную работу 😔\n\n" \
            "Но скорее всего без правильной информации, ты не только не заработаешь, но и <b>потеряешь свои деньги</b>.\n\n" \
            "<b>Но у нас есть решение для тебя!</b>\n\n" \
            "Мы решили скупить доступ во ВСЕ приватные телеграмм сообщества в СНГ для своего комьюнити\n\n" \
            "✍️ | Общая стоимость доступа в приватные каналы составляет <b>1.000.000 рублей/мес</b> \n\n" \
            "<b>Предлагаем тебе приобрести зеркало всех СНГ приваток в одном месте</b> \n" \
            "<b>ВСЕГО ЗА 39$</b>"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_8)



@router.callback_query(F.data == 'what-can-buy')
async def next_article_8(callback: CallbackQuery):
    text = "Текст, что можно купить на 39$"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.what_can_buy)


@router.callback_query(F.data == 'show-reviews')
async def show_reviews(callback: CallbackQuery):
    text = "Отзывы"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.show_reviews)

@router.callback_query(F.data == 'how-much-money')
async def show_reviews(callback: CallbackQuery):
    text = "Текст. Сколько нужно?"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.how_much)

@router.callback_query(F.data == 'next-article-8')
async def next_article_8(callback: CallbackQuery):
    text = "Почему ты еще не с нами?\n" \
        "Но возможно, что у тебя остались вопросики.\n" \
        "Выбери тот, который тебя интересует, и я отправлю тебе персональный ответ:\n" \
        "\n" \
        "1. Сколько денег нужно для старта в крипте? - пост\n" \
        "2. А есть ли у вас отзывы ? - переход на отзовик\n" \
        "Нажми на цифру интересующего вопроса 👇👇"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.what_can_buy)