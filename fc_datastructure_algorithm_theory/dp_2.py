def fibo(num):
    if num <= 1:
        return num
    # 하향식
    return fibo(num - 1) + fibo(num - 2)


print(fibo(5))


def fibo_dp(num):
    # 상향식
    cache = [0 for _ in range(0, num + 1)]
    cache[0] = 0
    cache[1] = 1
    for i in range(2, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num]


print(fibo_dp(6))
