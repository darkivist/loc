#author: pakelly, 2023

from collections import Counter
import csv
import pandas as pd
from pathlib import Path
import tarfile
import zipfile

source = input("Count file extensions from filesystem or fileList.txt? (fs/list): ")
file_extensions = []

if source.lower() == 'fs':
    count_path = input("Please enter path to count and press Enter: ")
    for file_path in Path(count_path).rglob('*'):
            if file_path.suffix in ['.zip', '.tar']:
                if file_path.suffix == '.zip':
                    with zipfile.ZipFile(file_path) as archive:
                        for zipinfo in archive.infolist():
                            ext = Path(zipinfo.filename).suffix.lower()
                            file_extensions.append(ext)
            else:
                if file_path.suffix == '.tar':
                    with tarfile.open(file_path) as archive:
                        for tarinfo in archive:
                            if tarinfo.isreg():
                                ext = Path(tarinfo.filename).suffix.lower()
                                file_extensions.append(ext)
                else:
                    if file_path.is_file():
                        file_extensions.append(file_path.suffix.lower())

else:
    fileList = input("Please enter path to fileList.txt and press Enter: ")
    with open(fileList,'r', errors='surrogateescape') as f:
        for line in f:
            p = Path(line.strip())
            forward = False
            file_extensions.append(p.suffix.lower())

file_extensions_clean = [ext[1:] if ext.startswith('.') else ext for ext in file_extensions]

extension_count = Counter(file_extensions_clean)
    
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
        
new_counts = {} 
new_counts["manuscript"] = 0

for ext in file_extensions_clean:

  ext_type = extension_types.get(ext)

  if ext_type in ["sound", "moving-image", "still-image"]:
     new_counts[ext_type] = new_counts.get(ext_type, 0) + 1

  elif ext_type is None or ext_type not in ["sound", "moving-image", "still-image"]:
     new_counts["manuscript"] += 1

df = pd.DataFrame(columns=['Extension', 'FDD Type', 'LC Type']) 

for ext in file_extensions_clean:
    original_type = extension_types.get(ext, 0)
    new_type = new_counts.get(extension_types.get(ext), 'manuscript')
    if new_type != 'manuscript':
        new_type = extension_types.get(ext, 0)

    row = {'Extension': ext, 'FDD Type': original_type, 'LC Type': new_type}
    df = df.append(row, ignore_index=True)

extension_counts = df['Extension'].value_counts().reset_index()
extension_counts.columns = ['Extension', 'Count']

result_df = df.merge(extension_counts, on='Extension')
result_df = result_df.groupby('Extension').agg({'Count': 'first', 'FDD Type': 'first', 'LC Type': 'first'}).reset_index()

print(result_df)
print("FDD type counts:", type_counts)
print("LC type counts:", new_counts)

type_counts_text = f"FDD type counts: {type_counts}"
new_counts_text = f"LC type counts: {new_counts}"

categories_df = pd.DataFrame({'Extension': [type_counts_text, new_counts_text], 'FDD Type': [''] * 2, 'LC Type': [''] * 2, 'Count': [''] * 2})
categories_df = categories_df[['Extension', 'FDD Type', 'LC Type', 'Count']]

result_df = pd.concat([result_df] + [categories_df])
result_df.to_csv('format_count.csv', index=False)
