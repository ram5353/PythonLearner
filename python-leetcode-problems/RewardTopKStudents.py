from collections import defaultdict


def topStudents(positive_feedback, negative_feedback, report, student_id, k):
    d = defaultdict(int)
    pos = set(positive_feedback)
    neg = set(negative_feedback)
    for i in range(len(report)):
        id = student_id[i]
        s = report[i]
        for word in s.split():
            if word in pos:
                d[id] += 3
            elif word in neg:
                d[id] -= 1
    arr = list(zip(d.keys(),d.values()))
    arr.sort()
    arr.sort(key = lambda x:x[1],reverse = True)
    return [x for x,y in arr[:k]]

positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is not studious","the student is smart"]
student_id = [1,2]
k = 2
print(topStudents(positive_feedback, negative_feedback, report, student_id, k))