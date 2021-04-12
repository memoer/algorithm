from random import randint

sample = [randint(1, 100) for _ in range(10)]


def i_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        target = arr[i]
        if target > arr[i - 1]:
            continue
        while i > 0 and target < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = target
    return arr


print(sample)
arr = i_sort(sample)
print(arr)
