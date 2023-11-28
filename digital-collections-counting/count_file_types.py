from pathlib import Path
import collections

fileList = input("Please enter path to fileList.txt and press Enter: ")

file_extensions = []

with open(fileList,'r', errors='surrogateescape') as f:
    for line in f:
        p = Path(line.strip())
        forward = False
        file_extensions.append(p.suffix.lower())

#print(file_extensions)

extension_count = collections.Counter(file_extensions)

for file_extensions, count in extension_count.items():
    print(f"{file_extensions}: {count}x")