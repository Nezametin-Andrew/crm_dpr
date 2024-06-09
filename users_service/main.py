import asyncio
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def main():
    return {"response": "Welcome to the User Service"}

