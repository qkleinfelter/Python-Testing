# Used to generate random number
import random
# File handling
import os

num_tries = 0
min_num = 0
max_num = 0

def guess():
    print("Entered guess")
    mynum = random.randint(min_num, max_num)
    usernum = 0
    numguess = 0
    # Do this until user gets it right or they max out guesses
    while (usernum != mynum) and (numguess < num_tries):
        print("Please enter a number between " + str(min_num) + " and " + str(max_num) + ":")
        usernum = int(input())
        numguess += 1
        if usernum > max_num:
            print("Your number is over the limit!")
            numguess -= 1
        elif usernum < min_num:
            print("Your number is under the limit!")
            numguess -= 1
        elif usernum > mynum:
            print("Your number is too high")
        elif usernum < mynum:
            print("Your number is too low")
        else:
            print("You got it right!")
    # If we broke out of the loop and the numbers aren't the same we know they ran out of guesses
    if usernum != mynum:
        print("You ran out of guesses!")

def check_config():
    if os.path.isfile(os.path.join("./guess.conf")):
        # Read it in
        print("File Found")
        config = open("./guess.conf", "r")
        conf_lines = config.readlines()
        global num_tries
        global min_num
        global max_num
        num_tries = int(conf_lines[0].split("=")[1].strip())
        min_num = int(conf_lines[1].split("=")[1].strip())
        max_num = int(conf_lines[2].split("=")[1].strip())
        if min_num > max_num:
            print("Invalid config! Using default values!")
            min_num = 1
            max_num = 10

    else:
        # Default Configuration
        config = open("guess.conf", "w")
        config.write("num_tries = 3\n")
        config.write("min_num = 1\n")
        config.write("max_num = 10\n")

check_config()
guess()
