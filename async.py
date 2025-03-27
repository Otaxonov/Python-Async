import asyncio

async def task():
    print("Hey...")
    await asyncio.sleep(1)
    print("I am here...")

asyncio.run(task())