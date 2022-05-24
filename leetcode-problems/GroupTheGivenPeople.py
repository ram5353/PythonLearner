import collections


def groupThePeople(groupSizes):
    result = []
    groups = collections.defaultdict(list)

    for i, size in enumerate(groupSizes):
        groups[size].append(i)
        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []
    print(groups)

def groupThePeopleNormal(groupSizes):
    result = []
    dict = {}
    for i, size in range(0, len(groupSizes)):
        if groupSizes[i] in dict:
            dict[groupSizes[i]].append(i)
        else:
            dict[groupSizes[i]] = [i]
        if len(groupSizes[i]) == groupSizes[i]:
            result.append(dict[groupSizes[i]])
            dict[groupSizes[i]] = []


    return result


groupThePeople([3,3,3,3,3,1,3])

