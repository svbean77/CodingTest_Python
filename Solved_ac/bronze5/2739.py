#2739 구구단

N = int(input())

print("***** format 1 *****")
for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')

print("***** format 2 *****")
for i in range(1, 10):
    print('%d * %d = %d' % (N, i, N * i))

print("***** format 3 *****")
for i in range(1, 10):
    print('{0} * {1} = {2}'.format(N, i, N * i))