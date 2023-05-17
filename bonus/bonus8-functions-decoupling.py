feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters


parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")

psw = input("Password: ")


def check_psw(p):
    result = {}
    is_digit = False
    is_upper = False

    if len(p) >= 8:
        result["len"] = True
    else:
        result["len"] = False

    for ch in p:
        if ch.isdigit():
            is_digit = True
        if ch.isupper():
            is_upper = True

    result["dig"] = is_digit
    result["up"] = is_upper

    return all(result.values())


if check_psw(psw):
    print("Strong")
else:
    print("weak")
