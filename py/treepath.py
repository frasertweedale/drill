def treepath(root, a, b):
    path_to_a = path(root, a)
    path_to_b = path(root, b)
    i = 0
    while path_to_a[i] == path_to_b[i]:
        i += 1
    last_common = i - 1
    return path_to_a[-1:last_common:-1] + path_to_b[last_common:]


def path(root, a):
    if root is None:
        return None
    elif root == a:
        return [root]
    else:
        if root.l:
            lpath = path(root.l, a)
            if lpath is not None:
                return [root] + lpath
        if root.r:
            rpath = path(root.r, a)
            if rpath is not None:
                return [root] + rpath
    return None  # target not found in either branch
