class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def dfs(i, path):
            # base 
            if sum(path) == target:
                res.append(path[::])
                return

            # recursive/backtrack
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                dfs(j + 1, path)
                path.pop()

        dfs(0, [])
        return res 