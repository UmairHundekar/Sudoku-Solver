import time
import random
import pygame

from allboards import *

boardone = random.choice(boardsList)


#Printing board
def printboard(board):
    colCounter = 3
    rowCounter = 0
    print("#########################")
    for i in board:
        if rowCounter == 3:
            rowCounter = 1
            print("#########################")
        else:
            rowCounter += 1
        for l in i: 
            if colCounter==3:
                colCounter=1
                print("|", end = " ")
            else:
                colCounter += 1
            print(l, end = ' ')
        print("|", end="")
        print(" ")
    print("#########################")


#Change value of a position 
def changenumber(board, row, col, newnumber):
    board[row][col] = newnumber

    

printboard(boardone)

def square(x, y, numlist, boardones):
    square = []
    # Row 1
    if x < 3:
        if y < 3:
            for col in list(range(3)):
                for row in list(range(3)):
                    square.append((row, col)) 
                    
        elif y < 6:
            for col in list(range(3, 6)):
                for row in list(range(3)):
                    square.append((row, col))
            

        elif y < 9:
            for col in list(range(6, 9)):
                for row in list(range(3)):
                    square.append((row, col))

    #Row 2
    elif x >= 3 and x <= 5:
        if y < 3:
            for col in list(range(3)):
                for row in list(range(3, 6)):
                    square.append((row, col))

        elif y < 6:
            for col in list(range(3, 6)):
                for row in list(range(3, 6)):
                    square.append((row, col))

        elif y < 9:
            for col in list(range(6, 9)):
                for row in list(range(3, 6)):
                    square.append((row, col))
    #Row 3
    elif x >= 6 and x <= 8:
        if y < 3:
            for col in list(range(3)):
                for row in list(range(6, 9)):
                    square.append((row, col))

        elif y < 6:
            for col in list(range(3, 6)):
                for row in list(range(6, 9)):
                    square.append((row, col))

        elif y < 9:
            for col in list(range(6, 9)):
                for row in list(range(6, 9)):
                    square.append((row, col))
    else:
        print("does not work")
    
    for coord in square:

        if boardones[coord[0]][coord[1]] in numlist:
            numlist.remove(boardones[coord[0]][coord[1]])
    return numlist

def possible(x, y, boardones):
    onetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if boardones[x][y] == 0:
 
        for numRow in boardones[x]:
            if numRow in onetonine:
                onetonine.remove(numRow)
 
        for numCol in range(9):
            if boardones[numCol][y] in onetonine:
                onetonine.remove(boardones[numCol][y])

    onetonine = square(x, y, onetonine, boardones)

    return onetonine

def solve(boardones, x=0, y=0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    time.sleep(0.1)
    boardx = 20
    boardy = 18
    screen.blit(board, (0, 0))
    for row in boardone:
        for col in row:
            number = font.render(str(col), True, BLACK)
            screen.blit(number, (boardx, boardy))
            boardx+=50
        boardy+=46
        boardx = 20
    pygame.display.flip()
    #Checking if board solved
    if 0 not in boardones[8]:
        return True
    #Checking if square is empty
    if boardones[x][y] != 0:
        if y==8:
            if solve(boardones, x+1, 0) == True:
                return True
        else:
            if solve(boardones, x, y+1) == True:
                return True
    else:            
        if boardones[x][y] == 0:    

            possibleMoves = possible(x, y, boardones)
            if possibleMoves==[]:
                return False
            for j in possibleMoves:
                
                changenumber(boardones, x, y, j)
                if y==8:
                    if solve(boardones, x+1, 0) == True:
                        return True
                else:
                    if solve(boardones, x, y+1) == True:
                        return True
                changenumber(boardones, x, y, 0)









pygame.init()

BLACK = (0, 0, 0)


screen = pygame.display.set_mode([453, 435])
pygame.display.set_caption('Sudoku')
board = pygame.image.load("sudoku-blankgrid.png")






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.fill((255, 255, 255))
    font = pygame.font.Font("ARIALBD.ttf", 25)
    
    x = 20
    y = 18
    screen.blit(board, (0, 0))
    for row in boardone:
        for col in row:
            number = font.render(str(col), True, BLACK)
            screen.blit(number, (x, y))
            x+=50
        y+=46
        x = 20
    pygame.display.flip()
    solve(boardone)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        x = 20
        y = 18
        screen.blit(board, (0, 0))
        for row in boardone:
            for col in row:
                number = font.render(str(col), True, BLACK)
                screen.blit(number, (x, y))
                x += 50
            y += 46
            x = 20


    pygame.display.flip()