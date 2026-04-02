class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, path):
            # base 
            res.append(path[:])

            # recursive /  backtrack 
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])
        return res 




# return all possible subsets of nums 
# conditions:
## 1. all in put is unique 
## 2. must not have duplicate
## 3. can order in any order 

# since we want to find all the possibilities -> backtracking 
# how to construct backtracing -> construct decision tree -> dfs(i, path)
## 1. base case: when the pointer is out of bound 
    ### append the tmp path to the result 
## 2. recursive call 
    ### append the current pointer to path -> recursively call dfs 
## 3. backtrack 
    ### pop the current pointer from path -> recursively call dfs again 

## 4. call the dfs and return result 

## what do we need? 
### a result list for final return 
### a tmp list for each step append








