"""
Created on Thu Jul 23 14:58:28 2020
    est to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input
and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged.
You’re welcome,but not required, to prompt the user explicitly,
as by passing a str of your own as an argument to input.
@author: Eppy
"""

name = input("Whats your name? ")
name  = name.lower().strip()
print(name)  