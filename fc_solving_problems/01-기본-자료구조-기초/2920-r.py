data = list(map(int, input().split()))
ascending = False
descending = False
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        ascending = True
    else:
        descending = True
if ascending and descending:
    print('mixed')
elif ascending:
    print('ascending')
else:
    print("descending")