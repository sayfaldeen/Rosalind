#!/usr/bin/env python3

"""
Code implementing the "Transcribing DNA into RNA" (https://rosalind.info/problems/rna/) Rosalind problem

The goal is to turn a string of DNA into a string of RNA: All this entails is changing T's into U's
    Given: A DNA string, t, having length at most 1000 nt.
    Return: The transcribed RNA string of t

This code will be implemented in 3 ways:
    1) Iteratively
    2) List comprehension
    3) str.replace()

"""

import time


# Iterative implementation
def Iter(s):

    u = ""

    for nt in s:
        if nt == "T":
            u += "U"
        else:
            u += nt

    return u


# List comprehension
def LC(s):

    return "".join(["U" if x == "T" 
            else x
            for x in s])


# str.replace() implementation
def Rep(s):
    return s.replace("T", "U")



#################### Run the functions ####################

print("Small example")
print("="*25)
s = "GATGGAACTTGACTACGTAAATT"

ts = time.time()
Iter(s)
print(f"Iterative solution completed in {time.time() - ts:0.2e} seconds")

ts = time.time()
LC(s)
print(f"ListComp solution completed in {time.time() - ts:0.2e} seconds")

ts = time.time()
Rep(s)
print(f"str.replace() solution completed in {time.time() - ts:0.2e} seconds")


print("Large example")
print("="*25)

s = open("./rosalind_rna.txt", "r").readline()

ts = time.time()
Iter(s)
print(f"Iterative solution completed in {time.time() - ts:0.2e} seconds")

ts = time.time()
LC(s)
print(f"ListComp solution completed in {time.time() - ts:0.2e} seconds")

ts = time.time()
print(Rep(s))
print(f"str.replace() solution completed in {time.time() - ts:0.2e} seconds")


""" #################### Summary ####################
As expected, the str.replace() method was the fastest by a big margin and the ListComp was much faster than the 
    iterative solution by a big margin as well with the full data. Sometimes it is tough to really tell what is
    happening with the small test data sets so going forward, I will only be using the large set

"""

"""
