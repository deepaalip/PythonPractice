import math
def calculateTemp_speed(v,t):
   w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v,0.16)
   print('the windchill index is:',w)
   
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
calculateTemp_speed(v,t)