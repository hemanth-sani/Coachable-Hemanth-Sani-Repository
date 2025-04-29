from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_find = defaultdict(list)
        result = []
        for i in range(len(nums)):
            numbers_find[nums[i]].append(i)
        
        sorted_numbers = dict(sorted(numbers_find.items(), key = lambda x: x[0]))
      
        for num, i in sorted_numbers.items():
            if(target - num) in sorted_numbers:
                k = i.pop()
                result.append(k)
                result.append(sorted_numbers[target - num][0])
                break
                
        return result

# [1, 3, 2, 1], 5
# {1:[0, 3], 3:[1], 2:[2]}
# 5-3 = 2
