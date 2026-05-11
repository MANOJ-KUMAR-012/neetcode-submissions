class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(n):
                if i!=j:
                    product*=nums[j]
            result.append(product)
        return result
        