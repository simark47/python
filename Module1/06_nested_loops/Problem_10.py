"""
https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true
"""

for i in range(1,int(input())):
    print(((10**i-1)//9)*i)



'''
logic:
THINK OF
i=1 and not updating
1
11
111
1111
str(i)*i  BUT we can not use str

9
99
999
9999
divide by 9 gives 1


10-1
100-1
1000-1
1000-1

(10 power i- 1)
(10 power i- 1)//9
 will give 

1
11
111
1111
 and lets multiply with i
1
22
333
4444
'''





