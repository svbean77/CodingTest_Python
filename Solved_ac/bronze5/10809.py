#10809 알파벳 찾기

word = input()

for alphabet in range(ord('a'), ord('z') + 1):
    idx = word.find(chr(alphabet))
    print(idx, end = ' ')