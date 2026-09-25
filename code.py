skills = ("python", "HTML", "CSS", "flask")
print(skills[0])
print(skills[-1])
print(skills[0:2])
for skill in skills:
    print(skill)

numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))
print(numbers.index(30))

person = ("Debby", 25, "Lagos")
name, age, city, = person
print(name)
print(age)
print(city)


skills = {"python", "HTML", "python", "CSS", "HTML"}
print(skills)

skills = {"python", "HTML"}
skills.add("CSS")
print(skills)
skills.update(["Flask", "SQL"])
print(skills)
skills.discard("HTML")
print(skills)

python_students = {"Debby", "John", "Gabby"}
html_students = {"Debby", "john", "Mike"}
print(python_students & html_students)
print(python_students | html_students)
print(python_students - html_students)

python_students = {"Debby", "John", "Gabby"}
html_students = {"Debby", "john", "Mike"}

clean_python = set()
for name in python_students:
    clean_python.add(name.lower())
print(clean_python)

clean_html = set()
for name in html_students:
    clean_html.add(name.lower())
print(clean_html)

print(python_students & html_students)

python_students = {"Debby", "John", "Gabby"}
html_students = {"Debby", "Mike", "Gabby"}

common_students = python_students & html_students
print(common_students)

python_students = {"Debby", "John", "Gabby"}
html_students = {"Debby", "Mike", "Gabby"}
all_student = python_students | html_students
print(all_student)

python_students = {"Debby", "John", "Gabby"}
html_students = {"Debby", "mike", "Gabby"}
python_only = python_students - html_students
print(python_only)