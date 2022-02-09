import random

stake = input('Enter number of stake gambler has:')
goal = input('Enter gamblers desired bankroll:')
trials = input('Enter number of trials gambler perform:')

bets = 0       
wins = 0 

for i in trials:
    cash = int(stake)
    while (cash > 0 and cash < int(goal)):
        bets += 1
        if random.randint(0,1) < 0.5:
            cash += 1
        else:
            cash -= 1
            if cash == goal:
                wins += 1
                
        print(int(wins),int(trials))
        print("Percent of games won = ",int(100.0) * int(wins) / int(trials))
        print("Avg bets = " ,int(1.0) * int(bets) / int(trials))
    


                
            