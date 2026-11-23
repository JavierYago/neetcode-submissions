class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cuenta_s = {}
        cuenta_t = {}
        for n in s:
            cuenta_s[n] = cuenta_s.get(n,0) + 1
        for m in t:
            cuenta_t[m] = cuenta_t.get(m,0) + 1
        return cuenta_s == cuenta_t        