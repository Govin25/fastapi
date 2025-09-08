from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/books", tags=["books"])

books=[]

class Book(BaseModel):
    id:int
    name:str
    author:str
    available:bool = True

@router.post("/" ,response_model = Book)
def add_book(book:Book):
    books.append(book.dict())
    return book

@router.get("/",response_model=list[Book])
def get_book():
    return books
