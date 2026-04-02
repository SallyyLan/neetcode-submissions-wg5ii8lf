class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0 

        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()

        def dfs(r, c):
            # base:
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or (r, c) in visit):
                return 

            visit.add((r,c))

            # recursive 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r, c)
                    island += 1

        return island 



        
















# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         island = 0

#         def bfs(r,c):
#             # queue
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))

#             while q:
#                 row, col = q.popleft()
#                 direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#                 for dr, dc in direction:
#                     rdr, cdc = row + dr, col + dc

#                     if (rdr in range(rows) and cdc in range(cols) and grid[rdr][cdc] == '1' and (rdr, cdc) not in visit):
#                         q.append((rdr, cdc))
#                         visit.add((rdr, cdc))



#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1' and (r,c) not in visit:
#                     bfs(r, c)
#                     island += 1

#         return island 











# graph problem 
# return the number of island in the grid 
## the tracker for the island 
## visit set 

# BFS solution (r, c) - using queue 
## how to construct BFS? 
### base case: if the grid is empty, then we return 0

### recursive call: using queue
### initialize a queue (dequeu), push the current r and c into the queue 
### four sides [[1, 0], [0, 1], [-1, 0], [0, -1]]
### r, c + for loop the four sides 
### 

## how to run the grid?  
### nest for loop: 



# DFS solution 

