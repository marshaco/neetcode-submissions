class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import re

        t = list(t)

        if len(s) != len(t):
            return False

        for i in s:
            print(i)
            if i not in t:
                return False
            t.remove(i)

        print(t)
        return True