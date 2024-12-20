import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_of_nums = {}
        for num in nums:
            if num in count_of_nums:
                count_of_nums[num] += 1
            else:
                count_of_nums[num] = 1

        top_k_elements = []
        for num, frequency in count_of_nums.items():
            if len(top_k_elements) >= k:
                heapq.heappushpop(top_k_elements, (frequency, num))
            else:
                heapq.heappush(top_k_elements, (frequency, num))
        result = []
        for frequency, num in top_k_elements:
            result.append(num)
        return result
