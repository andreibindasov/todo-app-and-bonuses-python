password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["len"] = True
else:
    result["len"] = False

digit = False
isUpper = False
for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        isUpper = True

result["digit"] = digit
result["upper"] = isUpper

print(result)

if all(result.values()):
    print("Strong password!")
else:
    print("Change your password!")


