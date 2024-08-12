import random

from fastapi import FastAPI, Depends

from src.schemas import SPassword


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello"}


@app.post("/new_password/")
async def password(password: SPassword = Depends()):
    chars229 = list("qwertyuiopasdfghjklzxcvbnm")
    if password.nums == True:
        chars229.extend(list("1234567890"))
    if password.symbols == True:
        chars229.extend(list("!@#$%"))
    if password.registry == True:
        chars229.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    fpassword = "".join(random.choice(chars229) for _ in range(password.len))

    return {"success": True, "data": fpassword}
