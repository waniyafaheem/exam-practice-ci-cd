import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL =  os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)
session = AsyncSession(engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)