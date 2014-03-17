import math


def points_form_square(points):
    p0 = points[0]
    dist = lambda a, b: math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    dist_from_p0 = lambda p: dist(p0, p)
    points = sorted(points, key=dist_from_p0)
    if dist(points[0], points[1]) != dist(points[0], points[2]):
        return False
    if dist(points[0], points[1]) >= dist(points[0], points[3]):
        return False
    if dist(points[0], points[3]) != dist(points[1], points[2]):
        return False
    return True
