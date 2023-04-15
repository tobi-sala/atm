import random
#guessing game
lower = int(input("Enter what you want the lowest number to be: "))
upper = int(input("Enter what you want the highest number to be: "))
hid_num = random.randint(lower, upper)
chances = ((upper/10)+2)
print("you have only ",chances," chances to guess the corect number\n")
count = 0
while count < chances:
    count += 1
    guess = int(input("Guess a number: "))
    if hid_num == guess:
        print("Congrats!!! you did it in ",count," try")
        break
    elif hid_num > guess:
        print("You guessed too small")
    elif hid_num < guess:
        print("You guessed too high")
if count >= chances:
    print("\n The number is ",  hid_num)
    print("\tBetter luck next time")
