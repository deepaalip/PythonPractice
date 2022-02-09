from random import randint

heads = 0
tails = 0

flip = int(input("how many coin tosses are you going to do?"))

for i in range(flip):
    result = randint(0, 1)
    if result < 0.5:
        print("Tails")
        tails += 1
    else:
        print("Heads")
        heads += 1
    print("the results are:")
    print("Heads",heads)
    print("Tails",tails)
            