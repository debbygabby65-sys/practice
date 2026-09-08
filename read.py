name = "Gabby"

def show_name():
    name = "Debby"
    print(name)

show_name()
print(name)

global_status = "Not processed"

def process_name(name):
    name = name.strip().lower()

    if not name.isalpha():
        return "Invalid name"
    status = "Valid"

    return name, status

name = "   DEBBY "

name, status = process_name(name)
print(f"Name: {name}")
print(f"Status: {status}")
print(f"Global_status: {global_status}")

def clean_text(text):
    text = text.strip().lower()
    return text

def process_account(name, email):
    name = clean_text(name)
    email = clean_text(email)

    if not name.isalpha():
        return "Invalid name"
    if "@" not in email:
        return "Invalid email"

    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    return name, username, domain

name = "    DEBBY   "
email = "     DEBBY@GMAIL.COM  "

name, username, domain = process_account(name, email)
print(f"Name: {name}")
print(f"Username: {username}")
print(f"Domain: {domain}")


count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(count)

global_status = "Not processes"

def process_username(username):
    username = username.strip().lower()

    if not username.isalnum():
        return "Invalid username"
    status = "Valid"
    return username, status

username = "   DEBBY123   "
username, status = process_username(username)
print(f"Username: {username}")
print(f"status: {status}")
print(f"Global_status: {global_status}")
