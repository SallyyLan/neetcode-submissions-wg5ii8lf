class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]




# class Solution:
#     def rob(self, nums: List[int]) -> int:
        
#         def dfs(i):
#             # base 
#             if i >= len(nums):
#                 return 0

#             return max(dfs(i + 1), nums[i] + dfs(i + 2))

#         return dfs(0)
        








# return the max amount of money can rob without alerting 
# conditions:
## 1. cannot rob two adjacent houses 


# dp -> dfs 
# dp -> tabulation 
# dp -> memorize 