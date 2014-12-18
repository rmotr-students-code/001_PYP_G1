names = {}

with open('names.txt', 'r') as f:
    for line in f:
         names.append(line.split()[0]
    test = [x for x in names if names[x] > 1]
    return test