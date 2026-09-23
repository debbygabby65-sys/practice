def multiply_numbers(a, b):
    return a * b

def  clean_name(name):
    name = name.strip().lower()
    return name

def validate_username(username):
    username = clean_name(username)
    if username.isalnum():
        return "valid username"
    else:
        return "invalid username"

def clean_text(text):
    text = text.strip().lower()
    return text

def process_name(name):
    name = clean_text(name)
    if name.isalpha():
        return "valid name"
    else:
        return "invalid name"

def clean_text(text):
    text = text.strip().lower()
    return text

def validate_name(name):
    name = clean_text(name)
    if name.isalpha():
        return "valid name"
    else:
        return "invalid name"

def validate_username(username):
    username = clean_text(username)
    if username.isalnum():
        return "valid username"
    else:
        return "invalid username"

def clean_text(text):
    text = text.strip().lower()
    return text

def validate_username(username):
    username = clean_text(username)
    if username.isalnum():
        return "valid username"
    else:
        return "invalid username"

def validate_year(year):
    if year.isdigit():
        year = int(year)
        if year >= 2000 and year <= 2026:
            return "valid year"
        else:
            return "invalid year"
