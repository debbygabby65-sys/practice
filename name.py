name = input("enter your name: ")
age = int(input("enter your age: "))
name = name.strip().title()
if age >= 18:
    print("you are eligible to register!")
else:
    print("you are to young to register")

username = input("enter a username: ")
username = username.strip().lower()
user = input("is_logged_in: ")
user = user.strip().lower()
if username == "debby" and user == "yes":
    print("welcome back, Debby!")
else:
    print("Access denied.")



