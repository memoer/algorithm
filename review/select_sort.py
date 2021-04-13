from random import randint

arr = [randint(0, 100) for _ in range(10)]
for i in range(len(arr) - 1):
    print(arr)
    sort_arr = arr[i:]
    minimum_num = min(sort_arr)
    idx = sort_arr.index(minimum_num) + i
    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)