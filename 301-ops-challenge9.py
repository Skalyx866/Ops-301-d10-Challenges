#!/usr/bin/env python3

# importing os library
import os

#declaring variables and name of files
file = "test.txt"
write = open(file, "w")
read = open(file, "r")

lines = ["First", "Second", "Third"]

# declaring the function that writes a file, closes it, opens in read, prints first line to terminal, then deletes.

def filemanip():
# using a for loop to make it easier to write lines
    for line in lines:
        write.write(line + "\n")

# closing the file out of write mode
    write.close()

# opening file in read and reading the first line
    print(read.readline())

# closing file
    read.close

# finishing up by deleting
    os.remove(file)
    print("File is deleted and script is complete!")

filemanip()

