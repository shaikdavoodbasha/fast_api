from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books =[
  {
    "id": 1,
    "title": "Python Basics",
    "author": "John Smith",
    "price": 299,
    "available": True
  },
  {
    "id": 2,
    "title": "FastAPI Guide",
    "author": "Emily Johnson",
    "price": 499,
    "available": True
  },
  {
    "id": 3,
    "title": "Backend Development",
    "author": "Michael Brown",
    "price": 699,
    "available": False
  },
  {
    "id": 4,
    "title": "Data Structures in Python",
    "author": "David Lee",
    "price": 399,
    "available": True
  },
  {
    "id": 5,
    "title": "API Design Principles",
    "author": "Sophia Wilson",
    "price": 550,
    "available": True
  }
]

app = FastAPI()

@app.get("/book")
def get_book():
    return books

@app.get('/book/{book_id}')
def get_book(book_id:int):
    for book in books:
        if book['id'] ==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
#adding data to data
class Book(BaseModel):
    id:int
    title:str
    author:str
    price:int
    available:bool

@app.post('/book')
def create_book(book:Book):
    newbook =  book.model_dump() #used to converts binary models into dictionaries
    books.append(newbook)

class BookUpdate(BaseModel):
    title:str
    author:str
    price:int

@app.put("/book/{book_id}")
def update_book(book_id:int,book_update : BookUpdate):
    for book in books:
        if(book['id']== book_id):
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['price'] = book_update.price
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

# @app.delete("/book/{book_id}")
# def delete_book(book_id:int):
#     for book in books:
#         if(book['id'] == book_id):
#             books.remove(book)
#         return {'Message':'Books has deleted'}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")