# Используйте асинхронный подход.

import asyncio
import time
from random import randint

sum = 0
array = [randint(1, 100) for i in range(1_000_000)]


async def increment(array):
    global sum
    for i in array:
        sum += i
    print(f"Значение счетчика: {sum:_} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    min = 0
    max = 1_999_999
    for i in range(5):
        task = asyncio.create_task(increment(array[min:max]))
        tasks.append(task)
        min += 2_000_000
        max += 2_000_000
    await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == '__main__':
    asyncio.run(main())
    print(f"Значение счетчика в финале: {sum:_}")
