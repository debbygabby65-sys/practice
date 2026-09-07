email = "  JOHN@YAHOO.COM"

parts = email.strip().lower().split('@')

print(parts[0])
print(parts[1])

email = "       DEBBY@GMAIL.COM        "
parts = email.strip().lower().split('@')
print(parts[0])
print(parts[1])

words = ["I", "love", "python"]
sentence = " ".join(words)
print(sentence)

names = ["Debby", "john", "peter"]
sentence = "-".join(names)
print(sentence)

parts = ["debby", "gmail.com"]
sentence = "@".join(parts)
print(sentence)

email = "john@yahoo.com"

parts = email.split('@')

email = "@".join(parts)
print(email)


email = "           DEBBY@GMAIL.COM       "

parts = email.strip().lower().split('@')
print(parts[0])
print(parts[1])
email = "@".join(parts)
print(email)

number = "12345"
name = "Debby"
username = "Debby123"
print(number.isdigit())
print(name.isalpha())
print(username.isalpha())

a = "Debby123"
b = "Debby_123"
c = "12345"
d = "Debby"
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

a = "    "
b = "Debby"
c = "   Debby   "
d = "\t"
print(a.isspace())
print(b.isspace())
print(c.isspace())
print(d.isspace())

username = "Debby123"
password = "DEBBY2026"
name = "Debby"
space = "     "
number = "12345"
print(username.isalnum())
print(password.isalnum())
print(name.isalpha())
print(space.isspace())
print(number.isdigit())

username = "Debby_123"

if username.isalnum():
    print("Valid username")
else:
    print("Invalid username")


username = "Brownstyle_123"
if username.isalpha():
    print("Letters only")
elif username.isalnum():
    print("Letters and numbers")
else:
    print("Contain special characters")


name = "Debby"
age = 25
print(f"my name is {name} iam {age} years old!")

price = 500
quantity = 4
print(f"total price: {price * quantity} naira")

username = "   DEBBY-GABBY  "
print(f"{username.strip().lower().replace('-', '')}")

name = "Debby"
email =  "    DEBBY@GMAIL.COM  "
parts = email.strip().lower().split('@')
print(f"user: {name}")
print(f"Email username: {parts[0]}")
print(f"Email domain {parts[1]}")

product = "  LAPTOP   "
price  = 350000
quantity = 2
print(f"total price: {product.strip().lower()} {price * quantity}")


first_name = "Debby"
last_name = "Gabby"
age = 25
username = "    DEBBY-GABBY   "
print(f"{first_name} {last_name} {age} {username.strip().lower().replace('-', ' ')}")
