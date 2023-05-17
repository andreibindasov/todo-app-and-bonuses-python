from bonus.converters9 import convert
from bonus.parsers9 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")