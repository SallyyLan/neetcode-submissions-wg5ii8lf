class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        mp = {n:0 for n in nums}
        for n in nums:
            mp[n] += 1

        def dfs():
            # Base 
            if len(path) == len(nums):
                res.append(path[::])
                return

            # Recursive / backtrack
            for num in mp:
                if mp[num] > 0:
                    path.append(num)
                    mp[num] -= 1
                    dfs()
                    mp[num] += 1
                    path.pop()

        dfs()
        return res
            