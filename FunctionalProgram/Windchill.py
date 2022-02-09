import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v,0.16)

print('the windchill index is:',w)