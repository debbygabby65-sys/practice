profile = ["Debby", "Lagos", 25]
profile_copy = profile.copy()
profile_copy[0] = "Gabby"
print(profile)
print(profile_copy)

profile = ["Debby", "Lagos", 25]
profile_copy = profile.copy()
profile_copy[0] = "Gabby"
profile_copy[2] = 30
print(profile)
print(profile_copy)




def add_numbers(a, b):
    return a + b
result = add_numbers(50, 10)
print(result)

person = {
    "name": "Debby",
    "age": 25,
    "city": "Lagos",
    "skill": "Python"
}

print(person["name"])
print(person["skill"])
person["age"] = 30
print(person["age"])
person["country"] = "Nigeria"
print(person["country"])

for key, value in person.items():
    print(key, value)

student = {
    "name": "Debby",
    "skills": ["python", "HTML", "CSS"]
}
print(student["name"])
print(student["skills"][0])
print(student["skills"][1])
print(student["skills"][2])

person = {
    "name": "Debby",
    "age": 25,
    "address": {
        "city": "Lagos",
        "country": "Nigeria"
    }
}
print(person["name"])
print(person["address"]["city"])
print(person["address"]["country"])
person["address"]["city"] = "Abuja"
print(person["address"]["city"])
person["address"]["state"] ="FCT"
print(person["address"])

people = {
    "user1": {
        "name": "Debby",
        "age": 25
    },
    "user2": {
        "name": "John",
        "age": 30, 
    },
    "user3": {
        "name": "Gabby",
        "age": 22
    },
}


print(people["user1"]["name"])
print(people["user2"]["age"])
people["user3"]["age"] = 23
print(people["user3"]["age"])
people["user1"]["city"] = "Lagos"
print(people["user1"])

for user, details in people.items(): 
    print(details["name"], details["age"])
    if details["age"] >= 25:
        print(details["name"], "is 25 or older")
    else:
        print(details["age"], "is under 25")