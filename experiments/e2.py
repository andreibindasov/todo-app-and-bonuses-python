import csv

with open("weather.csv", 'r') as f:
    data = list(csv.reader(f))

# print(data)

city = input("Where? ")

for row in data:
    if row[0] == city:
        print(row[1])