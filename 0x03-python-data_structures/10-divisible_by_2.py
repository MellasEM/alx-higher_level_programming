#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2 = []
    for i in my_list:
        div_2.append(i % 2 == 0)
    return div_2
