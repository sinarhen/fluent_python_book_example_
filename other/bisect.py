import _bisect


def grade(score, breakpoints=[60, 70, 80, 90, 99], grades='FDCBA'):
    i = _bisect.bisect_right(breakpoints, score)
    return grades[i]


gr = [grade(score) for score in [49, 90, 70, 50, 30]]
print(gr)