n = int(input())

for _ in range(n):
    count = 0
    n, idx = list(map(int, input().split()))
    docs = [(priority, i) for i, priority in enumerate(list(map(int, input().split())))]
    while True:
        if docs[0][0] < max(docs, key=lambda t: t[0])[0]:
            docs.append(docs.pop(0))
        else:
            count += 1
            if docs.pop(0)[1] == idx:
                print(count)
                break
