# 스택수열
# 반드시 오름차순
# 강의 코드
n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1):
    data = int(input())
    # 스택의 마지막 값보다 큰 값이 입력되었다면 -> 해당 값까지 push
    while count <= data:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == data:
        # 스택의 구조는 반드시 오름차순
        # 마지막 값은 스택에서 가장 큰 값
        # 해당 값은 pop을 할 수 있음
        stack.pop()
        result.append("-")
    else:
        # 마지막 같이 스택에서 가장 큰 값
        # 해당 값보다 작은 게 입력 되었다면 -> 오름차순 push가 아니게 됨
        print("NO")
        exit(0)

print("\n".join(result))
