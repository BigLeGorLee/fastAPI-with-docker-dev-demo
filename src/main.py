from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# sleep = lambda sec: promise(
#     lambda resolve, reject:
#         time.sleep(sec * 1000)
#         resolve()
# )

async def genMsg():
    await asyncio.sleep(1)
    getMsg = lambda : "Hello World"

    return getMsg

@app.get("/")
async def root():
    getMsg = await genMsg()
    return { "message": getMsg() }
