#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    results = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            results += 1
    return results
