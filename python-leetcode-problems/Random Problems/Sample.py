def closetTarget(words, target, startIndex):
    targetIndices = []
    result = float("inf")
    for i in range(len(words)):
        if words[i] == target:
            targetIndices.append(i)
    if len(targetIndices) == 0:
        return -1
    for targetIndex in targetIndices:
        forwardDistance = (targetIndex - startIndex) % len(words)
        if forwardDistance < 0:
            forwardDistance += len(words)
        backwardDistance = (startIndex - targetIndex) % len(words)
        if backwardDistance < 0:
            backwardDistance += len(words)
        current_min = min(forwardDistance, backwardDistance)
        result = min(result, current_min)
    return result

print(closetTarget(["odjrjznxpn","cyulttuabe","zqxkdoeszk","yeewpgriok","odjrjznxpn","btqpvxpjzv","ukyudladhk","ukyudladhk","odjrjznxpn","yeewpgriok"],
"odjrjznxpn", 5))
