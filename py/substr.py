def rabin_karp(keywords, s):
    """Search ``list`` of keywords in string."""
    R = 256  # radix
    Q = 997  # prime number
    hash_size = min(len(kw) for kw in keywords)

    # precompute R * M^-1 mod Q
    RM = 1
    for i in xrange(1, hash_size):
        RM = (R * RM) % Q

    # build dict of keywords keyed by hash
    hashes = {}
    for kw in keywords:
        h = 0
        for i in xrange(hash_size):
            h = (h * R + ord(kw[i])) % Q
        if h not in hashes:
            hashes[h] = []
        hashes[h].append(kw)

    # search input
    h = 0
    for i, c in enumerate(s):
        if i < hash_size:
            h = (h * R + ord(c)) % Q
        else:
            h = (h + Q - RM * ord(s[i - hash_size]) % Q) % Q
            h = (h * R + ord(c)) % Q
            if h in hashes:
                offset = i - hash_size + 1
                if any(s[offset:offset + len(p)] == p for p in hashes[h]):
                    return True
    return False
