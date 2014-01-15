from . import heap


def sort(xs):
    h = heap.Min(items=xs)
    result = []
    while h:
        result.append(h.delete())
    return result
