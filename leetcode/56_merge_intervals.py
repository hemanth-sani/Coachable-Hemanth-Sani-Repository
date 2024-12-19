class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        length_of_intervals = len(sorted_intervals)
        interval = 1
        starting = sorted_intervals[0][0]
        ending = sorted_intervals[0][1]
        
        while interval < length_of_intervals:
            next_starting = sorted_intervals[interval][0]
            next_ending = sorted_intervals[interval][1]
            if ending >= next_starting:
                max_interval_value = max(ending, next_ending)
                min_interval_value = min(starting, next_starting)
                starting, ending = min_interval_value, max_interval_value
            else:
                result.append([starting, ending])
                starting, ending = sorted_intervals[interval][0], sorted_intervals[interval][1]

            interval += 1

        result.append([starting, ending])
        return result

            
