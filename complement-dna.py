#!/usr/bin/env python3


"""
Script to solve the 'Complementing a Strand of DNA' Rosalind problem (https://rosalind.info/problems/revc/)

Generating the reverse complement is done by first reversing the string and then finding its complement
    - C <--> G
    - A <--> T

Given: A DNA string s of length at most 1000 bp

Return: The reverse complement, sc, of s


The algorithm will be implemented in 3 ways:
    1) Iterative
    2) ListComp
    3) Str.replace() [pretty sure this will be the winner]

"""

from time import time


test = "AAAACCCGGT"
ans = "ACCGGGTTTT"


# Pre-set the table
table = {"A":"T",
            "T":"A",
            "C":"G",
            "G":"C"}


# Iterative implementation
def Iter(s):
    sc = ""

    for nt in s[::-1]:
        if nt == "C":
            sc += "G"
        elif nt == "G":
            sc += "C"
        elif nt == "A":
            sc += "T"
        elif nt == "T":
            sc += "A"

    return sc

def Iter2(s):
    sc = ""

    for nt in s[::-1]:
        sc += table[nt]

    return sc


# ListComp implementation
def LC(s):
    
    return "".join([table[nt] for nt in s[::-1]])

def LC2(s):
    
    return [table[nt] for nt in s[::-1]]


# str.replace() method
def Rep(s):
    sc = s[::-1]

    for i in table.keys():
        sc = sc.replace(i, table[i])

    return sc

#################### Run the functions ####################
"""
ts = time()
print(Iter(test) == ans)
print(f"Iterative solution took {time() - ts:0.2e} seconds")

ts = time()
print(Iter2(test) == ans)
print(f"Iterative solution using dict took {time() - ts:0.2e} seconds")

ts = time()
print(LC(test) == ans)
print(f"ListComp solution took {time() - ts:0.2e} seconds")

ts = time()
print(Rep(test) == ans)
print(f"str.replace() solution took {time() - ts:0.2e} seconds")
"""


s = open("./rosalind_revc.txt", "r").readline().strip()

ts = time()
print(Iter(s))
print(f"Iterative solution took {time() - ts:0.2e} seconds")

ts = time()
print(Iter2(s))
print(f"Iterative solution using dict took {time() - ts:0.2e} seconds")

ts = time()
print(LC(s))
print(f"ListComp solution took {time() - ts:0.2e} seconds")

ts = time()
LC2(s)
print(f"ListComp WITHOUT JOIN() solution took {time() - ts:0.2e} seconds")


#ts = time()
#print(Rep(s))
#print(f"str.replace() solution took {time() - ts:0.2e} seconds")


""" #################### Summary ####################
Str.replace() was the fastest, but it was also wrong. Why? Simple, I forgot to account for the fact that when I 
    make the complement of C (G), it may later be transformed back into C (the complement of G) depending on how
    we order the dictionary.

The fastest correct solution is to use a list comp with a look-up dictionary. It is not surprising that the list
    comp is faster than the iterative solution, but one thing slowing the list comp down is that we end to call 
    the join() function on it. It is still 2x faster than the fastest iterative solution, but it does take a 
    small hit.

The final point that is also relatively intuitive; using the look-up table to eliminate the if-statements 
    makes the code faster, but it's not a huge difference.

"""
