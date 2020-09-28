import numpy as np
import random

prevs = -1

n=9

#The idea is right but is the time complexity is too big so it will not work, that's why it need changes!!!
#if instead  of checking the number is unique what I can do is generate a unique number fo that index in the board
# if in the index a unique number cannot be generated then only it has to go back to last changed number!


def isUnique(element, board, row, column):
    if element not in board[row]:
        for c in range(n):
            if element == board[c][column]:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            x = (row//3) * 3
            
            y = (column//3) * 3
            
            for i in range(x, x+3):
                
                for j in range(y, y+3):
                    
                    
                    if element == board[i][j]:
                        flag = False
                        break
                    else:
                        flag = True
                if flag == False:
                    break
    else:
        flag = False
    return flag

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

mark = np.zeros(np.array(b).shape, dtype=int)
def marker(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return i, j
    return None

marker(b)

def solve(b):
            find = marker(b)    
            if not find:
                return True
            else:
                row, column = find
            
            for i in range(1, 10):
                    print(f'i = {i}')
                    print(f'row={row},c={column}')
                    
                    if isUnique(i, b, row, column):
                        b[row][column] = i
                        print(f'b={b[row][column]}')
                        if solve(b):
                            print(f'before={b[row][column]}')
                            return True
                        b[row][column] = 0
            return False
                            
                             
               
                   
                
            
    
solve(b)
print(np.array(b))    
                
                    
                        
                        
                    
                
                