import app.keyboards as kb
import app.database.requests as rq


from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile

router = Router()


#Begin
@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message.chat.type == "private":
        text = 'Привет! Чтобы активировать бота подпишись на наши <a href="https://t.me/TestFolderLinks">ресурсы</a>!'
        await message.answer(text, parse_mode="HTML",
                             disable_web_page_preview=True,
                             reply_markup=kb.settings)

#Check sub
@router.message(F.text == 'Проверить')
async def check_subscription(message: types.Message):
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

#Get phone number
@router.callback_query(F.data == 'next-article-3')
async def next_article_3(callback: CallbackQuery):
    text = "У нас осталось для тебя еще несколько бесплатных подарков - чтобы их получить отправь свои контакты.\n"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.req_contact
                                  )
#Processing phone
@router.message(F.contact)
async def contact_callback(message: types.Message):
    await rq.set_tgid_and_number(message.from_user.id, int(message.contact.phone_number))
    await message.answer("Номер получен", reply_markup=kb.del_keyboard)
    await message.answer(text="Спасибо, вот твой <a href='#'>подарок</a>!", parse_mode="HTML",
                         reply_markup=kb.next_art_4)

#Skip write number
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
    text = "Мы решили скупить доступ во ВСЕ приватные телеграмм сообщества в СНГ для своего комьюнити. Общая стоимость доступа в приватные каналы составляет 1.000.000 рублей /мес\n" \
            "\n" \
            "Члены нашего приватного сообщества получают доступ к этой информации, совершенно бесплатно.\n" \
            "Если у тебя есть желание стать профи в крипте, но ты не можешь позволить стать членом нашего закрытого сообщества. \n" \
            "\n" \
            "Мы придумали для тебя решение! \n" \
            "\n" \
            "<b>ВСЕГО ЗА 39$</b> \n" \
           "\n" \
           "Ты можешь приобрести доступ ко всем закрытым телеграмм сообществам. \n"
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

@router.callback_query(F.data == 'suit-me')
async def show_reviews(callback: CallbackQuery):
    text = "Текст. Подойдет ли?"
    await callback.message.answer(text, parse_mode="HTML",
                                  reply_markup=kb.suit_me)


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