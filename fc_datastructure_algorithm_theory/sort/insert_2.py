import random


def insert_sort(arr):
    for i in range(1, len(arr)):
        target = arr[i]
        if target > arr[i - 1]:
            continue
        while i > 0 and target < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = target


data = [random.randint(0, 100) for _ in range(0, 5)]
print(data)
insert_sort(data)
print(data)
