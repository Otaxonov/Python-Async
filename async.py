import asyncio
from time import perf_counter
from asyncio import sleep

async def write():
    print('Hey')
    await sleep(1)
    print('there')

async def main():
    await asyncio.gather(
        write(), write(), write(), write(), write()
    )

if __name__ == '__main__':

    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()

    elapsed = end - start
    print(f'Executed in {elapsed:.2f} seconds.')
