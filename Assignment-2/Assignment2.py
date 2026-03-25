# Task - 1

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
    
print()  # Just to add a blank line between tasks
    
# Task - 2

total = 0
for i in range(1, 51):
    total += i

print("The sum of numbers from 1 to 50 is:", total)
