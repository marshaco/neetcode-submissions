class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = 1001
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            # There are numbers to the right which are smaller
            if nums[mid] > nums[r]:
                l = mid + 1
            # There are no numbers to the right which are smaller, and the current number is the smallest encountered
            elif nums[mid] < m:
                r = mid - 1
                m = nums[mid]
            # There are no numbers to the right which are smaller, but there are numbers to the left which are smaller
            else:
                r = mid - 1
            
        return m
