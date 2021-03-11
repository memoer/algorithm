import random


def merge_and_sort(left: [int], right: [int]):
    merged = []
    lp, rp = 0, 0
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        else:
            merged.append(left[lp])
            lp += 1
    if len(left) <= lp:
        merged += right[rp:]
    elif len(right) <= rp:
        merged += left[lp:]
    return merged


def split(arr: [int]):
    if len(arr) <= 1:
        return arr
    center_idx = len(arr) // 2
    return merge_and_sort(split(arr[:center_idx]), split(arr[center_idx:]))


data = random.sample(range(100), 10)
print(data)
print(split(data))
