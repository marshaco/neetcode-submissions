class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0 
        hi = len(heights)-1

        best = min(heights[lo], heights[hi]) * (hi - lo)
        while lo < hi:
            curr = min(heights[lo], heights[hi]) * (hi - lo)
            
            if curr > best:
                best = curr

            if heights[lo] > heights[hi]:
                hi -= 1
            else:
                lo += 1

        return best