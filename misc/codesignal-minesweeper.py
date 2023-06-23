'''You are given a boolean matrix field representing the distribution of bombs in the rectangular field.
You are also given integers x and y, representing the coordinates of the player's first clicked cell
x represents the row index, and y represents the column index, both of which are 0-based.

Your task is to return an integer matrix of the same dimensions as field, representing the resulting field after applying this click. 
If a cell remains concealed, the corresponding element should have a value of -1.

It is guaranteed that the clicked cell does not contain a mine. '''

def solution(field, x, y):
    bombs = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            try:
                if field[i][j] == True:
                    bombs += 1
            except IndexError:
                pass
    
    # Create array after click
    for i in range(len(field)):
        for j in range(len(field[i])):
            if i == x and j == y:
                field[i][j] = bombs
            else:
                field[i][j] = -1
                
    if bombs != 0:
        return field
