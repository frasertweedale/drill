def binary_search(x, error):
    """sqrt via binary search, with error margin"""
    if x < 0:
        return -1
    else:
        # watch out for float rounding errors
        if x > 1:
            lo = 0.0
            hi = x
        else:
            lo = x
            hi = 1
        while abs(hi - lo) > error:
            mid = lo + (hi - lo) / 2
            if mid ** 2 < x:
                lo = mid
            else:
                hi = mid
        return lo


def newton(n, error):
    """Newton's method with poor initial guess of n."""
    x = n
    while abs(x ** 2 - n) > error:
        x = x - (x ** 2 - n) / (2 * x)
    return x
