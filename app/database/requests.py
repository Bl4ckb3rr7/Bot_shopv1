from app.database.models import User,Category,Item,Basket,async_session
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_items(category_id):
    async with async_session() as sesssion:
        return await sesssion.scalars(select(Item).where(Item.category == category_id))

async def get_item(item_id):
    async with async_session() as sesssion:
        return await sesssion.scalar(select(Item).where(Item.id == item_id))