class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            maxleft = 0
            for j in range(i+1):
                maxleft = max(maxleft,height[j])
            maxright = 0
            for j in range(i,len(height)):
                maxright = max(maxright,height[j])
            waterlevel = min(maxleft,maxright)
            total+=waterlevel - height[i]
        return total
        