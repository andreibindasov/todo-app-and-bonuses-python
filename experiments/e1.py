import glob

myfiles = glob.glob("../files/*.txt")

print(f"my files are ==> {myfiles}")

for filepath in myfiles:
    with open(filepath, 'r') as f:
        print(f.read().upper())