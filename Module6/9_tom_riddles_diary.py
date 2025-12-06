"""
https://app.programmingpathshala.com/python/module/406?topicId=417&subTopicId=4097
"""
n=int(input())
a=[]
for _ in range(n):
    i=input()
    if(i in a):
        print("YES")
    else:
        print("NO")
        a.append(i)