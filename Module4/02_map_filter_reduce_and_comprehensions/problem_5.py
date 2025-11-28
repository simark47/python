# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

li = input().split()
n = int(li[0])
r = int(li[1])

b = []
for _ in range(r):
    row = list(map(float, input().split()))
    b.append(row)
# transpose
s = list(zip(*b))
def avg(li):
  return f"{sum(li)/len(li):.1f}";
t=list(map(float,(map(avg, s))))
for i in t:
  print(i)
        

# or
li = input().split()
co = int(li[0])
ro = int(li[1])

b = []
# logic
for _ in range(ro):
    row = list(map(float, input().split()))
    b.append(row)

result = []
for c in range(co):
    temp = []
    for r in range(ro):
        temp.append(b[r][c])
    result.append(temp)


def avg(li):
  return f"{sum(li)/len(li):.1f}";
t=list(map(float,(map(avg, result))))
for i in t:
  print(i)
        

# or
n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]

for i in zip(*marks):
    print(sum(i) / x)


"""
input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

"""