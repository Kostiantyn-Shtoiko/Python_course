from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Viktoria",
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Roman",
    }]


@app.get(
    "/books",
    tags=["Books"],
    summary="Get all books",
)
def read_books():
    return books

@app.get(
    "/books/{id}",
    tags = ["Books"],
    summary = "Get one books",
)
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


class NewBook(BaseModel):
    title: str
    author: str
@app.post(
    "/books",
    tags = ["New Book"],
)
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Book created successfully!"}





if __name__ == "__main__":
    uvicorn.run("Rest_Api:app", reload=True)