registrations = [
    ["  DEBBY123    ", "    Toyota ", " Camry ", "2020"],
    ["   JOHN_22  ", "  Honda  ", "  Civic ", "2018"],
    ["  GABBY99  ", "  BMW  ", "  X5  ", "2022"],
    ["  PETER@12  ", "  Ford  ", "  Mustang ", "2021"],
    [" SARAH7 ", "  Mercedes  ", "  C200  ", "2021"]
]

def clean_text(text):
    text = text.strip().lower()
    return text

def validate_username(username):
    username = clean_text(username)
    if username.isalnum():
        return "valid username"
    else:
        return "invalid username"

## validate year usuing nested conditional statement

def validate_year(year):
    if year.isdigit():
        year = int(year)
        if year >= 2000 and year <= 2026:
            return "valid year"
        else:
            return "invalid year"
    else:
        return "invalid year"        

def process_registration(registration):

## proceess the registration

    username = registration[0]
    brand = registration[1]
    model = registration[2]
    year = registration[3]

    username = clean_text(username)
    brand = clean_text(brand)
    model = clean_text(model)

    username_status = validate_username(username)
    year_status = validate_year(year)

## use a nested conditional statment to validate year and username

    if username_status == "valid username":
        if year_status == "valid year":
            print(f"accepted: {brand} {model} - {year}")
            accepted.append(f"{brand} {model}")
        else:
            print("rejected")
    else:
        print("rejected")

index = 0
accepted = []
while index < len(registrations):
    registration = registrations[index]
    for check in range(1, 3):
        print(f"Check {check}")

    process_registration(registration)

    index += 1

    ## summarize the registration using an f-string to print.

print("===== REGISTRATION SUMMARY =====")
print(f"Total registrations: {len(registrations)}")
print(f"Accepted: {len(accepted)}")
print(f"Rejected: {len(registrations) - len(accepted)}")
print("Accepted Vehicles:")
for vehicle in accepted:
    print(vehicle)