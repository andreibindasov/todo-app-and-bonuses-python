date = input("Enter today's date: ")
mood = input("Rate your today's mood from 1 to 10: ")
flow = input("let your thoughts flow:\n")

with open(f"../journal/{date}.txt", 'w') as f:
    f.write(mood + 2 * '\n')
    f.write(flow)

