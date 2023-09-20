import multiprocessing
import os
from multiprocessing.context import Process

PATH = 'parser_url'
counter = multiprocessing.Value('i', 0)


def get_amount_words(filename: str, cnt) -> None:
    with open(filename, encoding='utf-8') as f:
        with cnt.get_lock():
            cnt.value += len(f.read().split())
        print(cnt.value)


processes = []

if __name__ == '__main__':
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            process = Process(target=get_amount_words, args=(file_path, counter))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
