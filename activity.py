with open("student.txt", "w") as file:
    file.write("my name is Debby\n")
    file.write("I am learning python")

with open("student.txt", "a") as file:
    file.write("\nI am practicing file handling")

with open("student.txt", "r") as file:
    content = file.read()
print(content)


with open("note.txt", "w") as file:
    file.write("my name is Debby\n")
    file.write("I am learning python")
    file.write("\n I am practicing file handling")

with open("note.txt", "r") as file:
    lines = file.readlines()
print(lines)


with open("note.txt", "w") as file:
    file.write("my name is Debby\n")
    file.write("I am learning python")
    file.write("\n I am practicing file handling")

with open("note.txt", "r") as file:
    lines = file.readlines()
print(lines[0])
print(lines[1])
print(lines[2])

lines = [
        "Debby\n",
        "John\n",
        "Sarah\n"
]

with open("students.txt", "w") as file:
    file.writelines(lines)

with open("students.txt", "r") as file:
    lines = file.readlines()
    
print(lines)