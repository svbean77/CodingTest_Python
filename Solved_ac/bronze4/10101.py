#10101 삼각형 외우기

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

sum = angle1 + angle2 + angle3
setAngle = {angle1, angle2, angle3}

if len(setAngle) == 1 and angle1 == 60:
    result = 'Equilateral'
elif sum == 180 and len(setAngle) == 2:
    result = "Isosceles"
elif sum == 180 and len(setAngle) == 3:
    result = "Scalene"
else:
    result = "Error"

print(result)