from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        sorted_desc = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))

        res = []

        for key in sorted_desc:
            if len(res) < k:
                res.append(key)

        return res
