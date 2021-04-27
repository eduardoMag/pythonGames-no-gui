import random
import sys


def drawboard(board):
    # draw the board data structure
    hline = " "
    for j in range(1, 6):
        hline += (" " * 9) + str(j)

        # print the numbers across the top
        print(hline)
        print(" " + ('0123456789' * 6))
        print()

        # print each of the 15 rows
        for j in range(15):
            # single-digit numbers need to be padded with an extra space
            if j < 10:
                extraSpace = ' '
            else:
                extraSpace = ''
            print('%s%s %s %s') %(extraSpace, j, getRow(board, j), j)

        # print across the bottom
        print()
        print(' ' + '0123456789' * 6)
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
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


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
            return 'You have found a sunken treasure chest!!!'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return ('treasure detected at a distance of %s from the sonar device.') %smallestDistance
            else:
                board[x][y] = print('Where do you want to drop the next sonar device? (0-59 0-14)')
                return ('Sonar did not dect anything. All treasures chests are out range.')

def enterPlayerMove():
    print('Where do you want to drop the next sonar device? ' + '(0-59 0-14) ' + '(or type quit)')
    while True:
        move = input()

        if move.lower() == 'quit':
            print('Thank you for playing.')
            sys.exit()
