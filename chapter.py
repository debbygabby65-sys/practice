def clean_name(name):
    name = name.strip().lower()
    return name

def process_name(name):
    name = clean_name(name)
    if not name.isalpha():
        return "Invalid name"
    else:

        return f"Name: {name}, Status: Valid"


name = "   DEBBY   "
result = process_name(name)
print(f"Result: {result}") 


def process_user(name, username):
    name = name.strip().lower()
    username = username.strip().lower()

    if not name.isalpha():
        return "Invalid name"

    if not username.isalnum():
        return "Invalid username"
         
    else:
        
        return f"Name: {name}, Username: {username}, Status: Valid"

name = "   DEBBY   "
username = "   DEBBY123  "

result = process_user(name, username)
print(f"Result: {result}")

def greet_user(name, greeting="Hello"):
    return f"{greeting} {name}!"

result = greet_user(name="Debby", greeting="Welcome")
print(result)


def create_username(name, prefix="user"):
    name = name.strip().lower()
    return f"{prefix}_{name}"

result = create_username(name="   DEBBY  ", prefix="admin")
print(result)

    
def process_name(name):
    name = name.strip().lower()
    length = len(name)

    return name, length

name = "       DEBBY   "

clean_name, name_length = process_name(name)
print(f"Clean_name: {clean_name}")
print(f"Name_length: {name_length}")


def process_email(email):
    email = email.strip().lower()

    if '@' not in email:
        return None, None

    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    return username, domain

email = "     DEBBY@GMAIL.COM  "

username, domain = process_email(email)

print(f"Username: {username}")
print(f"Domain: {domain}")


def process_user(name, username):
    name = name.strip().lower()
    username = username.strip().lower()

    if not name.isalpha():
        return "Invalid name"
    if not username.isalnum():
        return "Invalid username"
    return name, username, "Valid"

name = "   DEBBY  "
username = "     DEBBY123  "

cleaned_name, cleaned_username, status = process_user(name, username)
print(f"Cleaned_name: {cleaned_name}")
print(f"Cleaned_username: {cleaned_username}")
print(f"Status: {status}")


def process_account(name, email):
    name = name.strip().lower()
    email = email.strip().lower()

    if not name.isalpha():
        return "Invalid name"
    if "@" not in email:
        return "Invalid email"
    
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    return name, username, domain 

name = "    DEBBY   "
email = "   DEBBY@GMAIL.COM   "

cleaned_name, email_username, email_domain = process_account(name, email)
print(f"Cleaned_name: {cleaned_name}")
print(f"Email-username: {email_username}")
print(f"Email_domain: {email_domain}")