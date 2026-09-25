class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in strs:
            freqI = [0] * 26
            for j in i:
                freqI[ord(j) - ord("a")] += 1
            if tuple(freqI) not in anagrams:
                anagrams[tuple(freqI)] = [i]
            else:
                anagrams[tuple(freqI)].append(i)

        groups = []
        for key in anagrams:
            groups.append(anagrams[key])
        return groups

            