# the same code using Pool from multiprocessing
import time
from multiprocessing import Pool, cpu_count
import os


def factorize(number):
    lst = []
    for i in range(1, number + 1):
        if number % i == 0:
            lst.append(i)
    return lst


if __name__ == "__main__":

    start_time = time.time()
    numbers = [128, 255, 99999, 10651060]
    cpuCount = os.cpu_count()
    print(f"Number of CPUs in the system: {cpuCount}")
    with Pool(processes=2) as pool:  # can use cpuCount
        results = pool.map(factorize, numbers)
    print(results)

    end_time = time.time()
    total_time = end_time - start_time
    print("Exercution time: ", total_time)
