#!usr/bin/python3

class Solution:
    def isValidSudoku(self, board):
        valid = []
        for row in board:
            valid = []
            for num in row:
                if num in valid:
                    return False
                elif num != '.':
                    valid.append(num)
        
        for i in range(9):
            valid = []
            for j in range(9):
                if board[j][i] in valid:
                    return False
                elif board[j][i] != '.':
                    valid.append(board[j][i])
        
        for b in range(0, 7, 3):
            for a in range(0, 7, 3):
                valid = []
                for j in range(3):
                    for i in range(3):
                        if board[i+a][j+b] in valid:
                            return False
                        elif board[i+a][j+b] != '.':
                            valid.append(board[i+a][j+b])
        
        return True

                    