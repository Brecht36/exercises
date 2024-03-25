def take_while(xs, condition):
    x = 0
    while x < len(xs) and condition(xs[i]):
        x += 1
    return (xs[:x], xs[x:])   