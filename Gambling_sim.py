import random
input("Welcome to Gambling sim!!! Lets start making bets!!! Goal of game : get 5 hundred dollars. press anything to continue")
my_money = 10
run = True
while my_money < 500 and run == True:
    number = input("Flip a coin!!! Bet if it will be on heads or tails. Type H/T. ")
    if number == 'H':
        number = 1
    elif number == 'T':
        number = 2
    else:
        input("oi type a valid input. For putting an invalid input, Ill punish you by causing you to lose your bet.")
    randomnum = random.randint(1,2)
    if randomnum == number:
        print(f"You won your bet!!! You earned {my_money:.2f} dollars!!!")
        my_money *=2
        print(f"You now have {my_money:.2f} dollars. ")
    else:
        print(f"Aww, you lost your bet. You lost {my_money-my_money/2.1:.2f} dollars")
        my_money /=2.1
        print(f"You now have {my_money:.2f} dollars. ")
        if my_money < 0.01:
            print("You went bankrupt and lost!!! Try again. ")
            run = False
if  my_money > 500:
    print("YOU WERE LUCKY AND WON!!!")
