# Write your code here
def to_list_of_pairs(dictionary):
    list = []
    for x, y in dictionary.items():
        pair = (x, y)
        list.append(pair)
    return list