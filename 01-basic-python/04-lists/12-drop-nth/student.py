# Write your code here
def drop_nth(xs, n):
    ys = list()
    ys += xs
    del ys[n]
    return ys