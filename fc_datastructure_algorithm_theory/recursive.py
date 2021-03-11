from random import sample


def sum(n):
  if n == 1:
    return 1
  return n+sum(n-1)


def multiple(n):
  if n == 1:
    return 1
  return n*multiple(n-1)


def sum_list(list):
  if len(list) == 1:
    return list[0]
  return list[0] + sum_list(list[1:])


def isPalindrome(str):
  if len(str) <= 1:
    return True
  if str[0] == str[-1]:
    return isPalindrome(str[1:-1])
  return False


def func1(n):
  print(n, end=", ")
  if n == 1:
    print()
    return n
  elif n % 2 == 0:
    return func1(int(n/2))
  else:
    return func1(3*n+1)


def func2(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  return func2(n-1)+func2(n-2)+func2(n-3)


print(f'sum\t\t: {sum(10)}')
print(f'multiple\t: {multiple(10)}')
tmp_list = sample(range(10), 5)
print(f'sum_list\t: {tmp_list} -> {sum_list(tmp_list)}')
print(f'isPalindrome\t: {isPalindrome("level")}')
func1(6)
print(func2(5))
