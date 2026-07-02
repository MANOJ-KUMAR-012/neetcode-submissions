class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        arr = heights 
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                width = j - i
                height = min(heights[i],heights[j])
                area = width * height
                max_area = max(max_area,area)
        return max_area
        