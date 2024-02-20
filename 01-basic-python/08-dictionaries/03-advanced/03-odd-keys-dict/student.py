# Write your code here
def odd_keys_dict(dic):
    new_dic = {}
    for key in dic:
        if key / 2 != key // 2:
            new_dic[key] = dic[key]
    return new_dic

#odd_keys_dict({1: 'a', 2: 'b', 3: 'c'})