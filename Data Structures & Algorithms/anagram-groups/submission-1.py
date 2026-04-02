class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for s in strs:
            sorteds = ''.join(sorted(s))
            mp[sorteds].append(s)

        return list(mp.values())