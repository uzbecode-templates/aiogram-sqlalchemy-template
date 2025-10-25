from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update as sql_update, delete as sql_delete

class ORMbase:
    def __init__(self, model, session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, **filters):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def create(self, **data):
        obj = self.model(**data)
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, filters: dict, values: dict):
        stmt = sql_update(self.model).filter_by(**filters).values(**values)
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete(self, **filters):
        stmt = sql_delete(self.model).filter_by(**filters)
        await self.session.execute(stmt)
        await self.session.commit()
