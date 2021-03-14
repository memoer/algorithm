n = int(input())
result = []
for _ in range(n):
    x, y = map(int, input().split())
    result.append((x, y))

# ! 파이썬 기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬을 한다.
# ! 기본적으로 오름차순 정렬 -> key 속성을 설정해주지 않았을 경우
result.sort()
for x, y in result:
    print(x, y)
