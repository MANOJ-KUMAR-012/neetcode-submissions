class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_len = 1
        max_len = 1
        nums.sort()
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                curr_len+=1
                max_len = max(curr_len,max_len)
            else:
                curr_len = 1
        return max_len
        