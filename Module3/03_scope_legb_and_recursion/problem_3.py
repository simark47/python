"""
https://leetcode.com/problems/convert-the-temperature/description/
"""

def convertTemperature(celsius: float) :
    Kelvin=celsius + 273.15
    Fahrenheit = celsius * 1.80 + 32.00
    return[Kelvin, Fahrenheit]

print(convertTemperature(celsius = 36.50))