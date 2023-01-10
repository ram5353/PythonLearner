def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[1])
    first_ending = float("inf")
    count  = 0
    for element in intervals:
        if element[0] < first_ending:
            count += 1
            first_ending = element[1]
    return count

print(minMeetingRooms([[7,10],[2,4]]))
