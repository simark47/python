"""
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
"""
def split_and_join(line):
    a=line.split(" ")
    a=("-").join(a)
    return a

print(split_and_join("hi my name is simarpreet"))