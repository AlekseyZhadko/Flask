import multiprocessing
import time
from multiprocessing.context import Process
from random import randint

sum = multiprocessing.Value('i', 0)
array = [randint(1, 100) for i in range(1_000_000)]


def increment(array, sum):
    for i in array:
        with sum.get_lock():
            sum.value += i
    print(f"Значение счетчика: {sum.value:_} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    min = 0
    max = 1_999_999
    for i in range(5):
        process = Process(target=increment, args=(array[min:max], sum))
        processes.append(process)
        process.start()
        min += 2_000_000
        max += 2_000_000

    for process in processes:
        process.join()
    print(f"Значение счетчика в финале: {sum.value:_}")
