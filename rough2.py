import math
import random
board = [
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
board_1 =  [[7,8,0],
            [6,0,0],
            [0,0,0]]

# we need to make a work board
n = 3
w_board = board
flag = True
#then we need to think what to do next
#check that if the board is all numbers
def zero(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                yes = False
                break
    else: yes = True
    return yes



#now we need to actually do something!
#first insert a number in the row and then check if its valid:
#then go to next column and insert the next valid number
             


def insert_number(board, curr_pos_x, curr_pos_y):
    if curr_pos_x < n:
        if curr_pos_y < n:
            if board[curr_pos_x][curr_pos_y] == 0:
                element = random.randrange(1,3)
                print(f'element={element}')
                if validNumber(element, curr_pos_x, curr_pos_y):
                    board[curr_pos_x][curr_pos_y] = element
                    return insert_number(board, curr_pos_x, curr_pos_y+1) 
                else: 
                    return insert_number(board, curr_pos_x, curr_pos_y)
            else: 
                return insert_number(board, curr_pos_x, curr_pos_y+1)
            print(f'x={curr_pos_x}')
            print(f'y={curr_pos_y}')      
        return insert_number(board, curr_pos_x+1, curr_pos_y=0)
    
#now check for the validity of the given number for the given index
count = dict()


def validNumber(element, curr_pos_x, curr_pos_y):
    if rowDistinct(element,curr_pos_x) and columnDistinct(element, curr_pos_y):
        return True
    else: return False

def rowDistinct(element, curr_pos_x):
    for column in range(n):
        if element == board_1[curr_pos_x][column]:
                flag = False
                break
        else: flag = True
        print(f'flagr={flag}')
    return flag

def columnDistinct(element, curr_pos_y):
    for row in range(n):
        if element == board_1[row][curr_pos_y]:
            flag = False
            break
        else: flag = True
        print(f'flagc={flag}')
    return flag




def main():
    if zero(board_1):
        insert_number(board_1, 0, 0)
    print(board_1)

if __name__ == "__main__":
    main()    
