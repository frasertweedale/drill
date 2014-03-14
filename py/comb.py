def mask_k_comb_for_all_k(xs):
    results = set()
    for n in range(2 ** len(xs)):
        result = ['*' for x in xs]
        for i in xrange(len(xs)):
            if n >> i & 1:
                result[i] = xs[i]
            results.add(tuple(result))
    return results
