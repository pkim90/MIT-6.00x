from string import *
#
# Write two functions, called countSubStringMatch and
# countSubStringMatchRecursive that
# take two arguments, a key string and a target string.
# These functions iteratively and recursively count
# the number of instances of the key in the target string.
# You should complete definitions for
# def countSubStringMatch(target,key):
# and
# def countSubStringMatchRecursive (target, key):
# Place your answer in a file named ps3a.py
#
# # find("atgacatgcacaagtatgcat","atgc")
# # returns the value 5, while
# # find("atgacatgcacaagtatgcat","atgc",6)
# # returns the value 15,

def countSubStringMatch(target, key):

    x = 0
    total = 0
    while find(target, key, x) > 0:
        find(target, key, x)
        total = total + 1
        x = find(target, key, x)
    return total

def countSubStringMatchRecursive(target, key):

    x = 0
    total = 0
    if find(target,key) < 0:
        return total
    while find(target,key) > 0:

        x = find(target,key)
        target = target[x:]
        total = total + 1
        return countSubStringMatchRecursive(target, key)
