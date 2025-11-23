"""
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""
if __name__ == '__main__':
    N = int(input())
    a=[]
    while N>0:
        stri=input()
        list=stri.split(" ")
        operator=list[0]
        
        if operator=="insert":
            a.insert(int(list[1]), int(list[2]))
        elif operator=="print":
            print(a)
        elif operator=="remove":
            a.remove(int(list[1]))
        elif operator=="append":
            a.append(int(list[1]))
        elif operator=="sort":
            a.sort()
        elif operator=="pop":
            a.pop()
        elif operator=="reverse":
            a.reverse()
  
        N-=1
