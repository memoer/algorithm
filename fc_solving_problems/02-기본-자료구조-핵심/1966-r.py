# 복습
test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    docs = [(priority, idx) for (idx, priority) in enumerate(map(int, input().split()))]
    count = 0
    while True:
        if docs[0][0] < max(docs, key=lambda x: x[0])[0]:
            docs.append(docs.pop(0))
        else:
            count += 1
            item = docs.pop(0)
            if item[1] == m:
                print(count)
                break