from fastapi import FastAPI
from data import en_uz, uz_en

app = FastAPI()


@app.get("/")
async def home_page():
    return {"message": "EN / UZ lang endpoint"}


@app.get("/uz_en/{name}")
async def uz_ens(name: str):
    data = uz_en(name)
    return {"EN": data}


@app.get("/en_uz/{name}")
async def en_uzs(name: str):
    data = en_uz(name)
    return {"UZ": data}
