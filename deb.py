import calculator
result = calculator.multiply_numbers(6, 4)
print(result)

import calculator
name = "    DEBBY  "
result = calculator.clean_name(name)
print(result)

import calculator
username = "    DEBBY123    "
answer = calculator.validate_username(username)
print(answer)

import calculator
name = "    DEBBY   "
result = calculator.process_name(name)
print(result)

import calculator
name = "  DEBBY   "
username = "  DEBBY123    "

solution = calculator.validate_name(name)
answer = calculator.validate_username(username)
print(solution)
print(answer)

import calculator
registrations = [
    ["   DEBBY123    ", "2020"],
    ["  JOHN_22 ", "2018"],
    ["  GABBY99 ", "2022"]
]
index = 0
while index < len(registrations):
    registration = registrations[index]

    username = registration[0]
    year = registration[1]
    username_status = calculator.validate_username(username)
    year_status = calculator.validate_year(year)
    print(username_status)
    print(year_status)
    index += 1