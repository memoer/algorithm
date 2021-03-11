import random

data_list = [1, 2, 3, 4, 5]
print(data_list[:2])  # 0, 1
print(data_list[2])  # 2
print(data_list[3:])  # 3,4
#
def divide(arr: [int]):
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if pivot < arr[i]:
            right.append(arr[i])
        else:
            left.append(arr[i])
    return left + [pivot] + right


print("-")
data_list_2 = [4, 1, 2, 5, 7]
print(divide(data_list_2))
#
print("-")
data_list_3 = random.sample(range(100), 10)
left = []
right = []
pivot = data_list_3[0]
for i in range(1, len(data_list_3)):
    if pivot > data_list_3[i]:
        left.append(data_list_3[i])
    else:
        right.append(data_list_3[i])
print(data_list_3)
print(left)
print([pivot])
print(right)
#
def quick_sort(arr: [int]):
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return left + [pivot] + right


data_list_4 = [4, 3, 2]
print(quick_sort(data_list_4))
