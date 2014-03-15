def insertion_sort(xs):
    for i in xrange(len(xs) - 1):
        min_index = i
        for j in xrange(i + 1, len(xs)):
            if xs[j] < xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]


def selection_sort(xs):
    for i in xrange(1, len(xs)):
        j = i
        while j > 0 and xs[j] < xs[j - 1]:
            xs[j], xs[j - 1] = xs[j - 1], xs[j]
            j -= 1
