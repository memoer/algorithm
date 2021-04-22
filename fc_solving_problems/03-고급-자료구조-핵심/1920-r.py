n = input()
a_list = set(sorted(input().split()))
m = input()
b_list = input().split()

for i in b_list:
    if i in a_list:
        print("1")
    else:
        print('0')
