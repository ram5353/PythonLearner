def dietPlanPerformance(calories, k, lower, upper):
    first_sum = sum(calories[:k])
    points = (first_sum > upper) - (first_sum < lower)
    for i in range(k, len(calories)):
        first_sum += calories[i] - calories[i - k]
        points += (first_sum > upper) - (first_sum < lower)
    return points

print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))

