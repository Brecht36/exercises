# Write your code here
def median(ns): 
    sort = sorted(ns)
    mid = len(sort) // 2

    if len(sort) % 2 == 0:
        return (sort[mid - 1] + sort[mid]) / 2
    else:
        return sort[mid]
