def  check_student_result(age, score):
    if age < 0:
        return "Invalid age"
    elif score < 0 or score > 100:
        return "Invalid score"
    elif age < 16:
        return "You not eligible for this program"
    elif score >= 70:
        return "Excellent - Grade A"
    elif score >= 60:
        return "Very good - Grade B"
    elif score >= 50:
        return "Good Grade C"
    elif score >= 40:
        return "Pass - grade D"
    else:
        return "Fail - Grade F"


name = input("enter your name: ")
name = name.strip().title()

age = int(input("enter your age: "))
score = int(input("enter your score: "))

result = check_student_result(age, score)
print(name, result)