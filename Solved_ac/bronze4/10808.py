#10808 알파벳 개수

word = input()

lst = []

for c in range(ord('a'), ord('z') + 1):
    cnt = word.count(chr(c))
    lst.append(cnt)

for item in lst:
    print(item, end = ' ')
