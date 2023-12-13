import uvicorn
from fastapi import FastAPI
from db import *

# Description
description = """
API that returns scraped anime from MyAnimeList.net with filters.
"""

app = FastAPI(
    title="MyAnimeAPI",
    description=description,
    version="0.0.1",
)

database = DataBase('myanimelist')


@app.get("/")
async def root():
    return {"message": "Capybara"}


@app.get("/animes")
async def get_animes():
    return database.select_table('myanimelist')


@app.get("/animes/{letter}")
async def get_animes_with_filter(letter: str):
    return database.select_anime_starts_with('myanimelist', letter)


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
