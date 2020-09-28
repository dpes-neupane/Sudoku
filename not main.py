import pygame

pygame.init()

window_size=(310, 310)
width = 303
height = 303

class Grid():
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        
    def draw(self, win):
        gap = int(self.width/9)

        for x in range(9):
            if x % 3 == 0 :
                pygame.draw.line(win, (0,0,0),  (x*gap, 0), (x*gap, self.height), 4 )
                pygame.draw.line(win, (0,0,0),  (0, x*gap), (self.width, x*gap), 4 )
            else:
                pygame.draw.line(win, (0,0,0),  (x*gap, 0), (x*gap,self.height), 2 )
                pygame.draw.line(win, (0,0,0),  (0, x*gap), (self.width, x*gap), 2 )
    
        


def main():
    #Initialize:
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Soduku")
    board = Grid(9, 9, 310, 310)
    #Background:
    screen.fill((255,255,255))

    #the individual rectangle
    
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        pygame.display.update
        board.draw(screen)
    pygame.quit()





if __name__ == '__main__': main()