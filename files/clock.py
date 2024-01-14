from bot_prhases import make_prhase, say
from settings import user_name
import asyncio

async def timer(a, b):
    for i in range(a, 0, -1):
        for ii in range(60, -1, -1):
            await asyncio.sleep(1)
    for ii in range(b - 1, -1, -1):
            await asyncio.sleep(1)
            
    make_prhase(f"Время вышло {user_name}!", "timeout")
    say("timeout")

    task = asyncio.create_task(timer(a, b))
    await task
