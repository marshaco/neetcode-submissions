class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True

        numbers = {'1','2','3','4','5','6','7','8','9'}

        # Checl horizontal
        for i in board:
            numbersSeen = set()
            for j in i:
                if j in numbersSeen:
                    isValid = False
                if j in numbers:
                    numbersSeen.add(j)
        
        # Check vertical
        for i in range(9):
            j = 0
            numbersSeen = set()
            while j < 9:
                if board[j][i] in numbersSeen:
                    isValid = False
                if board[j][i] in numbers:
                    numbersSeen.add(board[j][i])
                j += 1

        # Check boxes
        for boxNum in range(9):
            boxCol = (boxNum % 3) * 3
            boxRow = (boxNum // 3) * 3
            numsSeen = set()
            for iterator in range(9):
                checkCol = boxCol + (iterator % 3)
                checkRow = boxRow + (iterator // 3)
                if board[checkRow][checkCol] in numsSeen:
                    isValid = False
                if board[checkRow][checkCol] in numbers:
                    numsSeen.add(board[checkRow][checkCol])

        return isValid
        