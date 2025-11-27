# reduce tries to reduce it to a single value
# it is not directly available like map and filter but has to be imported from functools
import functools
# it maintains 2 variables value and previously computed value
# like you want to find odd numbers in a list
print(functools.reduce(lambda prev,new:prev+1 if new%2 else prev, [3,3,2,5,7], 0))
# prev is by default first element but we chose to make it 0 


