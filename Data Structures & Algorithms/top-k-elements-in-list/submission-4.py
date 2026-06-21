class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        n = len(nums)

        buckets = [[] for _ in range(n+1)]
        for key, val in frequency.items():
            buckets[val].append(key) 

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for key in buckets[freq]:
                result.append(key)
                if len(result) == k:
                    return result  # or break out cleanly

        return [0]