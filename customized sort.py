# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from functools import cmp_to_key


class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def mycmp(a, b):
    if a.x < b.x:
        return -1
    elif a.x > b.x:
        return 1
    else:
        if a.y < b.y:
            return -1
        elif a.y > b.y:
            return 1
        else:
            return 0


alist = [point(2, 3), point(2, 2), point(0, 0), point(0, 1)]
alist.sort(key=cmp_to_key(mycmp))

for a in alist:
    print(a.x, a.y)


# b=[4,2,1]
# b.sort(key = lambda x: x)
# print(b)
