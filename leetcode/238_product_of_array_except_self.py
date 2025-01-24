class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        mul = 1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= mul
            mul *= nums[i]
        
        return ans
