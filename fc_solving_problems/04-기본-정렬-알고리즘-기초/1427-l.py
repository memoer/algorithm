# 소트인사이드
# 각 자리수를 내림차순
# 2143 -> 4321
string = input()

for i in range(9, -1, -1):
    for j in string:
        if int(j) == i:
            print(j, end="")
