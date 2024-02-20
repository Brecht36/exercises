# Write your code here
def merge_dicts(dict_one, dict_two):
    new_dict = {}
    for key in dict_one:
        if key not in dict_two:
            new_dict[key] = dict_one[key]
    for key in dict_two:
        new_dict[key] = dict_two[key]
    return new_dict