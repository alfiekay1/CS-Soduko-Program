def take_input():
    print("Enter row, column and value: ")
    row = int(input("")) - 1
    column = int(input("")) - 1
    value = input("")

    return row, column, value

def check_not_original(x, y, grid):
    if "." in str(grid[y][x]):
        return False
    else:
        return True

def check_row_column(x, y, grid, value):
    state = True
    for i in grid[y]:
        if str(grid[y])[0] == str(value):
            state = False
    for j in grid[x]:
        if str(grid[x])[0] == str(value):  
            state = False
    return state

def check_square(x, y, grid, value):
    square_index = (
        x // 3,
        y // 3
    )
    local_square = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i // 3 == y // 3 and j // 3 == x // 3:
                local_square.append(str(grid[i][j])[0])
    if value not in local_square:
        return True
    else:
        return False

def check_all(x, y, grid, value):
    state = True
    state = state and check_not_original(x, y, grid)
    state = state and check_row_column(x, y, grid, value)
    state = state and check_square(x, y, grid, value)
    return state

def insert_input(x, y, grid, value):
    grid[y][x] = value
    return grid
    
def handle_input(grid):
    x, y, value = take_input()
    value = str(value)
    if not check_all(x, y, grid, value):
        print("Invalid input")
        return None
    else:
        return insert_input(x, y, grid, value)
