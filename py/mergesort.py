def down(xs):
    if len(xs) <= 1:
        return xs
    mid = len(xs) / 2
    return _merge(down(xs[:mid]), down(xs[mid:]))


def up(xs):
    span = 2
    while span < len(xs) * 2:
        i = 0
        while i < len(xs):
            mid = span / 2
            xs[i:i + span] = _merge(xs[i:i + mid], xs[i + mid:i + span])
            i += span
        span *= 2


def _merge(xs, ys):
    ix = 0
    iy = 0
    result = []
    while ix < len(xs) and iy < len(ys):
        if xs[ix] < ys[iy]:
            result.append(xs[ix])
            ix += 1
        else:
            result.append(ys[iy])
            iy += 1
    if ix < len(xs):
        result.extend(xs[ix:])
    else:
        result.extend(ys[iy:])
    return result
