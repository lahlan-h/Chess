import pygame
import math
import gameManager

def choose_move(chessDict, mousePos, screenWidth, screenHeight, boardSize, possibleMoves, display):

    points = []
    distances = []

    for x in possibleMoves:
        
        tempChessDict = chessDict[(x[0], x[1])]

        xPosM = tempChessDict[3]
        yPosM = tempChessDict[4]

        #print(f'x coords: {xPosM} y coords: {yPosM}')

        coordinates = (xPosM, yPosM)
        points.append(coordinates)

    for x in points:
        distance = round(math.sqrt( ((x[0]-mousePos[0])**2)+((x[1]-mousePos[1])**2) ), 3)
        distances.append(distance)
    

    min = distances[0]

    for x in range(len(distances)):
        if (distances[x] < min):
            min = distances[x]


    index = distances.index(min)
    closestPoint = points[index]


    squareSizeX = screenWidth / boardSize
    squareSizeY = screenHeight / boardSize



    keyX = int((closestPoint[0] / squareSizeX) + 0.5)
    keyY = int((closestPoint[1] / squareSizeY) + 0.5)


    keys = (keyX, keyY)
    

    #Instead of returning x and y coordinate, instead return the key of the dictionary 
    if (mousePos[0] >= closestPoint[0] - 50 and mousePos[0] <= (closestPoint[0] + 50) and mousePos[1] >= closestPoint[1] - 50 and mousePos[1] <= closestPoint[1] + 50):
        pygame.draw.circle(display, (0, 255, 0), closestPoint, 10)
        return keys
    else:
        return False

def print_possible_points(display, possiblePointsKeys, chessDict, screenWidth, boardSize):
    
    circleRadius = (screenWidth / boardSize) / 2.2
    circleRadius2 = (screenWidth / boardSize) / 6
    #print(circleRadius2)
    
    for x in possiblePointsKeys:
        keyX, keyY = x[0], x[1]

        possiblePointDict = chessDict[(keyX, keyY)]
        possiblePointX = possiblePointDict[3]
        possiblePointY = possiblePointDict[4]

        possiblePointSquareType = possiblePointDict[5]


        
        
        if(possiblePointSquareType != 'e_'):
            #(18, 200, 99)
            pygame.draw.circle(display, (255, 18, 99), (possiblePointX, possiblePointY), circleRadius2, width = 5)
        else:
            pygame.draw.circle(display, (18, 200, 99), (possiblePointX, possiblePointY), circleRadius2)

def is_king_check():
    
    
    
    
    
    
    
    
    
    
    
    



    
    pass

#Return possibleMoves, ClickedSquareKey
def possibles_moves(clickedSquareKey, chessDict, display):
    
    possibles_moves = []

    if (clickedSquareKey != False):
        #These keys are from where the player clicked
        keyX = clickedSquareKey[0]
        keyY = clickedSquareKey[1]

        currentSquareDict = chessDict[(keyX, keyY)]
        currentSquareString = currentSquareDict[5]
        currentSquareColour = str(currentSquareString.split('_', 1)[0])

        if (currentSquareString == 'black_knight' or currentSquareString == 'white_knight'):
            knightMoves = [[-2,-1], [-2, 1], [1, -2], [-1,-2], [2, -1], [2,1], [-1, 2], [1, 2]]

            for x in knightMoves:
                newSquareDictKey = (keyX + x[0], keyY + x[1])
                
                if (newSquareDictKey[0] >= 1 and newSquareDictKey[0] <= 8 and newSquareDictKey[1] >= 1 and newSquareDictKey[1] <= 8):
                    newSquareDict = chessDict[newSquareDictKey[0], newSquareDictKey[1]]
                    newSquareString = newSquareDict[5]
                    newSquareType = newSquareString.split('_', 1)[1]
                    newSquareColour = str(newSquareString.split('_', 1)[0])

                    if (currentSquareColour == 'black'):
                        teamColour = 'black'
                    elif (currentSquareColour == 'white'):
                        teamColour = 'white'


                    if (newSquareColour != teamColour and newSquareType != 'king'):
                        newSquareDictKeys = [newSquareDictKey[0], newSquareDictKey[1]]
                        possibles_moves.append(newSquareDictKeys)
            
            
            return possibles_moves, clickedSquareKey

        elif(currentSquareString == 'black_pawn' or currentSquareString == 'white_pawn'):

            
          


            if (currentSquareColour == 'black'):
                teamColour = 'black'
                
                pawnMoves = [[0, 1]]
                conditionalMoves = [[-1, 1], [1, 1]]
                
                if (keyY == 2): 
                    testSquare = chessDict[(keyX, 3)]
                    testSquareString = testSquare[5]
                    testSquareString = testSquareString.split('_', 1)[0]

                    if (testSquareString == 'e'):
                        pawnMoves.append([0, 2])

            elif (currentSquareColour == 'white'):
                teamColour = 'white'
                
                pawnMoves = [[0, -1]]
                conditionalMoves = [[-1, -1], [1, -1]]
                
                #Include check for piece in front
                
                
                if (keyY == 7):
                    #Check 6 for piece

                    testSquare = chessDict[(keyX, 6)]
                    testSquareString = testSquare[5]
                    testSquareString = testSquareString.split('_', 1)[0]



                    if (testSquareString == 'e'):

                        pawnMoves.append([0, -2])
            
            for x in pawnMoves:

                newSquareDictKey = (keyX + x[0], keyY + x[1])

                
                if (newSquareDictKey[0] >= 1 and newSquareDictKey[0] <= 8 and newSquareDictKey[1] >= 1 and newSquareDictKey[1] <= 8):
                    
                    #This is responsible for calculating diagonal moves
                    for y in conditionalMoves:
                        
                        new_ConditionalSquareDictKey = (keyX + y[0], keyY + y[1])

                        if (new_ConditionalSquareDictKey[0] >= 1 and new_ConditionalSquareDictKey[0] <= 8 and new_ConditionalSquareDictKey[1] >= 1 and new_ConditionalSquareDictKey[1] <= 8):
                            new_ConditionalSquareDict = chessDict[new_ConditionalSquareDictKey]
                            
                            new_ConditionalSquareString = new_ConditionalSquareDict[5]
                            new_ConditionalSquareStringType = new_ConditionalSquareString.split('_', 1)[0]
                            new_ConditionalSquareType = new_ConditionalSquareString.split('_', 1)[1]

                            print(f'Type: {new_ConditionalSquareType}')

                            if (new_ConditionalSquareStringType != teamColour and new_ConditionalSquareStringType != 'e' and new_ConditionalSquareType != 'king'):
                                #Possibly Return Check
                                
                                
                                possibles_moves.append([keyX + y[0], keyY + y[1]])

                    
                    #THIS IS FOR MOVING PIECE FORWARD (CHECKING)
                    newSquareDict = chessDict[newSquareDictKey[0], newSquareDictKey[1]]
                    newSquareString = newSquareDict[5]
                    newSquareColour = newSquareString.split('_', 1)[0]

            

                    if (newSquareColour != teamColour and newSquareColour == 'e'):
                        newSquareDictKeys = [newSquareDictKey[0], newSquareDictKey[1]]
                        possibles_moves.append(newSquareDictKeys)
                    
            
            #print(possibles_moves)
            return possibles_moves, clickedSquareKey


        elif(currentSquareString == 'black_rook' or currentSquareString == 'white_rook'):

            rookMoves = []
            
            #Data Type: currentSquareColour

            
            #For Testing Purposes its KeyX = 4 and KeyY = 5
            coordinates = (keyX, keyY)


            up_check_finished = False
            down_check_finished = False
            left_check_finished = False
            right_check_finished = False
            
            upCoord = (coordinates[0] + 0, coordinates[1] - 1)
            downCoord = (coordinates[0] + 0, coordinates[1] + 1)
            leftCoord = (coordinates[0] -1, coordinates[1] + 0)
            rightCoord = (coordinates[0] + 1, coordinates[1] + 0)
            
            #If inbetween 0 and 8

            while (upCoord[1] <= 8 and upCoord[1] >= 1 and up_check_finished == False):

                upCoordDict = chessDict[(upCoord)]
                upCoordString = upCoordDict[5]
                upCoordColour = upCoordString.split('_', 1)[0]
                upCoordType = upCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                #or teamColour != upCoordColour
                if (upCoordColour == 'e'):

                    rookMoves.append(upCoord)
                    upCoord = (upCoord[0], upCoord[1] - 1)

                    if (upCoord[1] < 1):
                        up_check_finished = True
                
                elif (upCoordColour != 'e'):
                   
                    if (upCoordColour != teamColour and upCoordType != 'king'):
                        
                        rookMoves.append(upCoord)
                        up_check_finished = True
                    
                    break
            
            
            while (downCoord[1] <= 8 and downCoord[1] >= 1 and down_check_finished == False):

                downCoordDict = chessDict[(downCoord)]
                downCoordString = downCoordDict[5]
                downCoordColour = downCoordString.split('_', 1)[0]
                downCoordType = downCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (downCoordColour == 'e'):


                    rookMoves.append(downCoord)
                    downCoord = (downCoord[0], downCoord[1] + 1)

                    if (downCoord[1] > 8):
                        down_check_finished = True
                
                elif (downCoordColour != 'e'):
                   
                    if (downCoordColour != teamColour and downCoordType != 'king'):
                        
                        rookMoves.append(downCoord)
                        down_check_finished = True
                    
                    break

            while (leftCoord[0] <= 8 and leftCoord[0] >= 1 and left_check_finished == False):

                leftCoordDict = chessDict[(leftCoord)]
                leftCoordString = leftCoordDict[5]
                leftCoordColour = leftCoordString.split('_', 1)[0]
                leftCoordType = leftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (leftCoordColour == 'e'):


                    rookMoves.append(leftCoord)
                    leftCoord = (leftCoord[0] - 1, leftCoord[1])

                    if (leftCoord[0] < 1):
                        left_check_finished = True
                
                elif (leftCoordColour != 'e'):
                   
                    if (leftCoordColour != teamColour and leftCoordType != 'king'):
                        
                        rookMoves.append(leftCoord)
                        left_check_finished = True
                    
                    break

            while (rightCoord[0] <= 8 and rightCoord[0] >= 1 and right_check_finished == False):

                rightCoordDict = chessDict[(rightCoord)]
                rightCoordString = rightCoordDict[5]
                rightCoordColour = rightCoordString.split('_', 1)[0]
                rightCoordType = rightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (rightCoordColour == 'e'):


                    rookMoves.append(rightCoord)
                    rightCoord = (rightCoord[0] + 1, rightCoord[1])

                    if (rightCoord[0] < 1):
                        right_check_finished = True
                
                elif (rightCoordColour != 'e'):
                   
                    if (rightCoordColour != teamColour and rightCoordType != 'king'):
                        
                        rookMoves.append(rightCoord)
                        right_check_finished = True
                    
                    break            

    
            return rookMoves, clickedSquareKey


        elif(currentSquareString == 'black_bishop' or currentSquareString == 'white_bishop'):
            
            bishopMoves = []

            coordinates = (keyX, keyY)

            upRight_check_finished = False
            upLeft_check_finished = False
            downRight_check_finished = False
            downLeft_check_finished = False
            
            upRightCoord = (coordinates[0] + 1, coordinates[1] - 1)
            upLeftCoord = (coordinates[0] -1, coordinates[1] - 1)
            downRightCoord = (coordinates[0] + 1, coordinates[1] + 1)
            downLeftCoord = (coordinates[0] - 1, coordinates[1] + 1)
            
            while (upRightCoord[0] >= 1 and upRightCoord[0] <= 8 and upRightCoord[1] >= 1 and upRightCoord[1] <= 8 and upRight_check_finished == False):
                
                upRightCoordDict = chessDict[(upRightCoord)]
                upRightCoordString = upRightCoordDict[5]
                upRightCoordColour = upRightCoordString.split('_', 1)[0]
                upRightCoordType = upRightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (upRightCoordColour == 'e'):
                    bishopMoves.append(upRightCoord)
                    
                    upRightCoord = (upRightCoord[0] + 1, upRightCoord[1] - 1)

                    if (upRightCoord[0] < 1 and upRightCoord[0] > 8 and upRightCoord[1] < 1 and upRightCoord[1] > 8):
                        
                        upRight_check_finished = True
                    
                elif (upRightCoordColour != 'e'):
                    
                    if(upRightCoordColour != teamColour and upRightCoordType != 'king'):
                        bishopMoves.append(upRightCoord)
                        upRight_check_finished = True
                    
                    break

            while (upLeftCoord[0] >= 1 and upLeftCoord[0] <= 8 and upLeftCoord[1] >= 1 and upLeftCoord[1] <= 8 and upLeft_check_finished == False):
                
                upLeftCoordDict = chessDict[(upLeftCoord)]
                upLeftCoordString = upLeftCoordDict[5]
                upLeftCoordColour = upLeftCoordString.split('_', 1)[0]
                upLeftCoordType = upLeftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (upLeftCoordColour == 'e'):
                    bishopMoves.append(upLeftCoord)
                    
                    upLeftCoord = (upLeftCoord[0] - 1, upLeftCoord[1] - 1)

                    if (upLeftCoord[0] < 1 and upLeftCoord[0] > 8 and upLeftCoord[1] < 1 and upLeftCoord[1] > 8):
                        
                        upLeft_check_finished = True
                    
                elif (upLeftCoordColour != 'e'):
                    
                    if(upLeftCoordColour != teamColour and upLeftCoordType != 'king'):
                        bishopMoves.append(upLeftCoord)
                        upLeft_check_finished = True
                    
                    break

            while (downRightCoord[0] >= 1 and downRightCoord[0] <= 8 and downRightCoord[1] >= 1 and downRightCoord[1] <= 8 and downRight_check_finished == False):
                
                downRightCoordDict = chessDict[(downRightCoord)]
                downRightCoordString = downRightCoordDict[5]
                downRightCoordColour = downRightCoordString.split('_', 1)[0]
                downRightCoordType = downRightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (downRightCoordColour == 'e'):
                    bishopMoves.append(downRightCoord)
                    
                    downRightCoord = (downRightCoord[0] + 1, downRightCoord[1] + 1)

                    if (downRightCoord[0] < 1 and downRightCoord[0] > 8 and downRightCoord[1] < 1 and downRightCoord[1] > 8):
                        
                        downRight_check_finished = True
                    
                elif (downRightCoordColour != 'e'):
                    
                    if(downRightCoordColour != teamColour and downRightCoordType != 'king'):
                        bishopMoves.append(downRightCoord)
                        downRight_check_finished = True
                    
                    break

            while (downLeftCoord[0] >= 1 and downLeftCoord[0] <= 8 and downLeftCoord[1] >= 1 and downLeftCoord[1] <= 8 and downLeft_check_finished == False):
                
                downLeftCoordDict = chessDict[(downLeftCoord)]
                downLeftCoordString = downLeftCoordDict[5]
                downLeftCoordColour = downLeftCoordString.split('_', 1)[0]
                downLeftCoordType = downLeftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (downLeftCoordColour == 'e'):
                    bishopMoves.append(downLeftCoord)
                    
                    downLeftCoord = (downLeftCoord[0] - 1, downLeftCoord[1] + 1)

                    if (downLeftCoord[0] < 1 and downLeftCoord[0] > 8 and downLeftCoord[1] < 1 and downLeftCoord[1] > 8):
                        
                        downLeft_check_finished = True
                    
                elif (downLeftCoordColour != 'e'):
                    
                    if(downLeftCoordColour != teamColour and downLeftCoordType != 'king'):
                        bishopMoves.append(downLeftCoord)
                        downLeft_check_finished = True
                    
                    break
            
            
            
            



            return bishopMoves, clickedSquareKey
                    
            
            
        elif(currentSquareString == 'black_queen' or currentSquareString == 'white_queen'):

            queenMoves = []
            
            coordinates = (keyX, keyY)

            #HORIZONTAL MOVE SET
            up_check_finished = False
            down_check_finished = False
            left_check_finished = False
            right_check_finished = False
            
            upCoord = (coordinates[0] + 0, coordinates[1] - 1)
            downCoord = (coordinates[0] + 0, coordinates[1] + 1)
            leftCoord = (coordinates[0] -1, coordinates[1] + 0)
            rightCoord = (coordinates[0] + 1, coordinates[1] + 0)   

            #DIAGONAL MOVE SET
            upRight_check_finished = False
            upLeft_check_finished = False
            downRight_check_finished = False
            downLeft_check_finished = False
            
            upRightCoord = (coordinates[0] + 1, coordinates[1] - 1)
            upLeftCoord = (coordinates[0] -1, coordinates[1] - 1)
            downRightCoord = (coordinates[0] + 1, coordinates[1] + 1)
            downLeftCoord = (coordinates[0] - 1, coordinates[1] + 1)
            
            #HORIZONTAL
            while (upCoord[1] <= 8 and upCoord[1] >= 1 and up_check_finished == False):

                upCoordDict = chessDict[(upCoord)]
                upCoordString = upCoordDict[5]
                upCoordColour = upCoordString.split('_', 1)[0]
                upCoordType = upCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                #or teamColour != upCoordColour
                if (upCoordColour == 'e'):

                    queenMoves.append(upCoord)
                    upCoord = (upCoord[0], upCoord[1] - 1)

                    if (upCoord[1] < 1):
                        up_check_finished = True
                
                elif (upCoordColour != 'e'):
                   
                    if (upCoordColour != teamColour and upCoordType != 'king'):
                        
                        queenMoves.append(upCoord)
                        up_check_finished = True
                    
                    break
            
            
            while (downCoord[1] <= 8 and downCoord[1] >= 1 and down_check_finished == False):

                downCoordDict = chessDict[(downCoord)]
                downCoordString = downCoordDict[5]
                downCoordColour = downCoordString.split('_', 1)[0]
                downCoordType = downCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (downCoordColour == 'e'):


                    queenMoves.append(downCoord)
                    downCoord = (downCoord[0], downCoord[1] + 1)

                    if (downCoord[1] > 8):
                        down_check_finished = True
                
                elif (downCoordColour != 'e'):
                   
                    if (downCoordColour != teamColour and downCoordType != 'king'):
                        
                        queenMoves.append(downCoord)
                        down_check_finished = True
                    
                    break

            while (leftCoord[0] <= 8 and leftCoord[0] >= 1 and left_check_finished == False):

                leftCoordDict = chessDict[(leftCoord)]
                leftCoordString = leftCoordDict[5]
                leftCoordColour = leftCoordString.split('_', 1)[0]
                leftCoordType = leftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (leftCoordColour == 'e'):


                    queenMoves.append(leftCoord)
                    leftCoord = (leftCoord[0] - 1, leftCoord[1])

                    if (leftCoord[0] < 1):
                        left_check_finished = True
                
                elif (leftCoordColour != 'e'):
                   
                    if (leftCoordColour != teamColour and leftCoordType != 'king'):
                        
                        queenMoves.append(leftCoord)
                        left_check_finished = True
                    
                    break

            while (rightCoord[0] <= 8 and rightCoord[0] >= 1 and right_check_finished == False):

                rightCoordDict = chessDict[(rightCoord)]
                rightCoordString = rightCoordDict[5]
                rightCoordColour = rightCoordString.split('_', 1)[0]
                rightCoordType = rightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'

                if (rightCoordColour == 'e'):


                    queenMoves.append(rightCoord)
                    rightCoord = (rightCoord[0] + 1, rightCoord[1])

                    if (rightCoord[0] < 1):
                        right_check_finished = True
                
                elif (rightCoordColour != 'e'):
                   
                    if (rightCoordColour != teamColour and rightCoordType != 'king'):
                        
                        queenMoves.append(rightCoord)
                        right_check_finished = True
                    
                    break
                            
                                         
            #DIAGONAL
            while (upRightCoord[0] >= 1 and upRightCoord[0] <= 8 and upRightCoord[1] >= 1 and upRightCoord[1] <= 8 and upRight_check_finished == False):
                
                upRightCoordDict = chessDict[(upRightCoord)]
                upRightCoordString = upRightCoordDict[5]
                upRightCoordColour = upRightCoordString.split('_', 1)[0]
                upRightCoordType = upRightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (upRightCoordColour == 'e'):
                    queenMoves.append(upRightCoord)
                    
                    upRightCoord = (upRightCoord[0] + 1, upRightCoord[1] - 1)

                    if (upRightCoord[0] < 1 and upRightCoord[0] > 8 and upRightCoord[1] < 1 and upRightCoord[1] > 8):
                        
                        upRight_check_finished = True
                    
                elif (upRightCoordColour != 'e'):
                    
                    if(upRightCoordColour != teamColour and upRightCoordType != 'king'):
                        queenMoves.append(upRightCoord)
                        upRight_check_finished = True
                    
                    break

            while (upLeftCoord[0] >= 1 and upLeftCoord[0] <= 8 and upLeftCoord[1] >= 1 and upLeftCoord[1] <= 8 and upLeft_check_finished == False):
                
                upLeftCoordDict = chessDict[(upLeftCoord)]
                upLeftCoordString = upLeftCoordDict[5]
                upLeftCoordColour = upLeftCoordString.split('_', 1)[0]
                upLeftCoordType = upLeftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (upLeftCoordColour == 'e'):
                    queenMoves.append(upLeftCoord)
                    
                    upLeftCoord = (upLeftCoord[0] - 1, upLeftCoord[1] - 1)

                    if (upLeftCoord[0] < 1 and upLeftCoord[0] > 8 and upLeftCoord[1] < 1 and upLeftCoord[1] > 8):
                        
                        upLeft_check_finished = True
                    
                elif (upLeftCoordColour != 'e'):
                    
                    if(upLeftCoordColour != teamColour and upLeftCoordType != 'king'):
                        queenMoves.append(upLeftCoord)
                        upLeft_check_finished = True
                    
                    break

            while (downRightCoord[0] >= 1 and downRightCoord[0] <= 8 and downRightCoord[1] >= 1 and downRightCoord[1] <= 8 and downRight_check_finished == False):
                
                downRightCoordDict = chessDict[(downRightCoord)]
                downRightCoordString = downRightCoordDict[5]
                downRightCoordColour = downRightCoordString.split('_', 1)[0]
                downRightCoordType = downRightCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (downRightCoordColour == 'e'):
                    queenMoves.append(downRightCoord)
                    
                    downRightCoord = (downRightCoord[0] + 1, downRightCoord[1] + 1)

                    if (downRightCoord[0] < 1 and downRightCoord[0] > 8 and downRightCoord[1] < 1 and downRightCoord[1] > 8):
                        
                        downRight_check_finished = True
                    
                elif (downRightCoordColour != 'e'):
                    
                    if(downRightCoordColour != teamColour and downRightCoordType != 'king'):
                        queenMoves.append(downRightCoord)
                        downRight_check_finished = True
                    
                    break

            while (downLeftCoord[0] >= 1 and downLeftCoord[0] <= 8 and downLeftCoord[1] >= 1 and downLeftCoord[1] <= 8 and downLeft_check_finished == False):
                
                downLeftCoordDict = chessDict[(downLeftCoord)]
                downLeftCoordString = downLeftCoordDict[5]
                downLeftCoordColour = downLeftCoordString.split('_', 1)[0]
                downLeftCoordType = downLeftCoordString.split('_', 1)[1]

                if (currentSquareColour == 'black'):
                    teamColour = 'black'
                elif (currentSquareColour == 'white'):
                    teamColour = 'white'
                
                if (downLeftCoordColour == 'e'):
                    queenMoves.append(downLeftCoord)
                    
                    downLeftCoord = (downLeftCoord[0] - 1, downLeftCoord[1] + 1)

                    if (downLeftCoord[0] < 1 and downLeftCoord[0] > 8 and downLeftCoord[1] < 1 and downLeftCoord[1] > 8):
                        
                        downLeft_check_finished = True
                    
                elif (downLeftCoordColour != 'e'):
                    
                    if(downLeftCoordColour != teamColour and downLeftCoordType != 'king'):
                        queenMoves.append(downLeftCoord)
                        downLeft_check_finished = True
                    
                    break
            
            return queenMoves, clickedSquareKey
        
        
        elif(currentSquareString == 'black_king' or currentSquareString == 'white_king'):
            
            kingMoves = [[0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1]]
            possiblePoints = []

            for x in kingMoves:
                xoffset = x[0]
                yoffset = x[1]

                currentPoint = chessDict[(keyX, keyY)]
                currentPoint = currentPoint[5]
                currentPoint = str(currentPoint.split('_', 1)[0])   


                newPoint = (keyX + x[0], keyY + x[1])

                if (newPoint[0] >= 1 and newPoint[0] <= 8 and newPoint[1] >= 1 and newPoint[1] <= 8):
                    newChessDict = chessDict[newPoint[0], newPoint[1]]
                    newPointPieceString = newChessDict[5]
                    newPointPieceColour = str(newPointPieceString.split('_', 1)[0])  
                    newPointPieceType = newPointPieceString.split('_', 1)[1]

                    
                    if (currentPoint == 'black'):
                        teamColour = 'black'
                    elif(currentPoint == 'white'):
                        teamColour = 'white'

                    if (newPointPieceColour != teamColour and newPointPieceType != 'king'):    
                        
                        newChessDictKey = (newPoint[0], newPoint[1])
                        newX = newChessDict[3]
                        newY = newChessDict[4]
                        
                        possiblePoints.append(newChessDictKey)
            
            return possiblePoints, clickedSquareKey
        
        
        
        
        
        #Default Return
        return [(1, 1)], clickedSquareKey

def move_piece(selectedPossibleMove, clickedSquareKey, chessDict):
    
    #selected = new
    #clicked = old

    e_ = 'emptyspace'

    pieceString = 'e_'
    
    #Old Dict
    clickedSquareDict = chessDict[(clickedSquareKey[0], clickedSquareKey[1])]
    
    #Old Dict
    clickedSquarePiece = clickedSquareDict[0]
    
    #Old Dict
    clickedSquareString = clickedSquareDict[5]

    #New Dict
    selectedPossibleMoveDict = chessDict[(selectedPossibleMove[0], selectedPossibleMove[1])]

    #New Dict = Old Dict Piece
    selectedPossibleMoveDict[0] = clickedSquarePiece

    #New Dict = Old Dict Piece
    selectedPossibleMoveDict[5] = clickedSquareString

    
    newTestDict = clickedSquareDict


    
    newTestDict[0] = e_

    newTestDict[5] = 'e_'
    
    
    
    #dict = [0] : Piece , [1] : X Coord Corner, [2] : Y Coord Corner , [3] : X Coord Middle , [4] : Y Coord Middle, [5] : piece string
    

    #Swap Piece and Piece String

    #Chess Dict = 
    #chessDict[(clickedSquareKey[0], clickedSquareKey[1])] = selectedPossibleMoveDict
    chessDict[(selectedPossibleMove[0], selectedPossibleMove[1])] = selectedPossibleMoveDict
    chessDict[(clickedSquareKey[0], clickedSquareKey[1])] = newTestDict
    #print('attempted to move')

    
    return chessDict