product = "Laptop"
price = 350000
quantity = 2 
total_cost = price * quantity
print("Price: ", price)
print("Quantity: ", quantity)
print("Total_cost: ", total_cost)

worker_name = "Debby"
daily_pay = 8000
number_of_days_worked = 22
total_earning = daily_pay * number_of_days_worked
print("Worker_name: ", worker_name)
print("Total_earning: ", total_earning)

running = True
students = {}

while running:
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Register student")
    print("2. Calculate average")
    print("3. Display grade")
    print("4. Display pass or fail")
    print("5. Exit")

    choice = input("Enter a choice: ")

    if choice == "1":
        name = input("Enter student's name: ")
        students[name] = []

        for number in range(3):
            score = int(input(f"Enter score {number + 1}: "))
            students[name].append(score)

        total = sum(students[name])
        average = total / len(students[name])

        print("\nStudent registered successfully!")
        print("Student name:", name)
        print("Scores:", students[name])
        print("Total:", total)
        print("Average:", round(average, 2))

    elif choice == "2":
        name = input("Enter student's name: ")

        if name in students:
            total = sum(students[name])
            average = total / len(students[name])
            print("Average:", round(average, 2))
        else:
            print("Student not found. Register the student first.")

    elif choice == "3":
        name = input("Enter student's name: ")

        if name in students:
            average = sum(students[name]) / len(students[name])

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
        else:
            print("Student not found. Register the student first.")

    elif choice == "4":
        name = input("Enter student's name: ")

        if name in students:
            average = sum(students[name]) / len(students[name])

            if average >= 50:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found. Register the student first.")

    elif choice == "5":
        print("Exiting program.")
        running = False

    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Student Result System!")
