import random


def swap(arr, a_idx, b_idx):
    arr[a_idx], arr[b_idx] = arr[b_idx], arr[a_idx]


def b_sort(arr: [int]) -> None:
    for i in range(len(arr) - 2):
        isSwapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                isSwapped = True
                swap(arr, j, j + 1)
        if not isSwapped:
            break


data = [random.randint(0, 100) for i in range(0, 5)]
b_sort(data)
print(data)
