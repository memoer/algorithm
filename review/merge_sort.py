from random import randint

arr = [randint(0, 100) for _ in range(8)]


def sort(left: list, right: list) -> list:
    merged = list()
    if not left:
        return right
    elif not right:
        return left
    while len(left) != 0 and len(right) != 0:
        if min(left) < min(right):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged += left if len(left) != 0 else right
    return merged


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    left, right = merge_sort(arr[:center]), merge_sort(arr[center:])
    return sort(left, right)


print(merge_sort(arr))