class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return n
        
        if n == 2:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]



# class Solution:
#     def climbStairs(self, n: int) -> int:

#         memo = {1:1, 2:2}

#         def dfs(i):
#             if i in memo:
#                 return memo[i]

#             memo[i] = dfs(i - 2) + dfs(i - 1)
#             return memo[i]

#         return dfs(n)




# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         def dfs(i):
#             # base 
#             if i >= n:
#                 return i == n

#             return dfs(i + 1) + dfs(i + 2)

#         return dfs(0)


