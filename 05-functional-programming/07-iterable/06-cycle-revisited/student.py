def cycle(xs):
    xs = list(xs)
    while True:
        for x in xs:
            yield x