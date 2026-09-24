def load_board (file_name):
    found = False
    while not found:
        try:
            file = open(file_name, "r")
            content = file.read()
            found = True
        except:
            file_name = input("File not found, input valid file: ")
    return content
    file.close()
def cast_board (board):
    numbers = board.split (" ")
    print (numbers)
    array_board = []
 
    for i in range (9):
        row = []
        for j in range (9):
            row.append (numbers[9*i + j])
 
        array_board.append (row)
    return array_board