# 복습
for _ in range(int(input())):
    result = 0
    n, m = map(int, input().split())
    docs = [
        (priority, False if idx != m else True)
        for idx, priority in enumerate(map(int, input().split()))
    ]
    while True:
        if max(docs)[0] > docs[0][0]:
            docs.append(docs.pop(0))
        else:
            result += 1
            printed_doc = docs.pop(0)
            if printed_doc[1]:
                print(result)
                break
