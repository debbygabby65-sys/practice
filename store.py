sales = [1200, 800, 1500, 700, 1800]
total = sum(sales)
print("Total sales: ", total)
number_of_days = len(sales)
print("Number of days: ", number_of_days)
average = total/number_of_days
print(average)

scores = [67, 89, 45 , 92, 56, 78, 34, 85]
higest_score = max(scores)
print("Higest score: ", higest_score)
lowest_score = min(scores)
print("Lowest score: ", lowest_score)
total = sum(scores)
Number_of_student = len(scores)
average = total / Number_of_student
print("Average: ", average)

def check_student_scores():
    students = {
        "Debby": [78, 85, 69],
        "John": [45, 52, 48],
        "Mary": [90, 92, 88],
        "Peter": [33, 40, 38],
        "Sarah": [60, 55, 65]
    }
    for student in students:
        scores = students[student]
        total = sum(scores)
        Number_of_subject = len(scores)
        average = total / Number_of_subject
        print(f"{student}: {average:.2f}")
        if average >= 70:
            print("Grade A")
        elif average >= 60:
            print("Grade B")
        elif average >= 50:
            print("Grade C")
        elif average >= 45:
            print("Grade D")
        else:
           print("Grade F")
        if average >= 50 and all(score >= 40 for score in scores):
            print("pass")

        else:
            print("fail") 
           
check_student_scores()