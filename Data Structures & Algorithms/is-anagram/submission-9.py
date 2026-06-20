class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)

        if len(s) != len(t):
            return False

        for i in s:
            if i not in t:
                return False
            t.remove(i)

        return True