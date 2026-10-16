import re
from pathlib import Path




# get the first line of the file

line =" Pateint ID : P-1001 "

print(f"Length of the line:{len(line)}")

fields =["Patient Id:","Visit Data:","Doctor:","Notes:"]
errors=[]

errors.append("bad date")
errors.append("invalid date")

print("Doctor:" in fields)

#learning dictionary
record ={"Patient ID":1001, "Date":"2023-06-01"}

print(record["Patient ID"])
print(record.get("Date"))
record["Doctor"]= "Dr.Pai"
print(record.get("Doctor"))
print("Doctor" in record)

#learing conditions

size=0

if size==0:
    print("empty")
elif size > 10000:
    print("too big")
else:
    print("ok")

#learning for file handling

filename="/Users/madhavagumbe/Downloads/patient_note.txt"

file=Path(filename)

print(file.stat().st_size)

print(file.suffix)

print(file.name)

text=file.read_text(encoding="utf-8")

print(text)

raw=file.read_bytes()

print(raw)

with open(filename,encoding='utf-8') as f:
    for line in f:
        print(line.strip())

#for f in Path("/Users/madhavagumbe/Downloads").glob("*.txt"):
   #print(f.name)

try:
    text=file.read_text(encoding="utf-8")
    print("valid utf-8")
except UnicodeDecodeError:
    print("not a valid utf-8")



#functions

def check_file_not_empty(file):
    if file.stat().st_size == 0 :
        "file is empty"
    return "file is not empty"

problem = check_file_not_empty(Path("/Users/madhavagumbe/Downloads/patient_note.txt"))

print(problem)

print(re.search(r"\d{4}-\d{2}-\d{2}","2023-06-01"))
print(re.search(r"",Path(file).read_text(encoding="utf-8")))


import csv
with open("report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "result", "reason"])
    writer.writerow(["patient_note.txt", "FAIL", "PII found"])