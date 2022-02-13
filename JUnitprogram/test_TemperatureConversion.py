import pytest

# def fahrenheit(celsius):
    
#     fahrenheit = (celsius * 1.8) + 32


# def celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9 
# print('%0.1f degree  Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit,celsius))

# celsius = int(input('Enter celsius value you want to convert in Fahrenheit'))
# fahrenheit(celsius)
# print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
# fahrenheit = int(input('Enter Fahrenheit value you want to convert in celsius'))
# celcius(fahrenheit)
# print('%0.1f degree  Fahrenheit is equal to %0.1f degree Celsius' %(fahrenheit,celsius))
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

