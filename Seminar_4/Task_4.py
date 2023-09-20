import threading
import os

PATH = 'parser_url'
count = 0


def get_amount_words(filename: str) -> None:
    global count
    with open(filename, encoding='utf-8') as f:
        count += len(f.read().split())
        print(count)



threads = []
for root, dirs, files in os.walk(PATH):
    for filename in files:
        file_path = os.path.join(root, filename)
        thread = threading.Thread(target=get_amount_words, args=(file_path,))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
