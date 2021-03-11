from random import randint

arr = [randint(0, 100) for _ in range(10)]


def i_sort(data: list) -> list:
    for i in range(1, len(data)):
        target = arr[i]
        if arr[i - 1] < target:
            continue
        while i > 0 and target < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = target
    return data


print(i_sort(arr))