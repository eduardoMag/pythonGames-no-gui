import random
import sys


def drawboard(board):
    # draw the board data structure
    hline = " "
    for i in range(1, 6):
        hline += (" " * 9) + str(i)

        # print the numbers across the top
        print(hline)
        print(" " + ('0123456789' * 6))
        print()

        # print each of the 15 rows
        for i in range(15):
            # single-digit numbers need to be padded with an extra space
            if i < 10:
                extraSpace = ' '
            else:
                extraSpace = ''
            print('%s%s %s %s') % (extraSpace, i, getRow(board, i), i)

        # print across the bottom
        print()
        print(' ' + ('0123456789' * 6))
        print(hline)


def getRow(board, row):
    # return string from the board data structure at a certain row
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow


def getNewBoard():
    # create a new 60X15 board data structure
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
        return board


def getRandomChests(numChests):
    # create a list of chest data structures
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests


def isValidMove(x, y):
    return 0 <= x <= 59 and 0 <= y <= 14


def makeMove(board, chests, x, y):
    if not isValidMove(x, y):
        return False

    smallestDistance = 100
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)

        if distance < smallestDistance:
            smallestDistance = distance

        if smallestDistance == 0:
            chests.remove([x, y])
            return 'You have found a sunken treasure chest!'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return 'treasure detected at a distance of %s from the sonar device.' % smallestDistance
            else:
                board[x][y] = 'O'
                return 'Sonar did not detect anything. All treasures chests are out range.'


def enterPlayerMove():
    print('Where do you want to drop the next sonar device? ' + '(0-59 0-14) ' + '(or type quit)')
    while True:
        move = input()

        if move.lower() == 'quit':
            print('Thank you for playing.')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print("Enter a number from 0 to 59, a space, then a number from 0 to 14")


def playAgain():
    print("Do you want to play again? " + "(yes or no)")
    return input().lower().startswith('y')


def showInstructions():
    print("INSTRUCTIONS:"
          "you are the captain of the Gold-Digger, a treasure-hunting ship.\n"
          "your current mission is to find the three sunken treasure chests that are lurking in the part of the "
          "ocean you are in and collect them. \n"
          "To play, enter the coordinates of the point in the ocean you wish to drop a sonar device.\n"
          "The sonar can find out how far away the closest chest is to it.\n"
          "For example, the d below marks where the device was dropped.\n"
          "The 2's represent distances of 2 away from the device. the 4's represent distances of 4 away from device.\n"
          "     444444444\n"
          "     4       4\n"
          "     4 22222 4\n"
          "     4 2   2 4\n"
          "     4 2 d 2 4\n"
          "     4 2   2 4\n"
          "     4 22222 4\n"
          "     4       4\n"
          "     444444444\n"
          "Press enter to continue...")
    input()
    print("For example, here is a teasure chest (the c) located a distance of 2 away from the sonar device (the d):\n"
          "     22222\n"
          "     c   2\n"
          "     2 d 2\n"
          "     2   2\n"
          "     22222\n"
          "the point where the device was dropped will be marked with a 2. The treasure chests don't move around.\n"
          "Sonar devices can detect tresure chests up to a distance of 9. if all chest are out of range, the point will be marked with 0.\n"
          "If a device is directly dropped on a tresure chest, the have discovered the location of the chest, and it will be collected.\n"
          "the sonar device will remain there. When you collect a chest, all sonar devices will update to locate the next closest sunken treasure chest.\n"
          "Press enter to continue...")
    input()
    print()


print(" S O N A R !")
print()
print("would you like to view the instructions? " + "(YES/NO)")
if input().lower().startswith('y'):
    showInstructions()

while True:
    # game setup
    sonarDevices = 16
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawboard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # start of a turn

        # sonar devices/chest status
        if sonarDevices > 1:
            extraSsonar = 's'
        else:
            extraSsonar = ''
        if len(theChests) > 1:
            extraSchest = 's'
        else:
            extraSchest = ''
        print('You have %s sonar device%s left. %s treasure chest%s remaining.') % (sonarDevices, extraSsonar, len(theChests), extraSchest)

        x, y = enterPlayerMove()
        previousMoves.append([x, y])

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
                drawboard(theBoard)
                print(moveResult)
            if len(theChests) == 0:
                print("You have found all the sunken treasure chests! CONGRATULATIONS and good game!")
                break

            sonarDevices -= 1

        if sonarDevices == 0:
            print(
                "we\'ve run out of sonar devices! Now we have to turn the ship around and head for home with treasure chests"
                "still out there! GAME OVER...")
            print("the remaining chests were here: ")
            for x, y in theChests:
                print('%s, %s') % (x, y)

        if not playAgain():
            sys.exit()
