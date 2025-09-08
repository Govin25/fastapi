from fastapi import FastAPI
from users import router as user_router
from books import router as book_router
#from borrow import router as borrow_router 

app = FastAPI(title="library api ")

app.include_router(user_router)
app.include_router(book_router)
#app.include_router(borrow_router)

