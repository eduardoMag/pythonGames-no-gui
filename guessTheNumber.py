import random

guessTaken = 0

print ('Hello, lets playa game...')
print ('what is your name?')
myName = input()

number = random.randint(1 ,20)
print ('Well, ' +myName + ', I am thinking of a number between 1 and 20.')

while guessTaken < 6:
    print('take a guess')
    guess =input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print ('your guess was too low try again, muahaha.')

    if guess > number:
        print ('your guess was too high try agian, hehehe...')

    if guess == number:
        break
if guess == number:
    guessTaken = str(guessTaken)
    print('good job, ' + myName + '! you were able to guess my number in ' + guessTaken + ' guesses!')

if guess != number:
    number =str(number)
    print('you failed my game... ')
    print('the number i was thinking about was ' + number)
        
