# lsd sort that handles 16-bit numbers, radix 16

def lsd(xs):
    exp = 4  # radix 16
    ys = [0 for x in xs]
    for i in xrange(16 / exp):
        counts = [0] + [0 for j in xrange(2 ** exp)]
        for x in xs:
            v = (x >> (i * exp)) & (2 ** exp - 1)
            counts[v + 1] += 1
        for r in xrange(2 ** exp):
            counts[r + 1] += counts[r]
        for x in xs:
            v = (x >> (i * exp)) & (2 ** exp - 1)
            ys[counts[v]] = x
            counts[v] += 1
        xs, ys = ys, xs
    return xs


def msd(xs, pos=0):
    if len(xs) <= 1:
        return xs

    ys = [0 for x in xs]
    R = 256
    v = lambda s, i: ord(s[i]) if i < len(s) else 0
    counts = [0, 0] + [0 for i in xrange(R)]
    for x in xs:
        counts[v(x, pos) + 2] += 1
    for r in xrange(R + 1):
        counts[r + 1] += counts[r]
    for x in xs:
        r = v(x, pos)
        ys[counts[r + 1]] = x
        counts[r + 1] += 1

    for r in xrange(R):
        lo, hi = counts[r], counts[r + 1]
        ys[lo:hi] = msd(ys[lo:hi], pos + 1)

    return ys
