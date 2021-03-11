# 수 문제

n = int(input())
# set 은 집합을 표현하기 위해 사용된다. [ 중복 제거 ]
# 특정한 정수가 어떠한 리스트에 포함되고 있는 지만을 체크한다면
arr_n = set(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

for m in arr_m:
    if m in arr_n:
        print("1")
    else:
        print("0")
