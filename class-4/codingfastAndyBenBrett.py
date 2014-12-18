from collections import defaultdict

data = {}
data = defaultdict(int)
raw_text = []

with open("names.txt", 'r') as f:
    raw_text = [text.split() for text in f.readlines()] #you could prolly slice into text.split() to get names [0]


d = {
    'JAMES': 1
}

d.setdefault('MARY', 0)
d = {
    'JAMES': 1,
    'MARY': 0
}
d.setdefault('JAMES', 0)
d = {
    'JAMES': 1,
    'MARY': 0
}

for line in raw_text:
    data[line[0]] += 1

#print data
for key, value in data.items():
    if value > 1:
        print(key)
        
        
#not sure why it's not working... testing:
for item in raw_text:
    counter = 0
    for other_item in raw_text:
        if item[0] == other_item[0]:
            counter += 1
        if counter == 2:
            print item
# no repeat elements??