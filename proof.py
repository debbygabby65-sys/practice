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

print("===== STUDENT RESULT SYSTEM =====")
print("Register student")
print("Calculate average")
print("Display grade")
print("Display pass or fail")
print("Exit")

choice = input("Enter your choice: ")

if  choice == "1":
    print("Register student.")
elif choice == "2":
    print("Calculate average.")
elif choice == "3":
    print("Display grade.")
elif choice == "4":
    print("Display pass or fail.")
elif choice == "5":
    print("Exiting program.")
else:
    print("Invalid choice.")
    
running = True
while running:
    print("welcome to python")
    running = False    

students = {}
name = input("Enter a student's name")
students[name] = [] 
score = int(input("Enter a score: "))
students[name].append(score)
print(student)
scores = []
for number in range(3):
    score = int(input("Enter a score: "))
    scores.append(score)
    print(score)
students = {}
name = input("Enter a name: ")
students[name] = []
print(students)