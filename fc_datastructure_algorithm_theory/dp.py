# 동적 계획법 - Memoization


def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


def fibo_dp(num):
    # Memoization -> 저장, 해당 결과값을 이용해서 상위 문제를 해결
    cache = [0 for index in range(num + 1)]
    # 가장 작은 부분 문제들을 해결
    cache[0] = 0
    cache[1] = 1
    for index in range(2, num + 1):
        # 해당 부분 문제의 해를 활용하여 보다 큰 크기의 부분 문제를 해결
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]
