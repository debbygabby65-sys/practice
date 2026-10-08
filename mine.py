resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },

    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 10,
        "available": 5
    },

    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada", 
    "F002": "John",
    "F003": "Grace"
}
borrow_records = []

def list_resources():
    for resource in resources:
        print(resource["id"])
        print(resource["name"])
        print(resource["category"])
        print(resource["total"])
        print(resource["available"])

def add_resource():
    resource_id = input("Enter your ID:")
    for resource in resources:
        if resource_id == resource["id"]:
            print("Resources ID already exists")
            return
    resource_name = input("Enter your name:")
    category = input("Enter your category:")
    total = int(input("Enter Total units:"))

    new_resource = {
        "id": resource_id,
        "name": resource_name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(new_resource)

add_resource()
list_resources()

def borrow_resource():
    fellow_id = input("Enter fellow ID:")
    if fellow_id in fellows:
        print("Fellow found")
        resource_id = input("Enter resource ID:")
        resource_found = False
        for resource in resources:
            if resource["id"] == resource_id:
                print("Resource found")  
                resource_found = True
                quantity = input("Enter quantity:")
                if not quantity.isdigit():
                    print("Quantity must be a positive integer")
                    return
                quantity = int(quantity)

                if quantity <= 0:
                    print("Quantity must be greater than 0")
                    return

          if quantity > resource["available"]:
    print("Not enough stock available")
    return
        print("Invalid fellow ID")



                