import random


def sort(xs):
    random.shuffle(xs)
    return _sort(xs)


def _sort(xs):
    if len(xs) <= 1:
        return xs
    pivot = xs[0]
    le = []
    gt = []
    for x in xs[1:]:
        if x <= pivot:
            le.append(x)
        else:
            gt.append(x)
    return _sort(le) + [pivot] + _sort(gt)
