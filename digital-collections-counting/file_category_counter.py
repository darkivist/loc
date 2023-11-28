from pathlib import Path
import collections
import csv

fileList = input("Please enter path to fileList.txt and press Enter: ")

file_extensions = []

with open(fileList,'r', errors='surrogateescape') as f:
    for line in f:
        p = Path(line.strip())
        forward = False
        file_extensions.append(p.suffix.lower())

print("Extensions detected:",file_extensions)

extension_count = collections.Counter(file_extensions)

file_extensions_clean = [ext[1:] if ext.startswith('.') else ext for ext in file_extensions]

type_counts = {}

with open('fdd_extensions_genre.csv') as f:
    reader = csv.reader(f)
    extension_types = {row[0]: row[1] for row in reader}

for ext in file_extensions_clean:
    if ext in extension_types:
        ext_type = extension_types[ext]
        if ext_type not in type_counts:
            type_counts[ext_type] = 0
        type_counts[ext_type] += 1
        
print("File category counts:", type_counts)