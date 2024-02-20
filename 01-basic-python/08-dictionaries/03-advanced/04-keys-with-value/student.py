# Write your code here
def keys_with_value(dic, value):
    new_dic = []
    for key in dic:
        if dic[key] == value:
            new_dic.append(key)
    return new_dic