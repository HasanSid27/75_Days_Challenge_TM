class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        for interval in sorted(intervals):
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],interval[1])
            else:
                result.append(interval)
        return result