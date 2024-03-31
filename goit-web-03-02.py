import time
import os

cpuCount = os.cpu_count()
print("Number of CPUs in the system:", cpuCount)
start_time = time.time()


def factorize(*number):
    result_lst = []
    for num in number:
        lst = []
        for i in range(1, num + 1):
            if num % i == 0:
                lst.append(i)
        result_lst.append(lst)
    return result_lst


end_time = time.time()
print(end_time - start_time)


a, b, c, d = factorize(128, 255, 99999, 10651060)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]



