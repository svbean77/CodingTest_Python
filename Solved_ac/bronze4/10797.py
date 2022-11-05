#10797 10부제

day = int(input())
car = list(map(int, input().split()))

while(day in car):
    car.remove(day)

print(5 - len(car))