import random
import numpy as np

row = [7,8,0,4,0,0,1,2,0]
board = [[1,2,0,0],
         [2,0,0,0],
         [0,0,0,1],
         [3,0,1,0]]
board_1 =  [[1,3,0],
            [2,0,0],
            [0,0,1]]
n = 9
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
def notinrow(row):
    element = list()
    t = range(0, 10)
    for c in t:
        if c not in row:
            element.append(c)
    return element
    
c_board = np.zeros((9,9))
    
dis_ele = list()

def isDistinct1(element, board, column):
    for e in element:
        for r in range(n):
            print(f'b={board[r][column]}')
            if e == board[r][column]:
                flag = False
                break
            else:
                flag = True
        if flag:
            dis_ele = e
            break
        
        print(f'f={flag}')
        
    return dis_ele



def insert(row, pos, y):
    
    if pos < n:
        print('x')
        if y < n:
            print('y')
            if row[pos][y] == 0:
                #if zero then check for distinct elements
                print(f'pos={pos}, y={y}')
                e = notinrow(row[pos])#generates unique elements in a row
                print(f'e={e} ')
                if e != []:
                    d = isDistinct1(e, row, y) #unique elements in row and column
                    print(f'd={d}')
                    if d != None:   #if there areunique elements then it takes one and puts in place of zero
                        row[pos][y] =  d
                        print(row)
                        return insert(row, pos, y+1 )
                else:
                   
                    return insert(row, pos, y)
            else:
                return insert(row, pos, y+1)
        else:
            return insert(row, pos+1, y=0)
               
def insert1(board, x, y):
    if x < n:
        
        if y< n:
            
            if board[x][y] == 0:
                e = random.randrange(1, 10) 
                print(f'x={x}')
                print(f'y={y}\n')
                print(f'e={e}\n')
                if e not in board[x]:
                    print('x')
                    board[x][y] = e
                    return insert1(board, x, y+1)
                else:
                    
                    return insert1(board, x, y)
            else: 
                return insert1(board, x, y+1)
        else:
            return insert1(board, x+1, y=0)
print(isDistinct1([9,5,6,3], b, 2))

print(insert(b, 0, 0))