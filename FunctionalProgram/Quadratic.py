import cmath
def getRootOfQuadraticEquation(a, b, c): 
 delta = (int(b*b) - (4*a*c))

root1_Of_x = (-b + cmath.sqrt(delta))/(2*a)
root2_Of_x = (-b - cmath.sqrt(delta))/(2*a)
print("Solution to the equation are:",root1_Of_x,root2_Of_x)

a = int(input('Enter value of a:'))
b = int(input('Enter  value of b:'))
c = int(input('Enter  value of c:'))
getRootOfQuadraticEquation(a, b, c)