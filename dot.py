def clean_name(name):
    name = name.strip().lower()
    return name


result = clean_name("   DEBBY   ")
print(f"clean_name: {result}")

def validate_username(username):
    username = username.strip().lower()

    if username.isalnum():
        return "Valid username"
    else:
        return "Invalid username"


answer = validate_username("   DEBBY123   ")

print(f"validate_username: {answer}")


def process_email(email):
    email = email.strip().lower()
    
    if "@" not in email:
        return "Invalid email"
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]

    return f"Username: {username}, Domain: {domain}"

result = process_email("     DEBBY@GMAIL.COM  ")

print(f"process_email: {result}")
    

def process_username(username):
    username = username.strip().lower()
    if not username.isalnum():
        return "Invalid username"
    else:
        return f"Username: {username}, Status: valid"


result = process_username("    DEBBY123   ")
print(f"Result: {result}")


def process_phone(phone):
    phone = phone.strip()
    if not phone.isdigit():
        return "Invalid phone number"
    else:
        return f"Phone: {phone}, Status: Valid"
phone = "08012345678"
result = process_phone(phone)

print(f"Result: {result}")

def process_name(name):
    name = name.strip().lower()
    if not name.isalpha():
        return "Invalid name"
    else:
        return f"Name: {name}, Status: Valid"
name = "   DEBBY   "
result = process_name(name)


print(f"Result: {result}")

def process_email(email):
    email = email.strip().lower()
    if '@' not in email:
        return "Invalid email"
    else:
        parts = email.split('@')
        username = parts[0]
        domain = parts[1]
        
        return f"Email: {email}, Username:{username}, Domain: {domain}"

email = "       DEBBY@GMAIL.COM"
result = process_email(email)
print(f"Result: {result}")
