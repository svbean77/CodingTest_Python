#4153 직각삼각형

while True:
    lst = list(map(int, input().split()))
    lst.sort()
    if (lst[0] == 0) & (lst[1] == 0) & (lst[2] == 0):
        break

    if(pow(lst[-1], 2) == pow(lst[0], 2) + pow(lst[1], 2)):
        print('right')
    else:
        print('wrong')