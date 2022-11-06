#1264 모음의 개수

Vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    sentence = input()
    cnt = 0
    if sentence == '#':
        break

    sentence = list(sentence)
    cnt = 0
    for item in sentence:
        if item.isalpha():
            if item.lower() in Vowels:
                cnt += 1

    print(cnt)