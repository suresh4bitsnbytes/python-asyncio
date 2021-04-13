import asyncio
import time

async def print_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    print(f"started at {time.strftime('%X')}")

    await print_after(2, "Suresh")
    await print_after(1, "Kumar")

    print(f"Ended at {time.strftime('%X')}")
asyncio.run(main())