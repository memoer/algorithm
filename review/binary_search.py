from random import randint

arr = [chr(randint(0, 30)) for _ in range(10)]


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    pivot = arr.pop(center)
    left, right = list(), list()
    for item in arr:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


def binary_search(arr: list, search: str) -> bool:
    center = len(arr) // 2
    center_num = ord(arr[center])
    search_num = ord(search)
    if len(arr) <= 1:
        return center_num == search_num
    return binary_search(arr[:center] if center_num > search_num else arr[center:], search)


sorted_list = quick_sort(list(map(lambda x: ord(x), arr)))
chr_list = list(map(lambda x: chr(x), sorted_list))
print(binary_search(chr_list, "F"))


def temp(arr: list, search: int, idx=0) -> int:
    center = len(arr) // 2
    center_num = arr[center]
    if search >= center_num:
        idx += center
    if center_num == search or len(arr) <= 1:
        return center_num == search, idx if center_num == search else -1
    return temp(arr[:center] if search < center_num else arr[center:], search, idx)


print(sorted_list)
print(temp(sorted_list, 12))