import threading
import time
from random import randint

sum = 0
array = [randint(1, 100) for i in range(1_000_000)]


def increment(array):
    global sum
    for i in array:
        sum += i
    print(f"Значение счетчика: {sum:_} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()

min = 0
max = 1_999_999
for i in range(5):
    t = threading.Thread(target=increment, args=[array[min:max]])
    threads.append(t)
    t.start()
    min += 2_000_000
    max += 2_000_000

for t in threads:
    t.join()
print(f"Значение счетчика в финале: {sum:_}")

