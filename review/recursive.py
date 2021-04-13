def multiple(n: int) -> int:
    return n * multiple(n - 1) if n > 2 else 2


print(multiple(5))


def sum(arr: list) -> int:
    if len(arr) == 0:
        return 0
    return arr.pop() + sum(arr)


def sum_2(arr: list) -> int:
    if len(arr) <= 1:
        return arr[0]
    return arr[0] + sum(arr[1:])


print(sum([1, 2, 3, 4, 5]))


def palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])


print(palindrome("aceffeca"))


def p_1(n: int) -> int:
    print(n)
    if n == 1:
        return n
    return p_1(3 * n + 1 if n % 2 == 1 else n // 2)


p_1(3)


def p_2(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 7
    return p_2(n - 1) + p_2(n - 2) + p_2(n - 3)


print(p_2(6))


def pibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return pibonacci(n - 1) + pibonacci(n - 2)


print(pibonacci(4))