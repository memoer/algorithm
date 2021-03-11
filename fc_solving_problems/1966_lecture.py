n = int(input())
result = []
for _ in range(n):
    n, m = list(map(int, input().split()))
    docs = [(value, idx) for idx, value in enumerate(list(map(int, input().split())))]
    count = 0
    while True:
        if docs[0][0] == max(docs, key=lambda x: x[0])[0]:
            count += 1
            if docs[0][1] == m:
                print(count)
                break
            else:
                docs.pop(0)
        else:
            docs.append(docs.pop(0))