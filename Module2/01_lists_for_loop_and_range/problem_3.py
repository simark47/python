'''
https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
'''
def birthdayCakeCandles(candles):
    maxi=max(candles)
    count=0
    for i in candles:
        if i==maxi:
            count+=1
    return count


#try:
candles=[3, 2 ,1, 3]
print(birthdayCakeCandles(candles))