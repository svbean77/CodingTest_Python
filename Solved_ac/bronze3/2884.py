#2884 알람 시계

H, M = map(int, input().split())

if M < 45:
    H = (H - 1 + 24) % 24

M = (M - 45 + 60) % 60

print(H, M)
