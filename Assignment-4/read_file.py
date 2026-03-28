try:
    print("Reading file content:")
    
    with open("sample.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

print()

text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.\n")

print("Final content of output.txt:")

with open("output.txt", "r") as file:
    print(file.read())
