import random


def q_sort(data):
    if len(data) <= 1:
        return data
    left, right = [], []
    pivot = data.pop(len(data) // 2)
    for item in data:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return q_sort(left) + [pivot] + q_sort(right)


arr = random.sample(range(100), 10)
print(arr)
print(q_sort(arr))

