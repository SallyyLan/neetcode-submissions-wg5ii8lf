class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col, i):

            if i == len(word):
                return True

            # base:
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or (row, col) in visit or board[row][col] != word[i]:
                return False 

            # recursive:
            visit.add((row, col))

            res = (dfs(row + 1, col, i + 1) or 
                dfs(row - 1, col, i + 1) or   
                dfs(row, col + 1, i + 1) or 
                dfs(row, col - 1, i + 1))  

            visit.remove((row, col))
            return res  

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False 







# return True is word in board else false 
# explore all possibilities -> backtracking 
# conditions:
## 1. the same cell may not used more than once -> set() for tracking 

# how to do backtracking on 2d?
# dfs(row, col, word)
## base case: when the point out of bond -> return 
## base case: when the search has == word 

## note the current cell in the set()
## recursive call -> explore the up, down, left, right 
## 


## nest loop to the grid  
