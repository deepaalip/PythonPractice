
import math

x1 = int(input("Enter the First Point Coordinate x1 = "))
y1 = int(input("Enter the First Point Coordinate y1  = "))

x = math.pow((x1), 2)
y = math.pow((y1), 2)

print(x)
print(y)
print(math.sqrt(x + y))
distance = math.sqrt(x + y)

print('The Distance Between Two Points = {0} Units'.format(distance))