def resolve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    resolve(n / 2, x, y)
    resolve(n / 2, x, y + n / 2)
    resolve(n / 2, x + n / 2, y)
    resolve(n / 2, x + n / 2, y + n / 2)


result = 0
N, X, Y = map(int, input().split())
resolve(2 ** N, 0, 0)