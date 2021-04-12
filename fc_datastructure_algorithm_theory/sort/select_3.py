from random import randint

sample = [randint(1, 100) for _ in range(0, 10)]


def s_sort(arr: list) -> list:
    for i in range(len(arr)):
        minum_idx = arr.index(min(arr[i:]))
        if minum_idx != i:
            arr[minum_idx], arr[i] = arr[i], arr[minum_idx]
    return arr


sorted_arr = s_sort(sample)
print(sorted_arr