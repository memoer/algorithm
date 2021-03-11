import random
from time import time


def q_sort(arr: [int]):
    if len(arr) <= 1:
        return arr
    center_idx = len(arr) // 2
    pivot = arr.pop(center_idx)
    left, right = [], []
    for item in arr:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    return q_sort(left) + [pivot] + q_sort(right)


def binary_search(data: [int], find_num: int, previous_idx: int = 0) -> int:
    if len(data) <= 1:
        if data[0] == find_num:
            return previous_idx
        else:
            return -1
    center_idx = len(data) // 2
    if data[center_idx] < find_num:
        return binary_search(data[center_idx + 1 :], find_num, previous_idx + center_idx + 1)
    elif data[center_idx] > find_num:
        return binary_search(data[:center_idx], find_num, previous_idx)
    else:
        return previous_idx + center_idx


sample = [10, 24, 39, 7, 3, 15, 34, 99, 22, 44]
sorted_sample = q_sort(sample)

