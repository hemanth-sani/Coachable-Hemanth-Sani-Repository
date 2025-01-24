import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_of_nums = defaultdict(int)
        for num in nums:
            if num in count_of_nums:
                count_of_nums[num] += 1
            else:
                count_of_nums[num] = 1

        max_freq_heap = []
        for num, frequency in count_of_nums.items():
            if len(max_freq_heap) >= k:
                heapq.heappushpop(max_freq_heap, (frequency, num))
            else:
                heapq.heappush(max_freq_heap, (frequency, num))
        result = []
        for frequency, num in max_freq_heap:
            result.append(num)
        return result
