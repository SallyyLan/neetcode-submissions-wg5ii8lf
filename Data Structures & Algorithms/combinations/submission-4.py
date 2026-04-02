class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(i, path):
            # base:
            if len(path) == k:
                res.append(path[:])
                return 

            # recurisve / backtracking 
            for j in range(i , n + 1):
                path.append(j)
                dfs(j + 1, path)
                path.pop()

        dfs(1, [])
        return res








# return all possibilites that list matches the input length 
# conditions:
## 1. the end range is inputed 
## 2. the append tmp length must match the lenght of k 
## 3. the entire range is [1, n] -> in for loop should be n + 1

# since we want to find out all posiibilities -> backtracking 
## how to construct backtracking ???
## 1. based on what to append?
## 2. recursive / backtrack call? for loop the range by using i to track 

# path is revised everytime so should be in the functions -> [] 
# since we need to return entire list -> result = []