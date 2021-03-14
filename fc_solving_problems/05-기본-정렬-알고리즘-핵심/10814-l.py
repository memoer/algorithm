n = int(input())

array = []

for _ in range(n):
    age, name = input().split()
    array.append((int(age), name))
# ! 나이(x[0])가 동일한 경우, 먼저 입력된 순서를 따르도록 key를 설정해주어야 한다.
array.sort(key=lambda x: x[0])

for age, name in array:
    print(age, name)