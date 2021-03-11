n = int(input())

for _ in range(n):
    arr.append(int(input()))

# 파이썬 라이브러리 사용
# 선택/삽입정렬 복습 겸 insert_3.py / select_3.py 연습해봄
arr.sort()
print("\n".join(list(map(str, arr))))