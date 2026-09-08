class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1

        longestString = 0
        seenChar = {}

        l,r = 0,0
        count = 0
        while r < len(s):
            if seenChar.get(s[r], -1) >= l: # duplicate in substring
                l = seenChar[s[r]] + 1
                
            
            seenChar[s[r]] = r
            r += 1
            longestString = max(longestString, r-l)
        return longestString
