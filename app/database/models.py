import os
from dotenv import load_dotenv
from sqlalchemy import BigInteger,String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs


load_dotenv()
engine = create_async_engine(url=os.getenv('SQLALCHEMY_URL'), echo = True) #Создания файла БД

async_session = async_sessionmaker(engine) # Переменная для подключения к БД

class Base(AsyncAttrs,DeclarativeBase): # Класс который является родительским по отношению ко всем моделям, для управления моделями
    pass

class User(Base): #Класс объекта User
    __tablename__ = 'users' # Создание таблицы users

    id: Mapped[int] = mapped_column(primary_key=True) # Колонка с типом и внутренним ключем
    tg_id = mapped_column(BigInteger) #объявили тип данных BigInteger которого нет в питоне, поэтому подтя нули с sqlalchemy

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(125))
    price: Mapped[str] = mapped_column(String(10))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

class Basket(Base):
    __tablename__ = 'basket'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item: Mapped[int] = mapped_column(ForeignKey('items.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # cоздание всех выше перечисленных таблиц