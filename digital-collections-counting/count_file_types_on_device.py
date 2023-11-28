from pathlib import Path
import csv
import collections
import zipfile
import tarfile

count_path = input("Please enter path to count and press Enter: ")

file_extensions = []

for file_path in Path(count_path).rglob('*'):
    if file_path.is_file():
        if file_path.suffix in ['.zip', '.tar']:
            if file_path.suffix == '.zip':
                with zipfile.ZipFile(file_path) as archive:
                    for zipinfo in archive.infolist():
                        file_extensions.append(Path(zipinfo.filename).suffix.lower())
            else:
                with tarfile.open(file_path) as archive:
                    for tarinfo in archive:
                        if tarinfo.isreg():
                            file_extensions.append(Path(tarinfo.name).suffix.lower())
        else:
            file_extensions.append(file_path.suffix.lower())

extension_count = collections.Counter(file_extensions)

for ext, count in extension_count.items():
    print(f"{ext}: {count}")
