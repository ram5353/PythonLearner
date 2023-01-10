def closeTarget(words, target, startIndex):
    targetIndex = -1
    shortDistance = float("inf")
    n = len(words)
    for i, word in enumerate(words):
        if word == target:
            targetIndex = i
            shortDistance = min(shortDistance, abs(targetIndex - startIndex), n - abs(targetIndex - startIndex))
    return shortDistance
        


