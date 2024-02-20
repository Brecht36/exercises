# Write your code here
def remove_duplicates(xs):
    ys = list()
    ss = set()
    for i in xs:
        if i not in ss:
            ys.append(i)
            ss.add(i)
    return ys