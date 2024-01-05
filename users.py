from fastapi import FastAPI

app = FastAPI()


#Iniciar el servidor con uvicorn mediante el comando:
# uvicorn users:app --reload

@app.get("/")

async def users():
    return "¡Hello users!"