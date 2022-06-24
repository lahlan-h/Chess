       
       
       
       
       
       
       
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