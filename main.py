from time import sleep
import pygame
pygame.init()



def display_winner(window,winner):
    if winner ==1:
        window.blit(player1wins,(150,300))
    elif winner == 2:
        window.blit(player2wins,(150,300))
    elif winner == -1:
        window.blit(draw,(150,300))
    
    window.blit(replay,(150,600))
    pygame.display.update()

def ready_board(window):
    window.fill((0,0,0))
    window.blit(board_surface,(0,0))
    pygame.display.update()


def check_draw(board):
    for i in board:
        for j in i:
            if j==0:
                return False
    else:
        return True

def check_win(board,player):
    
    for j in [0,1,2]:    
        if board[0][j]==player and board[1][j]==player and board[2][j]==player:
            return True
        if board[j][0]==player and board[j][1]==player and board[j][2]==player:
            return True
    if (board[0][0],board[1][1],board[2][2])==(player,player,player):
        return True
    if (board[2][0],board[1][1],board[0][2])==(player,player,player):
        return True
    

    return False


win = pygame.display.set_mode((900,900))
pygame.display.set_caption("Tic-Tac-Toe")

#required images
board_surface = pygame.image.load('images/board.png')
cross = pygame.image.load('images/cross2.png')
player1wins = pygame.image.load('images/player1wins.png')
player2wins = pygame.image.load('images/player2wins.png')
draw = pygame.image.load('images/draw.png')
replay = pygame.image.load('images/play_again.png')
circle = pygame.image.load('images/circle1.png')

def initiate_variables():
    global clock,one,two,three,four,five,six,seven,eight,nine,game_over,turn,board,mainloop,result_loop,result_declared
    clock = pygame.time.Clock()
    one,two,three,four,five,six,seven,eight,nine=False,False,False,False,False,False,False,False,False
    game_over = False
    ready_board(win)
    turn = 1

    board = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    mainloop = True
    result_loop = False
    result_declared = False

initiate_variables()
while not game_over:
    if mainloop:        
        if turn%2==0:
            player=2
        else:
            player=1


        clock.tick(24)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        
        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            if coords[0]<300:
                if coords[1]<300 and not one:
                    one = True
                    board[0][0]=player
                    mark = (150,150)
                elif 300<coords[1]<600 and not four:
                    four = True
                    board[1][0]=player
                    mark= (150,450)
                elif 600<coords[1]<900 and not seven:
                    seven = True
                    board[2][0]=player
                    mark= (150,750)
            elif 300<coords[0]<600:
                if coords[1]<300 and not two:
                    two = True
                    board[0][1]=player
                    mark = (450,150)
                elif 300<coords[1]<600 and not five:
                    five = True
                    board[1][1]=player
                    mark = (450,450)
                elif 600<coords[1]<900 and not eight:
                    eight = True
                    board[2][1]=player
                    mark = (450,750)
            elif 600<coords[0]<900:
                if coords[1]<300 and not three:
                    three = True
                    board[0][2]=player
                    mark = (750,150)
                elif 300<coords[1]<600 and not six:
                    six = True
                    board[1][2]=player
                    mark = (750,450)
                elif 600<coords[1]<900 and not nine:
                    nine = True
                    board[2][2]=player
                    mark = (750,750)
            if player ==1:
                win.blit(circle,(mark[0]-120,mark[1]-120))
            else:
                win.blit(cross,(mark[0]-120,mark[1]-120))
            result_loop = (check_win(board,player),check_draw(board))
            if result_loop[0]==True:
                mainloop=False
            elif result_loop==(False,True):
                player = -1
                mainloop=False

            pygame.display.update()
            turn +=1
            sleep(0.25)
        
    elif result_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True

        if not result_declared:
            win.fill((0,0,0))
            display_winner(win,player)
            result_declared = True

        if pygame.mouse.get_pressed()[0]:
            sleep(0.25)
            coords_mouse = pygame.mouse.get_pos()
            if 150<coords_mouse[0]<750 and 600<coords_mouse[1]<800:
                initiate_variables()
        
        

        
        


pygame.quit()