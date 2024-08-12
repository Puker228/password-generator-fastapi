

from fastapi import FastAPI

from src.router import router as password_router


app = FastAPI()
app.include_router(password_router)


@app.get("/")
async def home():
    return {"message": "hello"}



