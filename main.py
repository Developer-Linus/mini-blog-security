# FastAPI app
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_home():
    return "Welcome to mini app blog."
