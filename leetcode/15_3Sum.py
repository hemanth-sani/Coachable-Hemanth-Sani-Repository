class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        list_numbers = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k :
                numbers_sum = a + nums[j] + nums[k]
                if numbers_sum > 0:
                    k -= 1
                elif numbers_sum < 0:
                    j += 1
                else:
                    list_numbers.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                
        return list_numbers
