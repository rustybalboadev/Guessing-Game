import os
import random
number = 0
count = 0
x = input("Do you want the computer to pick a number or another player? say \"computer\" or say \"player\" ").lower()
if x == 'player':
    number = int(input("What number do you want them to guess? "))
    os.system("clear")
    guess = int(input("What do you think the number is? "))
    while guess != number:
        if guess < number:
            print ("Guess Higher")
            guess = int(input("What do you think the number is? "))
            count += 1
        elif guess > number:
            print ("Guess Lower")
            guess = int(input("What do you think the number is? "))
            count += 1
    print ("You guessed the number correctly! The number was {0} and it took you {1} ".format(number, count))
elif x == 'computer':
    smallest_number = int(input("Smallest number for the computer to pick from "))
    largest_number = int(input("Largest number for the computer to pick from "))
    computer_number = random.randint(smallest_number, largest_number)
    guess = int(input("What do you think the number is? "))
    while guess != computer_number:
        if guess < computer_number:
            print ("Guess Higher")
            guess = int(input("What do you think the number is? "))
            count += 1
        elif guess > number:
            print("Guess Lower")
            guess = int(input("What do you think the number is? "))
            count += 1
    print("You guess the number correctly! The number was {0} and it took you {1} tries".format(computer_number, count))