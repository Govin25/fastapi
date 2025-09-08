from fastapi import FastAPI
from typing import Optional

app = FastAPI()


books_list = [
    {"name": "geeta", "id": 1}, 
    {"name": "ramayan", "id": 2},
     {"name": "mahabharat", "id": 3}, 
    {"name": "abc", "id": 4},
     {"name": "athurved", "id": 5}, 
    {"name": "rigved", "id": 6},
     {"name": "samved", "id": 7}, 
    {"name": "yajurved", "id": 8}
]

@app.get("/books")
def get_limit_book(skip: int = 0, limit: Optional[int] = 5):
    return books_list[skip: skip+limit]


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_list:

        if book["id"]==book_id:

            return book["name"]
        
    return "book is not found"


    

    

