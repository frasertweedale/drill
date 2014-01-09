import itertools


def mapsub(m, s):
    nsubs = []
    results = []
    for c in s:
        if c in m:
            nsubs.append(len(m[c]))
    for product in itertools.product(*(xrange(-1, x) for x in nsubs)):
        result = ''
        subst_index = 0
        for c in s:
            if c in m:
                if product[subst_index] != -1:
                    c = m[c][product[subst_index]]
                subst_index += 1
            result += c
        results.append(result)
    return results
