p=input("Enter your password:")
if " " in p:
    print("Invalid Password,should not contain spaces")
elif len(p)<8 or len(p)>15:
    print("Invalid password,Password should be between 8 and 15 characters")
elif not any (char.isdigit()for char in p):
    print("Invalid password,must contain atleast one digit")
elif not any (char.islower()for char in p):
    print("Invalid password,must contain at least one lowercase letter")
elif not any (char.upper()for char in p):
    print("Invalid password,must contain at least one uppercase letter")
elif not any (char in"@#$%^&!*" for char in p):
    print("Invalid password,must contain at least one special character")
else:
    print("Password is valid")
