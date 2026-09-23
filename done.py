first_name = "DEBBY"
last_name = "GABBY"

first_name = first_name.lower()
last_name = last_name.lower()

full_name = first_name + " " + last_name
print(full_name)

brand = "Toyata"
model = "Camry"
year = 2020

car = f"{brand} {model} was made in {year}"
print(car)

name = "    DEBBY  "
email =  "      DEBBY@GMAIL.COM     "

name = name.strip().lower()
email = email.strip().lower()

print("Name:", name)
print("Email:", email)


def process_names(names):
    result = []
    for name in names:
        name = name.strip().lower()

        if name.isalpha():
            result.append(name)
        else:
            print(f"Rejected: {name}")
    return result

names = [
    "   DEBBY   ",
    "   Gabby   ",
    "   JOHN123 ",
    "   mary    ",
    "Peter_12",
    "   SARAH   "
]

accepted_names = process_names(names)

print(accepted_names)

def process_usernames(usernames):
    for username in usernames:
        username = username.strip().lower()

        if username.isalnum():
            print(f"Accecpted: {username}")
        else:
            print(f"Rejected: {username}")

usernames = [
    "   DEBBY123    ",
    "   Gabby_22    ",
    "   JOHN    ",
    "   Peter@123  ",
    "   SARAH99 "
]

answer = process_usernames(usernames)
print(answer)


number = 1
while number < 11:
    if number % 2 == 0:
        print(f"Even: {number}")
    else:
        print(f"Odd: {number}")
 
    number += 1

age = 10
while age < 21:
    if age >= 18:
        if age >= 21:
            print(f"Adult: {age}")
        else:
            print(f"18-20: {age}")
    if age < 18:
        print(f"Minor: {age}")
    age += 1



numbers = [1, 2, 3]
for number in numbers:
    for inner_number in range(1,4):
        print(f"Number: {number}, Inner_number: {inner_number}")


names = [
    "   DEBBY   ",
    "   JOHN123 ",
    "   GABBY   "

]

index = 0

while index < len(names):
    name = names[index]
    name = name.strip().lower()

    for check in range(1, 3):
        if name.isalpha():
            print(f"Valid: {name} - Check {check}")
        else:
            print(f"Invalid: {name} - Check {check}")

    index +=1