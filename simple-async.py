import asyncio

async def main():
    print("starting main")
    await asyncio.sleep(1)
    print("completed main")

asyncio.run(main())