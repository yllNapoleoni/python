from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI(title="Book Library API")

# Define our Data Model using Pydantic
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    is_read: bool = False

# In-memory "database" (a simple list)
books_db = []

# --- CRUD Endpoints ---

# CREATE
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    # Check if ID already exists
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book

# READ (All books)
@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db

# UPDATE
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, b in enumerate(books_db):
        if b.id == book_id:
            # Ensure the ID in the payload matches the URL path
            if updated_book.id != book_id:
                raise HTTPException(status_code=400, detail="Cannot change book ID")
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, b in enumerate(books_db):
        if b.id == book_id:
            del books_db[index]
            return {"message": f"Book {book_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")