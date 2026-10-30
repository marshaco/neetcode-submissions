class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        l, r = 0, len(self.nums)-1

        while l <= r:
            mid = (l+r) // 2

            if self.nums[mid] < val:
                l = mid + 1
            else:
                r = mid - 1


        self.nums = self.nums[:l] + [val] + self.nums[l:]

        return self.nums[-(self.k)]
