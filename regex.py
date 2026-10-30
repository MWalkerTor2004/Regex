import re

pattern = re.compile(r'[A-Z]{3}[0-9]{4}')

with open("plates.txt") as f:
    next(f)
    for line in f:
        fields = line.strip().split('\t')
        plate = fields[5] if len(fields) > 5 else ''
        if pattern.match(plate):
            print(plate) 
