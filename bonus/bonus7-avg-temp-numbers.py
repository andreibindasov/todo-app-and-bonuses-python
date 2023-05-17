def get_avg():
    with open("../files/temperatures.txt", 'r') as f:
        data = f.readlines()
    values = data[1:]
    values = [float(value) for value in values]

    avg_local = sum(values)/len(values)
    return avg_local


avg = get_avg()

print(avg)
