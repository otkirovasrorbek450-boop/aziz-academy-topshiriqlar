role, active = input().split()
if role == "admin":
    if active == 1:
        print("Admin inactive")
    else:
        print("Admin active")
else:
    print("User")