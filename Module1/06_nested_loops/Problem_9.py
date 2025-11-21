"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
"""
def dayOfProgrammer(year):
    date=""
    if year<1918:
        if(year %4==0):
            date="12.09."+str(year)
        else:
            date="13.09."+str(year)

    elif year ==1918:
        date="26.09.1918"

    elif year>1918:
        if(year %4==0):
            if(year%100==0):
                if(year%400==0):
                    date="12.09."+str(year)
                else:
                    date="13.09."+str(year)
            else:
                date="12.09."+str(year)
        else:
            date="13.09."+str(year)

    print( date)
#try------------
dayOfProgrammer(1918)
dayOfProgrammer(2000)
dayOfProgrammer(2003)
dayOfProgrammer(1900)
dayOfProgrammer(1600)
dayOfProgrammer(1704)
dayOfProgrammer(2100)