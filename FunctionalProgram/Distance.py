import math
def findDistance(point_x1,point_y1):

          x = math.pow((point_x1), 2)
          y = math.pow((point_y1), 2)

          print(x)
          print(y)
          print(math.sqrt(x + y))
          distance = math.sqrt(x + y)
          
          print('The Distance Between Two Points = {0} Units'.format(distance))
    
point_x1 = int(input("Enter the First Point Coordinate x1 = "))
point_y1 = int(input("Enter the First Point Coordinate y1  = "))

findDistance(point_x1, point_y1)

   
