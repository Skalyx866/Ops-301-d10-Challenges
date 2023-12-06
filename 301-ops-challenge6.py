#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables
path = input("Please enter a file path ")

### Read user input here into a variable

# Declaration of functions

### Declare a function here

def oswalk (path):
    for root, dirs, files in os.walk(path):
    ### Add a print command here to print ==root==
        print(root)
    ### Add a print command here to print ==dirs==
        print(dirs)
    ### Add a print command here to print ==files==
        print(files)

# Main
if __name__ == "__main__":
    oswalk(path)
### Pass the variable into the function here


# End