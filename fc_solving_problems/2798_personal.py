n, m = list(map(int, input().split()))
card_list = sorted(list(map(int, input().split())), reverse=True)
candidate_set = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            s = card_list[i] + card_list[j] + card_list[k]
            if s <= m:
                candidate_set.add(s)
print(sorted(list(candidate_set), reverse=True)[0])