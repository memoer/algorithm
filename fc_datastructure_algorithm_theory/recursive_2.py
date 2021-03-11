def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


def multiple(n):
    if n == 2:
        return 2
    return n * multiple(n - 1)


# ! 확인
def isPalindrome(str):
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return False


def func_1(n):
    print(n)
    if n == 1:
        return n
    func_1(3 * n + 1 if n % 2 == 1 else n // 2)


# ! 확인
def func_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return func_2(n - 1) + func_2(n - 2) + func_2(n - 3)


print(sum(10))
print(multiple(4))
print(isPalindrome("level"))
print(func_1(3))
print(func_2(5))

