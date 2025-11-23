"""
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

submit in python2
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

#try
'''

1
1 2
'''
