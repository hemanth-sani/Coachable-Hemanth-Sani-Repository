class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, k = 0, len(nums) - 1 
        nums = sorted(nums)
        list_numbers = []
        numbers_sum = 0
        while i < k and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
            else:
                j, k = i + 1, len(nums) - 1
                while j < k :
                    numbers_sum = nums[i] + nums[j] + nums[k]
                    if i != j and j != k and i != k and numbers_sum == 0:
                        list_numbers.append((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                    elif numbers_sum > 0:
                        k -= 1
                    else:
                        j += 1
                    numbers_sum = 0
                i += 1
        return list_numbers
