from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select



#поиск юзера по tg_id и создается в случае если его нет
async def set_tgid_and_number(tg_id, phone_number):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, phone=phone_number))
            await session.commit()




