import itertools


def naive(l):
    cap = 0
    height = 1
    while True:
        acc = 0
        include = False
        for h in l:
            if h >= height:
                if not include:
                    include = True
                else:
                    cap += acc
                    acc = 0
            if include and h < height:
                acc += 1
        if not include:  # nothing left to do
            break
        height += 1
    return cap

def beautiful(l):
    mins = map(min, zip(scanl1(max, l), scanr1(max, l)))
    return sum(map(lambda (h, g): h - g, zip(mins, l)))

def scanl1(f, xs):
    def f_(acc, x):
        return acc + [f(acc[-1], x)] if len(acc) else [x]
    return reduce(f_, xs, [])

def scanr1(f, xs):
    return list(reversed(scanl1(f, reversed(xs))))
