def run(w):
    for n in xrange(2 ** w):
        yield to_bits(w, (n >> 1) ^ n)

def to_bits(w, n):
    s = bytearray('0' * w)
    mask = 1
    for i in xrange(w):
        if n & mask:
            s[w - 1 - i] = ord('1')
        mask <<= 1
    return s
