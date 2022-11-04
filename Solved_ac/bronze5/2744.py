#2744 대소문자 바꾸기

word = input()

for i in range(len(word)):
    if word[i].islower():
        print(word[i].upper(), end = '')
    else:
        print(word[i].lower(), end = '')