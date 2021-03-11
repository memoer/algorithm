import random


def swap(arr, a_idx, b_idx):
    arr[a_idx], arr[b_idx] = arr[b_idx], arr[a_idx]


def s_sort(arr: [int]) -> None:
    for i in range(len(arr) - 1):
        minimum_idx = i
        for j in range(i + 1, len(arr)):
            if arr[minimum_idx] > arr[j]:
                minimum_idx = j
        if minimum_idx != i:
            swap(arr, i, minimum_idx)


data = [random.randint(0, 100) for _ in range(0, 5)]
print(data)
s_sort(data)
print(data)

