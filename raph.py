def  add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(50, 25)
    print(result)

for username in range(5):
    username = input("Enter your username:")
    if username == "admin":
        print("Access granted")
    else:
        print("Access denied")

for username in range(3):
    username = input("Enter your fucking name:")
    if username == "admin":
        age = int(input("Enter your age:"))
        if age >= 18:
            print("Access granted")
        else:
            print("Too young")
    else:
        print("Invalid username") 

for outer in range(1, 4):
    for inner in range(1, 3):
        print(outer, inner)

for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

for outer in range(1, 4):
    for inner  in range(1, 6):
        if inner % 2 == 0:
            print(inner, "is even")
        else: 
            print(inner, "is odd")