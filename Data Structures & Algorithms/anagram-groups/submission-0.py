class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []
        found = {}

        for i,val in enumerate(strs):

            if tuple(self.convertToFreq(val)) in found:
                anagrams[found[tuple(self.convertToFreq(val))]].append(val)
            else:
                found[tuple(self.convertToFreq(val))] = len(anagrams)
                anagrams.append([val])
        return anagrams
        
    def convertToFreq(self, s: str) -> List[int]:

        freq = [0] * 26

        for i in s:
            freq[ord(i) - ord("a")] += 1
        
        return freq