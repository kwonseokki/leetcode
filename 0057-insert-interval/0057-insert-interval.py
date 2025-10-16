class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        start = -1
        end = -1
        insert_index = 0
        for i in range(len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            new_a = newInterval[0]
            new_b = newInterval[1]
            if new_a > b:
                insert_index += 1
            if b >= new_a and new_b >= a:
                if start == -1:
                    start = i
                end = i
        merged = [data for inner_list in intervals[start:end+1] for data in inner_list] + newInterval
        if start == -1:
            intervals.insert(insert_index, newInterval)
        else:
            intervals[start:end + 1] = [[min(merged), max(merged)]]
        return intervals