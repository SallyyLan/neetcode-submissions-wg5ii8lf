class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smp, tmp = {}, {}

        for i in s:
            if i in smp:
                smp[i] += 1
            else:
                smp[i] = 1

        for j in t:
            if j in tmp:
                tmp[j] += 1
            else:
                tmp[j] = 1

        return smp == tmp