class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        visit = set()

        def dfs(path):
            # base 
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for j in range(len(nums)):
                if nums[j] in visit:
                    continue
                    
                visit.add(nums[j])
                path.append(nums[j])

                dfs(path)
                path.pop()

                visit.remove(nums[j])

        dfs([])
        return res










# return all possibilities of permutation -> backtracking 
## permutation is the sub path has the same length of input nums
## permutation order matters, meaning (1,2)(2,1) are different 
### when order matter, have to initialize set for tracking 

## how to construct backtracking? (i, path)
### base: when the tmp path length == input nums length, append
### recursive: for loop the nums