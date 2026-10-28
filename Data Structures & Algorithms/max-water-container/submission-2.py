class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_a = 0

        l = 0
        r = len(heights) - 1

        while (l < r):
            a = (r - l) * min(heights[l], heights[r])

            max_a = max(a, max_a)

            if (heights[l] > heights[r]):
                r-=1

            elif (heights[l] < heights[r]):
                l+=1

            else:
                r-=1
                l+=1
            

        return max_a
        