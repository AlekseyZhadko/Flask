import asyncio

import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

urls = ['https://waksoft.susu.ru/',
        'https://gb.ru/',
        'https://habr.com/ru/all/',
        'https://www.google.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        ]


def get_all_images(url):
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Получено изображение"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        urls.append(img_url)
    return urls


def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join(pathname, url.split("/")[-1])
    progress = tqdm(response.iter_content(1024), f"Загружен {filename}", total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def main(url, path):
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)


async def download_images(url):
    dir = url.replace('https://', '').replace('.', '_').replace('/', '')
    print(dir)
    main(url, dir)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

start_time = time.time()


async def main_asyncio():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_images(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == '__main__':
    asyncio.run(main_asyncio())



