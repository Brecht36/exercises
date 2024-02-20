# Write your code here
def double_dict_values(dic):
    new_dic = {}
    for key in dic:
        new_key = dic[key] * 2
        new_dic[key] = new_key
    return new_dic