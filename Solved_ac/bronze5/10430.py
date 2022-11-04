#10430 나머지

A, B, C = map(int, input().split())

result1 = (A+B)%C
result2 = ((A%C)+(B%C))%C
result3 = (A*B)%C
result4 = ((A%C)*(B%C))%C

print(f'{result1}\n{result2}\n{result3}\n{result4}')