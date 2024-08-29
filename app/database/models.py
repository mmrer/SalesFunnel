from sqlalchemy import BigInteger, String, ForeignKey, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv('SQLALCHEMY_URL'))

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    phone: Mapped[int] = mapped_column(BigInteger)

#class Contact(Base):
    #__tablename__ = 'contacts'

    #id: Mapped[int] = mapped_column(primary_key=True)
    #email: Mapped[str] = mapped_column(String(50))
    #phone: Mapped[int] = mapped_column()
    #user: Mapped[int] = mapped_column(ForeignKey('users.id'))

#запуск движка и создание таблиц
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


