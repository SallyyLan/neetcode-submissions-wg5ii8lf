class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smp, tmp = defaultdict(int), defaultdict(int)

        for i in s:
            smp[i] += 1

        for j in t:
            tmp[j] += 1

        return smp == tmp