student_marks = {
    "Sonu": 85,
    "Sujit": 78,
    "Shailesh": 92,
    "Mohit": 88
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")

print()

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_first_five = first_five[::-1]

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_first_five)
