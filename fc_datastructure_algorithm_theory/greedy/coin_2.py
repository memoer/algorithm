pay_amount = 4720
coin_list = [500, 100, 50, 1]
coin_number_dict = {500: 0, 100: 0, 50: 0, 1: 0}
result = 0

for coin in coin_list:
    coin_number_dict[coin] = pay_amount // coin
    pay_amount = pay_amount % coin
for coin in coin_number_dict:
    result += coin * coin_number_dict[coin]

print(pay_amount)
print(coin_number_dict)
print(result)
