class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            sorted_ = ''.join(sorted(s))
            mp[sorted_].append(s)

        return list(mp.values())