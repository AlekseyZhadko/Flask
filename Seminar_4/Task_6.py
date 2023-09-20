# Используйте асинхронный подход.

import asyncio
import os

PATH = 'parser_url'

count = 0

async def get_amount_words(filename: str):
    global count
    with open(filename, encoding='utf-8') as f:
        count += len(f.read().split())
    print(count)


async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            task = asyncio.create_task(get_amount_words(file_path))
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
