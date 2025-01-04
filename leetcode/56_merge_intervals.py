class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        N = len(sorted_intervals)
        i = 1
        start, end = sorted_intervals[0]
        
        while i < N:
            next_start, next_end = sorted_intervals[i]
            if end >= next_start:
                max_interval_value = max(end, next_end)
                min_interval_value = min(start, next_start)
                start, end = min_interval_value, max_interval_value
            else:
                result.append([start, end])
                start, end = sorted_intervals[i]

            i += 1

        result.append([start, end])
        return result

            
