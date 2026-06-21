class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        sortFreq = dict(sorted(frequency.items(), key = lambda x:x[1], reverse = True))
        return list(sortFreq.keys())[:k]
        