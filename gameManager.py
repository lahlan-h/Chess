from hashlib import new
import pygame
import random
import math

def draw_board(display, width, height, boardSize, boardTheme):
    black = boardTheme[0]
    white = boardTheme[1]

    display.fill(black)

    
    xPos = 0
    yPos = 0

    xPosc = 0 + width / (boardSize * 2)
    yPosc = 0 + height / (boardSize * 2)

    switch = 0
    
    rectWidth = width / boardSize
    rectHeight = height / boardSize

    positionCorner = []
    positionCentre = []
    positionColour = []
    
    for x in range(boardSize):
        for x in range(boardSize):
            if (switch == 0):
                colour = white            
                switch += 1
            else:
                colour = black
                switch = 0
            pygame.draw.rect(display,colour,(xPos ,yPos,rectWidth,rectHeight))
            positionCorner.append([xPos, yPos, colour])
            positionCentre.append([xPosc, yPosc, colour])
            
                     
            xPos = xPos + (width / boardSize)  
            xPosc = xPos + (width / (boardSize * 2))
        
        xPos = 0
        xPosc = 0 + width / (boardSize * 2)
        
        yPos = yPos + (height / boardSize)
        yPosc = yPos + (height / (boardSize * 2))
        
        if (switch == 0):
          colour = white            
          switch += 1
        else:
            colour = black
            switch = 0
    
    return positionCorner, positionCentre

def create_dict(posC, posM, width, height, boardSize):
    
    #posC = pos Corner
    #posM = pos Middle
    
    #Generates all pieces

    black_bishop = pygame.image.load("blackbishop.png")
    black_bishop = pygame.transform.scale(black_bishop, (width / boardSize , height / boardSize))

    white_bishop = pygame.image.load("whitebishop.png")
    white_bishop = pygame.transform.scale(white_bishop, (width / boardSize , height / boardSize))

    black_rook = pygame.image.load("blackrook.png")
    black_rook = pygame.transform.scale(black_rook, (width / boardSize , height / boardSize))

    white_rook = pygame.image.load("whiterook.png")
    white_rook = pygame.transform.scale(white_rook, (width / boardSize , height / boardSize))

    black_queen = pygame.image.load("blackqueen.png")
    black_queen = pygame.transform.scale(black_queen, (width / boardSize , height / boardSize))

    white_queen = pygame.image.load("whitequeen.png")
    white_queen = pygame.transform.scale(white_queen, (width / boardSize , height / boardSize))

    black_pawn = pygame.image.load("blackpawn.png")
    black_pawn = pygame.transform.scale(black_pawn, (width / boardSize , height / boardSize))

    white_pawn = pygame.image.load("whitepawn.png")
    white_pawn = pygame.transform.scale(white_pawn, (width / boardSize , height / boardSize))

    black_knight = pygame.image.load("blackknight.png")
    black_knight = pygame.transform.scale(black_knight, (width / boardSize , height / boardSize))

    white_knight = pygame.image.load("whiteknight.png")
    white_knight = pygame.transform.scale(white_knight, (width / boardSize , height / boardSize))

    black_king = pygame.image.load("blackking.png")
    black_king = pygame.transform.scale(black_king, (width / boardSize , height / boardSize))

    white_king = pygame.image.load("whiteking.png")
    white_king = pygame.transform.scale(white_king, (width / boardSize , height / boardSize))

    e_ = 'emptyspace'

    dict = {}
    
    counter = 0

    '''
    pieces = [
        e_, e_, e_, e_, e_, e_, e_, e_, 
        black_pawn, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, white_king, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
       e_, e_, e_, e_, e_, e_, e_, e_
        ]
    '''
    pieces = [
        black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook,
        black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn,
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        e_, e_, e_, e_, e_, e_, e_, e_, 
        white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn,
        white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook
        ]
    

    piecesString = []

    for x in pieces:
        x = [ i for i, a in locals().items() if a == x][0]
        piecesString.append(x)


    for y in range(8):
        y = y + 1
        for x in range(8):
            x = x + 1


            dict[(x, y)] = [pieces[counter], posC[counter][0], posC[counter][1], posM[counter][0], posM[counter][1], piecesString[counter]]

            
            counter += 1

    #dict = [0] : Piece , [1] : X Coord Corner, [2] : Y Coord Corner , [3] : X Coord Middle , [4] : Y Coord Middle, [5] : piece string

    return dict

def update_screen(dict, display, height, width, boardSize, boardTheme):
    
    black = boardTheme[0]

    display.fill(black)
    pos = draw_board(display, width, height, boardSize, boardTheme)
    
    #Circle 
    red = (255, 0 ,0)
    radius =  10

    for x in dict:
        key = x
        contents = dict[x]
        
        #Variables
        pieces = contents[0]
        xPosC = contents[1]
        yPosC = contents[2]

        xPosM = contents[3]
        yPosM = contents[4]


        coordinates = (xPosC, yPosC) 
        coordinatesMiddle = (xPosM, yPosM)

        if (pieces != 'emptyspace'):
            #pygame.draw.circle(display, red, coordinates, radius)
            #pygame.draw.circle(display, red, coordinatesMiddle, radius)

            display.blit(pieces, coordinates)

def find_closest_square(dict, mousePos, display, screenWidth, screenHeight, boardSize, colour):

    points = []
    distances = []


    #Retrieves all points from the chess dict
    for x in dict:
        key = x
        contents = dict[x]

        #Variables
        
        #AHHWHDHAWUDSA DOWAUGDYBWAIUDYBAWNDOU
        pieces = contents[0]


        xPosM = contents[3]
        yPosM = contents[4]

        pieceType = contents[5]
        pieceType = str(pieceType.split('_', 1)[0])


            
        

        if (pieces != 'emptyspace' and pieceType == colour):
            coordinates = (xPosM, yPosM)
            points.append(coordinates)

    #Calculates distance between all points on the chess board
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

    #HAVE TO DO Y
    halfSquareSizeX = squareSizeX / 2
    #halfSquareSizeX = 50
    

    keyX = int((closestPoint[0] / squareSizeX) + 0.5)
    keyY = int((closestPoint[1] / squareSizeY) + 0.5)

    #print(keyX, keyY)
    #print(dict[(keyX, keyY)])

    keys = (keyX, keyY)
    



    #Instead of returning x and y coordinate, instead return the key of the dictionary 
    if (mousePos[0] >= closestPoint[0] - halfSquareSizeX and mousePos[0] <= (closestPoint[0] + halfSquareSizeX) and mousePos[1] >= closestPoint[1] - halfSquareSizeX and mousePos[1] <= closestPoint[1] + halfSquareSizeX):
        #pygame.draw.circle(display, (255, 0, 0), closestPoint, 10)
        return keys
    else:
        return False

def calculate_moves(keys, chessDict, display):
    if (keys != False):
        keyX = keys[0]
        keyY = keys[1]

        #print(chessDict)
        currentDict = chessDict[(keyX, keyY)]

        currentDictPiece =  currentDict[5]
        

        if (currentDictPiece == 'black_knight' or currentDictPiece == 'white_knight'):
            
            knightMoves = [[-2,-1], [-2, 1], [1, -2], [-1,-2], [2, -1], [2,1], [-1, 2], [1, 2]]
            possiblePoints = []

            for x in knightMoves:
                xoffset = x[0]
                yoffset = x[1]

                currentPoint = chessDict[(keyX, keyY)]
                currentPoint = currentPoint[5]
                currentPoint = str(currentPoint.split('_', 1)[0])   


                newPoint = (keyX + x[0], keyY + x[1])

                if (newPoint[0] >= 1 and newPoint[0] <= 8 and newPoint[1] >= 1 and newPoint[1] <= 8):
                    newChessDict = chessDict[newPoint[0], newPoint[1]]
                    newPointPieceString = newChessDict[5]
                    newPointPieceString = str(newPointPieceString.split('_', 1)[0])            
                    
                    if (currentPoint == 'black'):
                        teamColour = 'black'
                    elif(currentPoint == 'white'):
                        teamColour = 'white'

                    if (newPointPieceString != teamColour):    
                        
                        newChessDictKey = (newPoint[0], newPoint[1])
                        newX = newChessDict[3]
                        newY = newChessDict[4]
                        
                        possiblePoints.append(newChessDictKey)
            
            return possiblePoints, keys

        elif (currentDictPiece == 'black_king' or currentDictPiece == 'white_king'):
            
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
                    newPointPieceString = str(newPointPieceString.split('_', 1)[0])            
                    
                    if (currentPoint == 'black'):
                        teamColour = 'black'
                    elif(currentPoint == 'white'):
                        teamColour = 'white'

                    if (newPointPieceString != teamColour):    
                        
                        newChessDictKey = (newPoint[0], newPoint[1])
                        newX = newChessDict[3]
                        newY = newChessDict[4]
                        
                        possiblePoints.append(newChessDictKey)
            
            return possiblePoints, keys
        
        elif (currentDictPiece == 'black_pawn' or currentDictPiece == 'white_pawn'):
            possiblePoints = []    

            
            currentPoint = chessDict[(keyX, keyY)]
            currentPoint = currentPoint[5]
            currentPoint = str(currentPoint.split('_', 1)[0])  

            conditionalMove = []

            if (currentPoint == 'black'):
                pawnMoves = [[0, 1]]
                conditionalMove = [[-1, 1], [1, 1]]
                if (keyY == 2):
                    pawnMoves.append([0, 2])
            elif (currentPoint == 'white'):
                pawnMoves = [[0, -1]]
                conditionalMove = [[-1, -1], [1, -1]]
                if (keyY == 7):
                    pawnMoves.append([0, -2])

            

            for x in pawnMoves:

                xoffset = x[0]
                yoffset = x[1]
 

                newPoint = (keyX + x[0], keyY + x[1])



                if (newPoint[0] >= 1 and newPoint[0] <= 8 and newPoint[1] >= 1 and newPoint[1] <= 8):
                    
                    if (currentPoint == 'black'):
                        teamColour = 'black'
                    elif(currentPoint == 'white'):
                        teamColour = 'white'  

                    for y in conditionalMove:
                        
                        #PROBLEM CHILD
                        new_conditionalMove = (keyX + y[0], keyY + y[1])
                        #[[-1, -1], [1, -1]]
                        
                        #if statement if between 1 and 8 x 

                        if (new_conditionalMove[0] >= 1 and new_conditionalMove[0] <= 8):
                            new_conditionalMoveDict = chessDict[(new_conditionalMove[0], new_conditionalMove[1])]
                            
                            
                            new_conditionalMoveString = new_conditionalMoveDict[5]
                            new_conditionalMoveString = str(new_conditionalMoveString.split('_', 1)[0]) 

                            #print(new_conditionalMoveString)
                            if (new_conditionalMoveString != teamColour and new_conditionalMoveString != 'e'):
                                possiblePoints.append((keyX + y[0], keyY + y[1]))



                    newChessDict = chessDict[newPoint[0], newPoint[1]]
                    newPointPieceString = newChessDict[5]
                    newPointPieceString = str(newPointPieceString.split('_', 1)[0])            
                    

                    if (newPointPieceString != teamColour):    
                        

                        newChessDictKey = (newPoint[0], newPoint[1])
                        newX = newChessDict[3]
                        newY = newChessDict[4]
                        
                        possiblePoints.append(newChessDictKey)
            
            return possiblePoints, keys

        if (currentDictPiece == 'black_placeHolder' or currentDictPiece == 'white_placeHolder'):

            #Find moves moves
        
            for x in 10:
                xoffset = x[0]
                yoffset = x[1]

                currentPoint = chessDict[(keyX, keyY)]
                currentPoint = currentPoint[5]
                currentPoint = str(currentPoint.split('_', 1)[0])   


                newPoint = (keyX + x[0], keyY + x[1])

                if (newPoint[0] >= 1 and newPoint[0] <= 8 and newPoint[1] >= 1 and newPoint[1] <= 8):
                    newChessDict = chessDict[newPoint[0], newPoint[1]]
                    newPointPieceString = newChessDict[5]
                    newPointPieceString = str(newPointPieceString.split('_', 1)[0])            
                    
                    if (currentPoint == 'black'):
                        teamColour = 'black'
                    elif(currentPoint == 'white'):
                        teamColour = 'white'

                    if (newPointPieceString != teamColour):    
                        
                        newChessDictKey = (newPoint[0], newPoint[1])
                        newX = newChessDict[3]
                        newY = newChessDict[4]
                        
                        possiblePoints.append(newChessDictKey)
                        
            print(possiblePoints)
            return possiblePoints, keys

    return [(1, 1)], keys

def print_possible_points(display, possiblePointsKeys, chessDict):
    for x in possiblePointsKeys:
        keyX, keyY = x[0], x[1]

        possiblePointDict = chessDict[(keyX, keyY)]
        possiblePointX = possiblePointDict[3]
        possiblePointY = possiblePointDict[4]


        pygame.draw.circle(display, (255, 0, 0), (possiblePointX, possiblePointY), 10)