def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

print()

import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number for logarithm and square root.")
else:
    print("Square root:", math.sqrt(num))
    print("Natural logarithm:", math.log(num))
    print("Sine (in radians):", math.sin(num))

