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


def in_place(xs):
    random.shuffle(xs)
    return _in_place(xs, 0, len(xs) - 1)


def _in_place(xs, lo, hi):
    if hi <= lo:
        return
    i = lo
    j = hi + 1
    while True:
        i += 1
        j -= 1
        while i < hi and xs[i] < xs[lo]:
            i += 1
        while j > lo and xs[j] > xs[lo]:
            j -= 1
        if i >= j:
            break
        xs[i], xs[j] = xs[j], xs[i]
    xs[lo], xs[j] = xs[j], xs[lo]
    _in_place(xs, lo, j - 1)
    _in_place(xs, j + 1, hi)
