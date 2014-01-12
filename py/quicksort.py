import random


def sort(xs):
    random.shuffle(xs)
    return _sort(xs)


def _sort(xs):
    if len(xs) <= 1:
        return xs
    pivot = xs[0]
    l = []
    r = []
    for x in xs[1:]:
        (l if x < pivot else r).append(x)
    return _sort(l) + [pivot] + _sort(r)
