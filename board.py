import pygame 
import solver
#the board
b = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
]

def solve(b):
            
            find = solver.marker(b)    
            if not find:
                return True
            else:
                row, column = find
            pygame.event.pump()
            for i in range(1, 10):
                    
                    
                    if solver.isUnique(i, b, row, column):
                        
                        b[row][column] = i
                        screen.fill((0, 0, 0))
                        draw()

                        pygame.display.update()
                        pygame.time.delay(20)
                        if solve(b):
                            
                            return True
                        b[row][column] = 0
                        screen.fill((0, 0, 0))

                        draw()
                        pygame.time.delay(50)
            return False

def draw():
    #coordinates for the rectangles
    x = 30
    y = 30
    for row in range(9):
        for col in range(9):
            if row < 8 and col < 8:
                
                pygame.draw.rect(screen, (0, 128 , 255), pygame.Rect(x, y, 120, 120), 2)
            if b[col][row] != 0:
                
                textsurface = myfont.render(f'{b[col][row]}', False, (0, 128, 255))
                screen.blit(textsurface, (15+x, 15+y))
            y = y + 60
       
        y = 30
        x = x + 60



#window size 
WINDOW_WIDTH = 605
WINDOW_HEIGHT = 605


pygame.init()
pygame.display.set_caption("SODOKU SOLVER USING BACKTRACKING")
myfont = pygame.font.SysFont('Comic Sans MS', 30)


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
run = True
clock = pygame.time.Clock()





while run:
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        
        
    draw()
    solve(b)
    

            


    
    
    
    pygame.display.flip()
    clock.tick(60)
        