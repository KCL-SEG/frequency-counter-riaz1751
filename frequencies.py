"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        if str(i) not in frequencies.keys():
            frequencies[str(i)] = 1
        else:
            value = frequencies.get(str(i))
            print(value)
            frequencies[str(i)] = value + 1
    return(frequencies)
