class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = []
        current_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                merged_intervals.append(current_interval)
                current_interval = interval

        merged_intervals.append(current_interval)

        return merged_intervals
