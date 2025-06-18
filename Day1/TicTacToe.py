win_con = [[1,2,3],[4,5,6],[7,8,9],
           [1,4,7],[2,5,8],[3,6,9],
           [1,5,9],[3,5,7]]
def check_winner(board):
    x= []
    o = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x.append(i * 3 + j + 1)
            elif board[i][j] == 'O':
                o.append(i * 3 + j + 1)
            else:
                continue
    
    for win in win_con:
        if set(win).issubset(set(x)):
            return "X wins"
        elif set(win).issubset(set(o)):
            return "O wins"
        
    return "No winner"
    
    
board = [
    ["X", "O", "X"],
    ["O", "X", ""],
    ["O", "", "X"]
]

print(check_winner(board))