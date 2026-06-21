class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
            
        print(frequency)
        topK = []

        for i in range(k):
            maxVal = max(frequency, key=frequency.get)
            topK.append(maxVal)
            frequency.pop(maxVal)


        return topK