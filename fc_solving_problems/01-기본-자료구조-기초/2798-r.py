n, m = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum_card = card_list[i] + card_list[j] + card_list[k]
            if sum_card > result and sum_card <= m:
                result = sum_card
print(result)