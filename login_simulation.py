users = {"admin": "password123"}

u = input("Username: ")
p = input("Password: ")

if users.get(u) == p:
    print("Login success")
else:
    print("Login failed")
