"""
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
"""
def gradingStudents(grades):
    a=[]
    for grade in grades:
        if grade <38:
            a.append(grade)
        else:
            nm=(grade//5+1)*5
            diff=nm-grade
            if diff<3:
                a.append(nm)
            else:
                a.append(grade)
    return a



#------------- try

grades=[73, 67, 38, 33]

a=gradingStudents(grades)
for i in a:
    print(i)