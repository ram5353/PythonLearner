def deleteGreatestValue(grid):
    result = 0
    max_list = []
    while any(grid):
        for i in range(0, len(grid)):
            if len(grid[i]) > 0:
                max_value = max(grid[i])
                grid[i].remove(max_value)
                max_list.append(max_value)
        result += max(max_list)
        max_list = []
    return result

print(deleteGreatestValue([[10]]))