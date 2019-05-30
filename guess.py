import random
def guess():
    mynum = random.randint(1, 10)
    usernum = 0
    numguess = 0
    while (usernum != mynum) and (numguess < 3):
        print("Please enter a number between 1 and 10:")
        usernum = int(input())
        numguess += 1
        if usernum > mynum:
            print("Your number is too high")
        elif usernum < mynum:
            print("Your number is too low")
        else:
            print("You got it right!")
    if usernum != mynum:
        print("You ran out of guesses!")

guess()