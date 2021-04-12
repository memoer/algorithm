a, b, c = map(int, input().split())
minimum_num = min([a, b, c])
i = 1
while True:
    i += 1
    temp = minimum_num * i
    if temp % a == 0 and temp % b == 0 and temp % c == 0:
        break
print(temp)