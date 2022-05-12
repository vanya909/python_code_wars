def sum_of_intervals(intervals):
    a = set()
    for interval in intervals:
        a.update(x for x in range(interval[0], interval[1]))
    return len(a)
    