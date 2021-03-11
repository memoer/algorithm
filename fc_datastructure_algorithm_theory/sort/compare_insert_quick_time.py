import random
from time import time


def quick_sort(arr: [int]):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = [], []
    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


def insert_sort(arr: [int]):
    for i in range(1, len(arr)):
        target = arr[i]
        if target > arr[i - 1]:
            continue
        while i > 0 and target < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = target
    return arr


data_list = random.sample(range(100000), 10000)

m_start_time = time()
insert_sort(data_list)
m_process_time = time() - m_start_time

# q_start_time = time()
# quick_sort(data_list)
# q_process_time = time() - q_start_time

print(m_process_time)
