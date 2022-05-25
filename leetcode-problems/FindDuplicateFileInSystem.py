import collections


def findDuplicate(paths):
    c = collections.defaultdict(list)
    for p in paths:
        a = p.split(" ")
        folder = a[0]
        for b in a[1:]:
            s = b.split(".txt")
            name = s[0]
            content = s[1]
            c[content].append((folder, name))
    output = []
    for k, v in c.items():
        input = []
        for each in v:
            input.append(f"{each[0]}/{each[1]}.txt")
        output.append(input)
    return output



paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
print(findDuplicate(paths))
