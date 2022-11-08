#10818 최소, 최대

N = int(input())

lst = list(map(int, input().split()))

#방법 1
#print(min(lst), max(lst))

#방법 2
#lst.sort()
#print(lst[0], lst[-1])

#방법 3
minimum = lst[0]
maximum = lst[0]

for i in range(1, N):
    if lst[i] > maximum:
        maximum = lst[i]
    if lst[i] < minimum:
        minimum = lst[i]

print(minimum, maximum)