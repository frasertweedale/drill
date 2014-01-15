def threesum(l):
    results = set()
    n = len(l)
    indices_by_value = {}
    for i in xrange(n):  # O(n) to build the hashmap
        indices_by_value[l[i]] = i
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                continue
            twosum = -l[i] - l[j]
            k = indices_by_value.get(twosum)
            if k is not None and i != j and i != k and j != k:
                results.add(frozenset({l[i], l[j], twosum}))
    return results
