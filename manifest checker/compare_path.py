from pathlib import Path
import csv

input1 = input("Please enter path to fileList.txt and press Enter: ")

fileList = open(input1, "r")
data = fileList.read()
fileList_reformatted = data.replace('\n', '').split(",")
#print(fileList_reformatted)

input2 = input("Please enter path to content and press Enter: ")

p = Path(input2).rglob('*')
filePaths = [x for x in p if x.is_file()]
filePaths_string = [str(x) for x in filePaths]
#print(filePaths_string)

differences1 = []
for element in fileList_reformatted:
    if element not in filePaths_string:
        differences1.append(element)

print("The following files from the provided list were not found:",differences1)

with open("missing_files_report.csv","w",newline="\n") as f:
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(['filepath'])
    wr.writerow(differences1)

differences2 = []
for element in filePaths_string:
    if element not in fileList_reformatted:
        differences2.append(element)

print("The following unexpected files were found:",differences2)

with open("unexpected_files_report.csv","w",newline="\n") as f:
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(['filepath'])    
    wr.writerow(differences2)

wrong_location = []
for element in filePaths:
    if element.parts[-1].split("_")[0] != element.parent.parts[-1].split("_")[0]:
        wrong_location.append(element)
    
print("The following files may be in the wrong location:",wrong_location)

with open("wrong_location_report.csv","w",newline="\n") as f:
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(['filepath'])
    wr.writerow(wrong_location)
