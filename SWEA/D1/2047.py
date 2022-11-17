#2047 신문 헤드라인

content = input()

for item in content:
    if item.isalpha():
        print(item.upper(), end = '')
    else:
        print(item, end = '')