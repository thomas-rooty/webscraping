import uvicorn
from fastapi import FastAPI

# Description
description = """
This is a simple API that returns the square of a number.
"""

app = FastAPI(
    title="My First API",
    description=description,
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/square")
async def square(num: int):
    return {"square": num ** 2}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
