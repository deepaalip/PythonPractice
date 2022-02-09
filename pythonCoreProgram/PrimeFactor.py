#find prime factors
number = int(input("Enter any Number for calculating the prime factors: "))
i = 1
 
while(i <= number):
    counter = 0
    if(number % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                counter = counter + 1
            j = j + 1
             
        if (counter == 2):
            print(i)
    i = i + 1
