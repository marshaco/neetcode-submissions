class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # Convert to freq array
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        # Return the dict as a list
        return list(anagrams.values())