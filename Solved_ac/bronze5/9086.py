#9086 문자열

T = int(input())

for _ in range(T):
    string = input()
    print(f'{string[0]}{string[len(string)-1]}')