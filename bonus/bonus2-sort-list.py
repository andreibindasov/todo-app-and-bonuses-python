waiting_list = ["shawn", "bob", "john"]
waiting_list.sort()
# waiting_list.sort(reverse=True)

for i, item in enumerate(waiting_list):
    row = f"{i+1}.{item.capitalize()}"
    print(row)