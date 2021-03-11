'''
 - 탐욕의 알고리즘은 일종의 `전략`이라고 생각하면 된다. -

1. 동전 문제
 - 지불해야 하는 값이 4720원 일때, 1원 / 50원 / 100원 / 500원 동전으로 동전의 수가 가장 적게 지불하시오.
 - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
 - 탐욕 알고리즘으로 매 순간 최적이라고 생각되는 경우를 선택하면 된다.
'''
# 동전의 개수를 최대한 작게 하려면 가장 큰 동전의 개수를 가장 많게 해주어야 한다. -> 500원의 동전 개수가 제일 많아야 한다는 것.
money = 4720
coin_list = [1, 500, 50, 100]


def calculate(money: int, coin_list: list):
  coin_list.sort(reverse=True)
  number_of_coins = dict()
  for coin in coin_list:
    number = money // coin
    number_of_coins[coin] = number
    money -= coin * number
  return number_of_coins


print(calculate(money, coin_list))
