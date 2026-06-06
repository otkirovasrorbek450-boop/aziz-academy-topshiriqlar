username = input
age = int(input("Age: "))

if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")