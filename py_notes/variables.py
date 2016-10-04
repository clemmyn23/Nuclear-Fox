#!/usr/bin/python3

# Experiments with default args in python
# - optional args can be passed in any order
# - all required paramenters (args with NO defualts)
#   must be placed before default args
#

def foo(a=1, b=2, c=3, d=4):
    print("{} {} {} {}".format(a, b, c, d))
    return

foo(9)                  # 9 2 3 4
foo(9,8)                # 9 8 3 4
foo(9,8,7)              # 9 8 7 4
foo(9,8,7,6)            # 9 8 7 6

foo(b = 7)                          # 1 7 3 4
foo(d = 9, c = 8, b = 7, a = 6)     # 6 7 8 9
foo(d = 9)                          # 1 2 3 9
