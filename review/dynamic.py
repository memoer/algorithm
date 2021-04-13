def fibo_dp(num: int) -> int:
    data = [0, 1, 1, 2, 3]
    if num < len(data):
        return data[num]
    while True:
        data.append(data[-1] + data[-2])
        if num + 1 == len(data):
            return data[-1]


print(fibo_dp(10))
