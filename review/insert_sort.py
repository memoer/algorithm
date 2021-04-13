from random import randint

arr = [randint(0, 100) for _ in range(10)]
sorted_arr = [arr.pop(0)]
for _ in range(len(arr)):
    print(sorted_arr)
    item = arr.pop(0)
    pushed = False
    for i in range(len(sorted_arr)):
        if sorted_arr[i] > item:
            pushed = True
            sorted_arr.insert(i, item)
        if pushed:
            break
    if not pushed:
        sorted_arr.append(item)
print(sorted_arr)
