import random

def main():

    print "Welcome to guess the number"
    print "I'm thinking of a number, you have to guess what it is."

    num = random.randrange(100)
    guess = ""
    print num

    while guess != num:
        guess = int(raw_input("Take a guess: "))
        if guess < num:
            print "Guess higher next time\n"
        elif guess > num:
            print "Guess lower next time\n"
    print "!!***CONGRATULATIONS***!!"
    raw_input()
    if insults == "yes":
        file.close()

main()  

