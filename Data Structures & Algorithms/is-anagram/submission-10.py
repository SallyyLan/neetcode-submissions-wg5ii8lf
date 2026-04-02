class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smp = defaultdict(int)
        tmp = defaultdict(int)

        for char_s in s:
            smp[char_s] += 1

        for char_t in t:
            tmp[char_t] += 1

        return smp == tmp