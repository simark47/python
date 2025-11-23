"""
http://hackerrank.com/challenges/capitalize/problem?isFullScreen=true
"""
def solve(s):
    s=s.split(" ")
    print(s)
    for i in range(len(s)):
      for j in range(len(s[i])):
        if j==0:
           a=s[i][j].capitalize()
           s[i]=a+s[i][j+1:]
    s=(" ").join(s)      
    return(s)
        



#try
print(solve("chris alan"))