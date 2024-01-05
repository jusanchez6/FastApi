from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hello World!"

@app.get("/url")
async def root():
    return {"url_curso": "https://platzi.com/cursos/fastapi/"}

