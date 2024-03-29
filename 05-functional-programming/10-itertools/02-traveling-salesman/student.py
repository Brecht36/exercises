from itertools import pairwise, permutations

def find_shortest_path(distance, city_count):
    def total_distance(path):
        return sum(distance(a,b) for a,b in list(pairwise(path)))
    routes = [[0, *p, 0] for p in permutations(range(1, city_count))]
    return  min(routes, key=total_distance)

def distance(a, b):
    return abs(a - b)