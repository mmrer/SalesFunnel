import app.keyboards as kb
import app.database.requests as rq


from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile

router = Router()


#начало
@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message.chat.type == "private":
        text = 'Привет! Чтобы активировать бота подпишись на наши <a href="https://t.me/addlist/rlH9GFsdWsowZThi">ресурсы</a>!'
        await message.answer(text, parse_mode="HTML",
                             disable_web_page_preview=True,
                             reply_markup=kb.settings)

#проверка на подписку
@router.message(F.text == 'Проверить')
async def check_subscription(message: types.Message):
    chat_id_list = ["-1002234927815"]
    #нужно добавить id групп и добавить бота в администраторы каналов/пабликов
    status_channel_list = []

    for chat_id in chat_id_list:
        chat_member = await message.bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if chat_member.status != 'left':
            status_channel_list.append("+")
        else:
            status_channel_list.append("-")
    if "-" in status_channel_list:
        text = 'Для продолжения необходимо добавить <a href="https://t.me/addlist/rlH9GFsdWsowZThi">папку</a> с ресурсами.'
        await message.answer(text, parse_mode="HTML",
                             disable_web_page_preview=True,
                             reply_markup=kb.settings
                             )
    else:
        await message.answer(text="Добро пожаловать!", reply_markup=kb.del_keyboard)
        text ="Лови полезнейший гайд как заработать на новом тренде криптовалюты МЕМЕ КОИНЫ!" \
                "Мы с командой уже умножили свой капитал в 10, 20 и даже 100 раз! Подтверждение на картинках выше!" \
                "Хочешь так-же? Тогда обязательно прочти \n<a href='https://t.me/KKrypty/1920'>ЭТУ СТАТЬЮ!</a>"
        await message.answer(text, parse_mode="HTML",
                             reply_markup=kb.next_art_2,
                             )

@router.callback_query(F.data == 'next-article-2')
async def next_article_2(callback: CallbackQuery):
    text = "Не хочешь вкладывать большие деньги в криптовалюту и заработать первый капитал? У нас есть решение для тебя! " \
        "Потребуется всего 500 рублей, чтобы начать свой путь к успеху здесь и сейчас! Лови полезнейший видео-гайд для начала работы в криптовалюту!\n" \
        "<a href='https://t.me/KKrypty/1920'>статья про варпкаст</a>"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_3
                                  )

#запрос телефона
@router.callback_query(F.data == 'next-article-3')
async def next_article_3(callback: CallbackQuery):
    text = "У нас осталось для тебя еще несколько бесплатных подарков - чтобы их получить отправь свои контакты.\n"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.req_contact
                                  )
#обработка телефона
@router.message(F.contact)
async def contact_callback(message: types.Message):
    await rq.set_tgid_and_number(message.from_user.id, int(message.contact.phone_number))
    await message.answer("Номер получен", reply_markup=kb.del_keyboard)
    await message.answer(text="Спасибо, вот твой <a href='#'>подарок</a>!", parse_mode="HTML",
                         reply_markup=kb.next_art_4)

#пропуск ввода
@router.message(F.text == "Пропустить")
async def skip_send_number(message: types.Message):
    await message.answer(text="Ввод пропущен", reply_markup=kb.del_keyboard)
    text = "Отлично теперь ты знаешь как зарабатывать в вапркасте - теперь давай создадим твой " \
            "первый аккаунт - \n<a href='#'>видео про варпкаст</a>"
    await message.answer(text, parse_mode="HTML",
                         reply_markup=kb.next_art_5)

@router.callback_query(F.data == 'next-article-4')
async def next_article_4(callback: CallbackQuery):
    text = "Отлично теперь ты знаешь как зарабатывать в вапркасте - теперь давай создадим твой " \
           "первый аккаунт - \n<a href='#'>видео про варпкаст</a>"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_5)

@router.callback_query(F.data == 'next-article-5')
async def next_article_5(callback: CallbackQuery):
    text = "Бро да ты уже почти профи в крипте. Лови еще один подарок от нас"
    await callback.message.answer(text, parse_mode="HTML")
    video = FSInputFile(path="app/animation/crypto-crypto.mp4")
    await callback.message.answer_video_note(video_note=video,
                                             reply_markup=kb.next_art_6)

@router.callback_query(F.data == 'next-article-6')
async def next_article_6(callback: CallbackQuery):
    text = "<a href='#'>статья</a>"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_7)

@router.callback_query(F.data == 'next-article-7')
async def next_article_7(callback: CallbackQuery):
    text = "Ни для кого не секрет, что главным инструментом для заработка денег в криптовалюте является инфополе!\n" \
            "Мы готовы предоставить тебе наш уникальный инструмент для заработка в криптовалюте стоимостью более 5000$!\n" \
            "Всего за 29$! + БОНУС ДОСТУП К БИБЛИОТЕКЕ ЗНАНИЙ ПО ВСЕЙ КРИПТЕ В нём собраны самые лучшие приватные сообщества СНГ!\n" \
            "Владея таким инфополем заработает каждый!"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.next_art_8)

@router.callback_query(F.data == 'next-article-8')
async def next_article_8(callback: CallbackQuery):
    text = "Закрываем отрицание людей\nПочему ты еще не с нами?\n" \
        "Но возможно, что у тебя остались вопросики.\n" \
        "Выбери тот, который тебя интересует, и я отправлю тебе персональный ответ:\n" \
        "\n" \
        "1. Сколько денег нужно для старта в крипте? - пост\n" \
        "2. А есть ли у вас отзывы ? - переход на отзовик\n" \
        "3. Подойдет ли это конкретно мне? - 1 конкретный кейс (который закрывает боли большинства нормисо = они должны увидеть себя в этом кейсе)\n" \
        "\n" \
        "Нажми на цифру интересующего вопроса 👇👇"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.choice_question)