class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_ = defaultdict(int)
        t_ = defaultdict(int)

        for char in s:
            s_[char] += 1

        for char in t:
            t_[char] += 1

        return s_ == t_