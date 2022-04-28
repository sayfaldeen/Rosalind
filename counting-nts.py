#!/usr/bin/env python3

"""
Problem: [Counting DNA nucleotides](https://rosalind.info/problems/dna/)

Given: A DNA string, s, of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

This solution will be implemented using multiple approaches:
    1) ListComp
    2) For-loop
    3) regex
    4) collections.Counter
    5) str.count()

"""


import time
import re
from collections import Counter


s = "AGCTTTTCATT"

# ListComp approach
def LC(s):
    "ListComp implementation"

    a_count = sum([1 for n in s if n == "A"])
    c_count = sum([1 for n in s if n == "C"])
    g_count = sum([1 for n in s if n == "G"])
    t_count = sum([1 for n in s if n == "T"])

    return a_count, c_count, g_count, t_count

# ListComp with regex
def LCR(s):
    "ListComp with regex implementation"
    
    [print(len(re.findall(x, s)), end=" ") for x in ["A", "C", "G", "T"]]
    

# Iterative approaches
def Iter(s):
    "Basic iterative approaches"
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for n in s:
        if n == "A":
            a_count += 1
        elif n == "C":
            c_count += 1
        elif n == "G":
            g_count += 1
        else:
            t_count += 1


    return a_count, c_count, g_count, t_count
    

def Iter2(s):
    "Iterative implementation examining else vs elif performance"

    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for n in s:
        if n == "A":
            a_count += 1
        elif n == "C":
            c_count += 1
        elif n == "G":
            g_count += 1
        elif n == "T":
            t_count +=1


    return a_count, c_count, g_count, t_count


def CC(s):
    "collections.Counter implementation"

    res = dict(Counter(s))

    [print(res[x], end=" ") for x in "ACGT"]

def SC(s):
    "String.count() implementation"

    return s.count("A"), s.count("C"), s.count("G"), s.count("T")


#################### Run the functions ####################
print("Small string comparison")
print("="*25)

ts = time.time()
print(LC(s))
print(f"ListComp implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
LCR(s)
print(f"\nListComp WITH REGEX implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
print(Iter(s))
print(f"Iterative implementation using ELSE took {time.time() - ts:0.2e}\n")

ts = time.time()
print(Iter2(s))
print(f"Iterative implementation using ELIF took {time.time() - ts:0.2e}\n")

ts = time.time()
CC(s)
print(f"\nCounter implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
print(SC(s))
print(f"Str.count implementation took {time.time() - ts:0.2e}\n")


####################################################################################################


print("LARGE string comparison")
print("="*25)
 
s = open("./rosalind_dna.txt", "r").readline()

ts = time.time()
print(LC(s))
print(f"ListComp implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
LCR(s)
print(f"\nListComp WITH REGEX implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
print(Iter(s))
print(f"Iterative implementation using ELSE took {time.time() - ts:0.2e}\n")

ts = time.time()
print(Iter2(s))
print(f"Iterative implementation using ELIF took {time.time() - ts:0.2e}\n")


ts = time.time()
CC(s)
print(f"\nCounter implementation took {time.time() - ts:0.2e}\n")

ts = time.time()
print(SC(s))
print(f"Str.count implementation took {time.time() - ts:0.2e}\n")



""" #################### Summary ####################

Here we see that the basic iterative solution is the fastest (with no difference between using elif or else) FOR 
    THE SMALL DATA.

However, when we use a larger string, we see that the counter approaches are the fastest. Why? These approaches
    have some associated overhead for importing and being called but this overhead becomes more and more trivial as 
    the data gets larger.

Finally, why is str.count() faster than Counter()? str.count() is wirtten in CPython and has a more efficient
    implementation whereas Counter() inherits from the python dict class and requires multiple calls per value.

Summary of summary: Use str.count() for count occurences in a string; data will almost never be so small where the 
    overhead will be big enough to hurt, but that data will very often be much larger. Also, if you need more than 
    just counts, ListComp with a regex is a pretty good solution, but for basic counting, it is 10x slower than 
    the str.count() method.

"""
