from typing import Annotated
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, mapped_column, Mapped
from fastapi import FastAPI, HTTPException, Depends

import uvicorn

app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///books.db')


new_session = AsyncSession(engine, expire_on_commit=False)


async def get_session():
    async with new_session as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str] 


@app.post("/setup_database", tags=["Setup Database"])
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"success": True, "message": "Database setup completed!"}


class BookAddSchema(BaseModel):
    title: str
    author: str

class BookSchema(BookAddSchema):
    id: int

@app.post("/books", tags=["Books"])
async def add_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title, 
        author=data.author
    )
    session.add(new_book)
    await session.commit()
    return {"success": True, "message": "Book added successfully!"}



@app.get("/books", tags=["Books"])
async def get_books(session: SessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()



if __name__ == "__main__":
    uvicorn.run("Database_FastApi:app", reload=True)
