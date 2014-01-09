def down(xs):
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) / 2
        return merge(down(xs[:mid]), down(xs[mid:]))


def up(xs):
    size = len(xs)
    span = 2
    while span < size * 2:
        i = 0
        while i < size:
            xs[i:i + span] = merge(xs[i:i + span / 2], xs[i + span / 2: i + span])
            i += span
        span *= 2
    return xs


def merge(xs, ys):
    output = []
    ix = 0
    iy = 0
    while ix < len(xs) or iy < len(ys):
        if ix < len(xs) and iy < len(ys):
            if xs[ix] <= ys[iy]:
                output.append(xs[ix])
                ix += 1
            else:
                output.append(ys[iy])
                iy += 1
        elif ix >= len(xs):
            output.append(ys[iy])
            iy += 1
        elif iy >= len(ys):
            output.append(xs[ix])
            ix += 1
    return output
