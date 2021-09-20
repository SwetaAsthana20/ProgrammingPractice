def merge_interval(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    i = 0
    while i < len(intervals):
        if not result or result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            # result[-1][0] = min(intervals[i][0], result[-1][0])
            result[-1][1] = max(intervals[i][1], result[-1][1])
        i += 1

    return result


print(merge_interval([[1, 4], [2, 6], [0, 4], [15, 18]]))
