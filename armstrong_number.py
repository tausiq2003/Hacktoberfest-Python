import math

def isArmstrong(num):
    no_of_digits = math.floor(math.log10(num)) + 1
    safe = num
    res = 0
    while(num != 0):
        res += pow((num % 10), no_of_digits)
        num //= 10
    return res == safe

try:
    num = int(input("Enter a number:"))    
    print(isArmstrong(num))
except ValueError:
    print("Please enter a non-negative number!")    
