import pygame, sys
from pygame.locals import *
import gameManager
import calculateMoves
from pygame import mixer
import PySimpleGUI as sg

def main_menu(Test):
    
    if (Test != True):
        themes = ['Code Classic', 'Green Board', 'Icy Board']
        screenSizes = ['500px', '650px', '750px']
        #screenSizes = [350, 500, 650, 750]


        #set the theme for the screen/window
        sg.theme('Dark')
        #define layout
        layout=[[sg.Text('Choose Board Theme',size=(20, 1), font='Lucida',justification='left')],
                #[sg.Combo(themes, default_value='Code Classic', key='board')],
                [sg.Listbox(themes, default_values='Code Classic', size = (17 , 4), font='Lucida 13' ,key='theme')],
                
                [sg.Text('Choose Board Size (Pixels) ',size=(30, 1), font='Lucida',justification='left')],
                #[sg.Combo(screenSizes, key='dest')],
                [sg.Listbox(screenSizes, default_values='500px', size = (17, 4), font='Lucida 13', key='size')],
      
                #[sg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
                #[sg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet','Blanket', 'Neck Rest'], select_mode='extended', key='fac', size=(30, 6))],

                [sg.Button('START', font=('Lucida',12)),sg.Button('CANCEL', font=('Lucida',12))]]
        #Define Window
        win =sg.Window('Major Project Chess',layout, size= (350, 250))
        #Read  values entered by user
        e , p = win.read()
        
        #close first window
        win.close()
        
        #access the selected value in the list box and add them to a string
        

        if (e == 'CANCEL'):
            return False
        
        elif(e == 'START'):
            # [0] = Theme, [1] = Size
            mainMenuArray = []

            for x in p:
                returnDict = p[x][0]
                mainMenuArray.append(returnDict)       
            
            return mainMenuArray
    else:
        return ['Code Classic', '600px']
        
def game_loop(chessDict, display, screenWidth, screenHeight, boardSize, boardTheme):
    searching = True
    
    #If turn == True
        #White Turn
    
    #If Turn == False
        #Black Turn


    #mixer.music.load("../Major Project Chess/Audio Files/move_piece.wav")
    mixer.music.load("move_piece.wav")
    mixer.music.set_volume(0.7)


    whitesTurn = True

    while True:
        

        #Maybe screen doesn't have to be updated every loop, instead when a piece is moved
        #gameManager.update_screen(chessDict, display, screenHeight, screenWidth, boardSize)
        
        #Run Code Here
        
        for event in pygame.event.get():
            #Run Event Code Here
            
            mousePos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                gameManager.update_screen(chessDict, display, screenHeight, screenWidth, boardSize, boardTheme)
                
                if (searching == False):
                    
                   
                    selectedPossibleMove = calculateMoves.choose_move(chessDict, mousePos, screenWidth, screenHeight, boardSize, possibleMoves, display)
                    
                    
                    if (selectedPossibleMove != False):
                        
                        chessDict = calculateMoves.move_piece(selectedPossibleMove, clickedSquareKey, chessDict)
                        gameManager.update_screen(chessDict, display, screenHeight, screenWidth, boardSize, boardTheme)
                        
                        if (whitesTurn == True):
                            whitesTurn = False
                            pygame.display.set_caption('Major Project: Chess - Blacks Turn')
                        elif(whitesTurn != True):
                            pygame.display.set_caption('Major Project: Chess - Whites Turn')
                            whitesTurn = True
                        
                        
                        
    
                    
                        mixer.music.play()
                    searching = True
                    continue




                
                
                if (searching == True):
                    
                    if (whitesTurn == True):
                        clickedSquareKey = gameManager.find_closest_square(chessDict, mousePos, display, screenWidth, screenHeight, boardSize, 'white')
                    elif(whitesTurn != True):
                        clickedSquareKey = gameManager.find_closest_square(chessDict, mousePos, display, screenWidth, screenHeight, boardSize, 'black')
                        
                    
                    if (clickedSquareKey != False):
                        
                        #possibleMoves = gameManager.calculate_moves(clickedSquareKey, chessDict, display)

                        #Maybe Return If King In Check
                        possibleMoves, clickedSquareKeys = calculateMoves.possibles_moves(clickedSquareKey, chessDict, display)

                        if(possibleMoves == []):
                            continue
                        

                        calculateMoves.print_possible_points(display, possibleMoves, chessDict, screenWidth, boardSize)
                        #calculateMoves.move_piece(possibleMoves[0], clickedSquareKeys)
                        
                        searching = False
                        continue
                    #gameManager.print_possible_points(display, possibleMoves[0], chessDict)
            

  

                
            if (event.type==QUIT):
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main():
    
    results = main_menu(False)

    if (results != False):
        pygame.init()
        mixer.init()   

        board, size = results[0], results[1]
        size = int(size.split('px', 1)[0])

        boardTheme = (163, 124, 105) , (234, 216, 194)

        if (board == 'Code Classic'):
            boardTheme = (163, 124, 105) , (234, 216, 194)
        elif (board == 'Green Board'):
            boardTheme = (102, 139, 79) , (234, 235, 208)
        elif (board == 'Icy Board'):
            boardTheme = (113, 152, 175), (228, 239, 248)

        #Variables
        boardSize = 8
        screenWidth =  size
        screenHeight =  size


        #Sets application name
        display = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption('Major Project: Chess - Whites Turn')
        #pygame.display.set_caption('Major Project: Chess     Whites Turn')
        
        #Sets application icon
        pygameChessIcon = pygame.image.load("Icon.png")
        pygame.display.set_icon(pygameChessIcon)
    
        #Board postions, pos[0] = corner, pos[1] = middle (centre)
        pos = gameManager.draw_board(display, screenWidth, screenHeight, boardSize, boardTheme)

        #dict = [0] : Piece , [1] : X Coord Corner, [2] : Y Coord Corner , [3] : X Coord Middle , [4] : Y Coord Middle, [5] : piece string
        
        #Dictionary = [0] = PiecePNG , [1] = [X Coordinate Corner], [2] = [Y Coordinate Corner], [3] = [X Coordinate Middle], [4] = [Y Coordinate Middle], [5] = VariableName
        
        chessDict = gameManager.create_dict(pos[0], pos[1], screenWidth, screenHeight, boardSize)

        #Updates screen
        gameManager.update_screen(chessDict, display, screenHeight, screenWidth, boardSize, boardTheme)
        
        game_loop(chessDict, display, screenWidth, screenHeight, boardSize, boardTheme)


if __name__ == "__main__":
    main()