lass Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start>= prevEnd: #if not overlapping
                prevEnd = end
            else:   #if it is overlapping
                res+=1
                prevEnd = min(end,prevEnd)
        return res