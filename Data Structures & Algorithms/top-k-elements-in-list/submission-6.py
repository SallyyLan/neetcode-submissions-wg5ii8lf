class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        res = sorted(mp.items(), key = lambda item:item[1], reverse = True)

        return [ n for n, freq in res[:k]]