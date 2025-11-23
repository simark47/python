"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #code here
    new=student_marks[query_name]
    
    print(f"{sum(new)/len(new):.2f}")
   


#try

'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''
