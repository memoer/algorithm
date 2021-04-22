# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-1074%EB%B2%88-Z-1-Python
n, r, c = map(int, input().split())
result = 0
while n > 1:
    ran = 2 ** (n - 1)
    if r >= ran:
        if c >= ran:
            result += 3 * (4 ** (n - 1))
            r -= ran
            c -= ran
        else:
            result += 2 * (4 ** (n - 1))
            r -= ran
    else:
        if c >= ran:
            result += 1 * (4 ** (n - 1))
            c -= ran
        else:
            pass
    n -= 1

if r == 0:
    if c == 0:
        print(result)
    else:
        print(result + 1)
else:
    if c == 0:
        print(result + 2)
    else:
        print(result + 3)
