from random import randint

arr = [randint(0, 100) for _ in range(10)]


def quick(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    pivot = arr.pop(center)
    left,right = list(),list()
    for item in arr:
        if item > pivot:
            right.append(item)
        else:
            left.append(item)
    return quick(left) + [pivot] + quick(right)


print(quick(arr))