number = int(input("Enter number:"))
i = 0
result = 0
while result < number:
    result = 1<<i
    if result == number:
        print('power of two',i)
    i = i + 1
    
else:
        print('enter number is not power of two')
               
             