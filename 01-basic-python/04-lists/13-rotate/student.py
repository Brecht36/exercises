# Write your code here
def rotate(xs, n):
    for i in range(0,n):
        i += 1
        xs.append(xs[0])
        del xs[0]
    return xs