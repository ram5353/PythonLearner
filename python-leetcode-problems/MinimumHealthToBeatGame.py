def minimumHealth(damage, armor):
    max_element = max(damage)
    total_sum = sum(damage)
    result = 0
    if max_element > armor:
        result = total_sum - max_element + (max_element - armor)
    else:
        result = total_sum - max_element
    return result

