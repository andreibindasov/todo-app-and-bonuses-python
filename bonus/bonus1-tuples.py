filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
filenames_t = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")

# changing dot to a dash in filenames

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

print(filenames)