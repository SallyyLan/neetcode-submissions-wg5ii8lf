class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        if not nums:
            return []

        res = []
        def dfs(i, total, cur_list):

            # base:
            if total == target:
                res.append(cur_list.copy())
                return

            if i >= len(nums) or total > target:
                return 

            # recursive 
            cur_list.append(nums[i])
            dfs(i, total + nums[i], cur_list)
            cur_list.pop()
            dfs(i + 1, total, cur_list)

        dfs(0, 0, [])
        return res 









# return the list of lists that numbers combinations == target
# conditions:
## 1. dfs -> we want to find all the combinations as possible 
## 2. ensure the total is == target -> a tracker for the total
## 3. a res list for storing combination, a tmp list for storing current combinations

# dfs
## base: when the cur total == target, append to the res 
## base: if the pointer out of bound or the cur combination > target

## recursive: 
### total += the pointer num 
### cur list append the pointer num 
### pop the last number -> explore all possibilities 
### call the func again but move the pointer to next 





