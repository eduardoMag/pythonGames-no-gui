import random
import time


def displayIntro():
    print('you are on a planet full of dragons. infront of you,')
    print('you see two caves. in one cave, the dragon is friendly')
    print('and will share her treasure with you. the other dragon ')
    print('is greedy and hungry, and will eat you on sight.')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
        return cave


def checkCave(chosenCave):
    print('you approach the cave...')
    time.sleep(2)
    print('a large dragon jumps out in front of you! It opens its jaws and...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('gives you her treasures!')
    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
