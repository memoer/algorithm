from random import randint

sample = [randint(1, 100) for _ in range(0, 10)]


def c_sort(arr: list) -> list:
    maximum_num = max(arr)
    tmp = [0 for _ in range(maximum_num + 1)]
    result = []
    for i in arr:
        tmp[i] += 1
    for i in range(len(tmp)):
        for _ in range(tmp[i]):
            result.append(i)
    return result


print(sample)
arr = c_sort(sample)
print(arr)