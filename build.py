def check_student_registration(age, paid):
    if age < 0:
        return "Invalid age"
    elif age < 16:
        return "You are too  young to register"
    elif paid == "no":
        return "Please pay your registration fee"
    elif age >= 16 and paid == "yes":
        return "Registration successful"
    else:
        return "Registration could not completed"

name = input("enter your name")
name = name.strip().lower()

age = int(input("enter your age"))
paid = input("have you pay your registration fee yes/no: ")
paid = paid.strip().lower()

result = check_student_registration(age, paid)
print(name, result)